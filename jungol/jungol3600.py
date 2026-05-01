import sys

def solve():
    # 모든 데이터를 한 번에 읽어 처리 속도를 높입니다.
    data = sys.stdin.read().split()
    if not data:
        return
    
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    
    # 인접 리스트 생성
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    # DFS Order (Euler Tour Technique)를 반복문으로 구현
    in_time = [0] * (N + 1)
    out_time = [0] * (N + 1)
    timer = 0
    
    stack = [1]
    visited = [False] * (N + 1)
    visited[1] = True
    adj_idx = [0] * (N + 1) # 자식 노드 순회를 위한 인덱스
    
    while stack:
        u = stack[-1]
        if in_time[u] == 0:
            timer += 1
            in_time[u] = timer
        
        found_child = False
        while adj_idx[u] < len(adj[u]):
            v = adj[u][adj_idx[u]]
            adj_idx[u] += 1
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                found_child = True
                break
        
        if not found_child:
            out_time[u] = timer
            stack.pop()
            
    # 펜윅 트리 (Binary Indexed Tree)
    bit = [0] * (N + 1)
    
    def update(idx, val):
        while idx <= N:
            bit[idx] += val
            idx += idx & -idx
            
    def get_sum(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s
    
    # 현재 각 노드의 가중치를 저장 (업데이트 시 차이값을 구하기 위함)
    current_weights = [0] * (N + 1)
    
    Q = int(data[ptr])
    ptr += 1
    output = []
    
    for _ in range(Q):
        q_type = int(data[ptr])
        if q_type == 1:
            a = int(data[ptr+1])
            x = int(data[ptr+2])
            # 기존 값과의 차이만큼 트리에 반영
            diff = x - current_weights[a]
            update(in_time[a], diff)
            current_weights[a] = x
            ptr += 3
        else:
            a = int(data[ptr+1])
            # 서브트리 구간 [in_time, out_time]의 합 계산
            res = get_sum(out_time[a]) - get_sum(in_time[a] - 1)
            output.append(str(res))
            ptr += 2
            
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

########################################################################3

