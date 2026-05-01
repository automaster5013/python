import sys

# 반복문 기반 DFS로 트리 평면화 수행
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    Q = int(input_data[ptr]); ptr += 1
    
    # 초기 연봉 저장 및 인접 리스트 생성
    initial_salaries = [0] * (N + 1)
    adj = [[] for _ in range(N + 1)]
    
    initial_salaries[1] = int(input_data[ptr]); ptr += 1
    for i in range(2, N + 1):
        sal = int(input_data[ptr]); ptr += 1
        boss = int(input_data[ptr]); ptr += 1
        initial_salaries[i] = sal
        adj[boss].append(i)
        
    # 오일러 경로 테크닉 (Iterative DFS)
    in_time = [0] * (N + 1)
    out_time = [0] * (N + 1)
    timer = 0
    
    stack = [1]
    adj_ptr = [0] * (N + 1)
    
    while stack:
        u = stack[-1]
        if in_time[u] == 0:
            timer += 1
            in_time[u] = timer
            
        if adj_ptr[u] < len(adj[u]):
            v = adj[u][adj_ptr[u]]
            adj_ptr[u] += 1
            stack.append(v)
        else:
            out_time[u] = timer
            stack.pop()
            
    # 펜윅 트리 (차분 배열 기반 구간 업데이트용)
    bit = [0] * (N + 2)
    
    def update(idx, val):
        while idx <= N:
            bit[idx] += val
            idx += idx & -idx
            
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s

    output = []
    for _ in range(Q):
        cmd = input_data[ptr]; ptr += 1
        if cmd == 'p':
            i = int(input_data[ptr]); ptr += 1
            x = int(input_data[ptr]); ptr += 1
            # i번 사원의 부하 직원 범위: [in_time[i]+1, out_time[i]]
            start = in_time[i] + 1
            end = out_time[i]
            if start <= end:
                update(start, x)
                update(end + 1, -x)
        else:
            i = int(input_data[ptr]); ptr += 1
            # 현재 연봉 = 초기 연봉 + 누적 변화량
            res = initial_salaries[i] + query(in_time[i])
            output.append(str(res))
            
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

###########################################################################

