import sys

# 대규모 그래프를 위해 재귀 한도 확장
sys.setrecursionlimit(10**6)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        u = int(input_data[2 + 2*i])
        v = int(input_data[3 + 2*i])
        adj[u].append(v)
        adj[v].append(u)

    dfn = [0] * (N + 1)
    low = [0] * (N + 1)
    comp_split = [0] * (N + 1)
    timer = 1

    def dfs(u, p):
        nonlocal timer
        dfn[u] = low[u] = timer
        timer += 1
        
        for v in adj[u]:
            if v == p:
                continue
            if dfn[v]:
                low[u] = min(low[u], dfn[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                # 절점 판정 조건: 자식 v가 u의 조상으로 갈 수 없을 때
                if low[v] >= dfn[u]:
                    comp_split[u] += 1

    # 그래프가 연결되어 있으므로 1번 노드에서 시작
    dfs(1, -1)
    
    K = M - N + 1
    total_sum = 0
    
    for v in range(1, N + 1):
        # comp'(v) 계산
        if v == 1:
            c_prime = comp_split[1]
        else:
            c_prime = comp_split[v] + 1
        
        # 사이클 제거 조건 확인
        if len(adj[v]) - c_prime == K:
            total_sum += v
            
    print(total_sum)

solve()

##################################################################3

