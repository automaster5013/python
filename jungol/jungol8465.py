import sys
from collections import deque

def solve():
    # 입력 처리 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    
    ptr = 2
    for _ in range(m):
        if ptr + 1 >= len(input_data): break
        u, v = int(input_data[ptr]), int(input_data[ptr+1])
        adj[u].append(v)
        rev_adj[v].append(u)
        ptr += 2
        
    # 1. 1번 마을에서 도달 가능한 노드 탐색 (visit1)
    visit1 = [False] * (n + 1)
    q = deque([1])
    visit1[1] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visit1[v]:
                visit1[v] = True
                q.append(v)
                
    # 2. 2번 마을로 도달 가능한 노드 탐색 (visit2) - 역방향 그래프 사용
    visit2 = [False] * (n + 1)
    q = deque([2])
    visit2[2] = True
    while q:
        u = q.popleft()
        for v in rev_adj[u]:
            if not visit2[v]:
                visit2[v] = True
                q.append(v)
                
    # 3. 유효 노드(relevant) 필터링
    is_relevant = [False] * (n + 1)
    relevant_nodes = []
    for i in range(1, n + 1):
        if visit1[i] and visit2[i]:
            is_relevant[i] = True
            relevant_nodes.append(i)
            
    # 4. 유효 그래프에서의 진입 차수(in-degree) 계산
    in_degree = [0] * (n + 1)
    for u in relevant_nodes:
        for v in adj[u]:
            if is_relevant[v]:
                in_degree[v] += 1
                
    # 5. 위상 정렬 및 DP 수행
    q = deque([i for i in relevant_nodes if in_degree[i] == 0])
    dp = [0] * (n + 1)
    if 1 in relevant_nodes:
        dp[1] = 1
        
    processed_count = 0
    MOD = 1000000000
    
    while q:
        u = q.popleft()
        processed_count += 1
        
        for v in adj[u]:
            if is_relevant[v]:
                dp[v] = (dp[v] + dp[u]) % MOD
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
    # 6. 결과 검증 및 출력
    # 모든 유효 노드가 위상 정렬되지 않았다면 사이클 존재
    if processed_count < len(relevant_nodes):
        print("inf")
    else:
        print(dp[2])

if __name__ == "__main__":
    solve()

#######################################################################3


