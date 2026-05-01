import sys

# 빠른 입출력 설정
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    ptr = 0
    N = int(data[ptr]); ptr += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
    
    # 1. 트리 정보 구하기 (Depth & Parent) - Iterative DFS
    # LOG = 19 (2^18 < 300,000 < 2^19)
    LOG = 19
    parent = [[0] * LOG for _ in range(N + 1)]
    depth = [-1] * (N + 1)
    
    stack = [(1, 0, 0)] # (node, p, d)
    depth[1] = 0
    
    # 반복문 DFS로 재귀 오버헤드 방지
    while stack:
        curr, p, d = stack.pop()
        parent[curr][0] = p
        depth[curr] = d
        for nxt in adj[curr]:
            if depth[nxt] == -1:
                depth[nxt] = d + 1
                stack.append((nxt, curr, d + 1))
                
    # 2. 희소 테이블(Sparse Table) 구성: O(N log N)
    for j in range(1, LOG):
        for i in range(1, N + 1):
            if parent[i][j-1] != 0:
                parent[i][j] = parent[parent[i][j-1]][j-1]
                
    # 3. LCA Query 처리: O(Q log N)
    Q = int(data[ptr]); ptr += 1
    results = []
    
    for _ in range(Q):
        u = int(data[ptr]); ptr += 1
        v = int(data[ptr]); ptr += 1
        
        # 항상 v의 깊이가 더 깊도록 설정
        if depth[u] > depth[v]:
            u, v = v, u
            
        # 깊이 맞추기 (Jump)
        diff = depth[v] - depth[u]
        for j in range(LOG):
            if (diff >> j) & 1:
                v = parent[v][j]
                
        # 깊이가 같아졌을 때 노드가 같다면 해당 노드가 LCA
        if u == v:
            results.append(str(u))
            continue
            
        # 동시에 위로 점프하며 공통 조상 바로 아래까지 이동
        for j in range(LOG - 1, -1, -1):
            if parent[u][j] != parent[v][j]:
                u = parent[u][j]
                v = parent[v][j]
                
        results.append(str(parent[u][0]))
        
    # 결과 일괄 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

###############################################################3

