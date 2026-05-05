import sys
from collections import deque

# 재귀 깊이 제한 해제 (필요시) 및 빠른 입력 설정
sys.setrecursionlimit(10**6)
input = sys.stdin.read

def solve():
    data = input().split()
    if not data: return
    
    N, M = int(data[0]), int(data[1])
    adj = [[] for _ in range(N + 1)]
    ptr = 2
    for _ in range(M):
        u, v = int(data[ptr]), int(data[ptr+1])
        adj[u].append(v)
        ptr += 2
        
    cash = [0] * (N + 1)
    for i in range(1, N + 1):
        cash[i] = int(data[ptr])
        ptr += 1
        
    S = int(data[ptr])
    P = int(data[ptr+1])
    ptr += 2
    
    restaurants = set()
    for _ in range(P):
        restaurants.add(int(data[ptr]))
        ptr += 1
        
    # 1. SCC 추출 (Tarjan's Algorithm - Iterative)
    dfn = [0] * (N + 1)
    low = [0] * (N + 1)
    stack = []
    in_stack = [False] * (N + 1)
    scc_id = [0] * (N + 1)
    timer = 0
    scc_cnt = 0
    
    for i in range(1, N + 1):
        if dfn[i] == 0:
            dfs_stack = [(i, 0)]
            while dfs_stack:
                u, edge_idx = dfs_stack.pop()
                if edge_idx == 0:
                    timer += 1
                    dfn[u] = low[u] = timer
                    stack.append(u)
                    in_stack[u] = True
                
                found = False
                for j in range(edge_idx, len(adj[u])):
                    v = adj[u][j]
                    if dfn[v] == 0:
                        dfs_stack.append((u, j + 1))
                        dfs_stack.append((v, 0))
                        found = True
                        break
                    elif in_stack[v]:
                        low[u] = min(low[u], dfn[v])
                
                if found: continue
                
                if low[u] == dfn[u]:
                    scc_cnt += 1
                    while True:
                        node = stack.pop()
                        in_stack[node] = False
                        scc_id[node] = scc_cnt
                        if node == u: break
                
                if dfs_stack:
                    parent, _ = dfs_stack[-1]
                    low[parent] = min(low[parent], low[u])

    # 2. DAG 생성 및 데이터 압축
    scc_cash = [0] * (scc_cnt + 1)
    scc_adj = [set() for _ in range(scc_cnt + 1)]
    scc_restaurant = [False] * (scc_cnt + 1)
    indegree = [0] * (scc_cnt + 1)
    
    for u in range(1, N + 1):
        u_id = scc_id[u]
        scc_cash[u_id] += cash[u]
        if u in restaurants:
            scc_restaurant[u_id] = True
        for v in adj[u]:
            v_id = scc_id[v]
            if u_id != v_id:
                if v_id not in scc_adj[u_id]:
                    scc_adj[u_id].add(v_id)
                    indegree[v_id] += 1
                    
    # 3. 위상 정렬을 이용한 최장 경로 DP
    start_scc = scc_id[S]
    dp = [-1] * (scc_cnt + 1)
    dp[start_scc] = scc_cash[start_scc]
    
    queue = deque([i for i in range(1, scc_cnt + 1) if indegree[i] == 0])
    
    while queue:
        u = queue.popleft()
        for v in scc_adj[u]:
            if dp[u] != -1: # 출발점 S로부터 도달 가능한 경우만 갱신
                dp[v] = max(dp[v], dp[u] + scc_cash[v])
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
                
    # 4. 결과 출력: 레스토랑이 있는 SCC들 중 DP 최댓값
    ans = 0
    for i in range(1, scc_cnt + 1):
        if scc_restaurant[i] and dp[i] != -1:
            ans = max(ans, dp[i])
            
    sys.stdout.write(str(ans) + '\n')

solve()

#####################################################################################



