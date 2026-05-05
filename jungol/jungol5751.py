import sys

# 대규모 트리를 처리하기 위해 재귀 한도와 입력을 최적화합니다.
sys.setrecursionlimit(300000)
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u, v = int(data[idx]), int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # dp[u][0]: u를 포함하지 않는 서브트리의 MIS 크기
    # dp[u][1]: u를 포함하는 서브트리의 MIS 크기
    dp = [[0, 0] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    
    # Bottom-up 순서를 위한 트래버스
    visited = [False] * (n + 1)
    visited[1] = True
    q = [1]
    while q:
        u = q.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

    # 단계 1: 서브트리 DP (Bottom-up)
    for u in reversed(order):
        dp[u][0] = 0
        dp[u][1] = 1
        for v in adj[u]:
            if v == parent[u]: continue
            dp[u][0] += max(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]

    # 단계 2: Rerooting DP (Top-down)
    # up[u][0]: u를 포함하지 않는 '위쪽' 트리의 MIS 크기
    # up[u][1]: u를 포함하는 '위쪽' 트리의 MIS 크기
    up = [[0, 0] for _ in range(n + 1)]
    
    for u in order:
        for v in adj[u]:
            if v == parent[u]: continue
            # v를 제외한 u의 다른 자식들과 부모 쪽에서 오는 정보를 합산
            # u를 선택하지 않을 때 v 방향으로 줄 수 있는 최대치
            up[v][0] = (dp[u][0] - max(dp[v][0], dp[v][1])) + max(up[u][0], up[u][1])
            # u를 선택할 때 v 방향으로 줄 수 있는 최대치 (u 선택 시 자식 v는 선택 불가)
            up[v][1] = (dp[u][1] - dp[v][0]) + up[u][0]

    # 단계 3: 모든 MIS에 포함되는 정점 M 판별
    # H[u][0]: u를 선택하지 않았을 때 전체 트리의 MIS 크기
    # H[u][1]: u를 선택했을 때 전체 트리의 MIS 크기
    alpha = max(dp[1][0], dp[1][1]) # 전체 트리의 최대 독립 집합 크기
    m_count = 0
    
    for u in range(1, n + 1):
        h0 = dp[u][0] + max(up[u][0], up[u][1])
        h1 = dp[u][1] + up[u][0]
        
        # u를 선택하지 않았을 때의 최대 크기가 전체 최대치(alpha)보다 작다면
        # u는 모든 최대 독립 집합에 반드시 포함되어야 함
        if h0 < alpha:
            m_count += 1

    # 최종 결과 계산: 전체 쌍 - (M에서 2개를 뽑는 쌍)
    total_pairs = n * (n - 1) // 2
    bad_pairs = m_count * (m_count - 1) // 2
    print(total_pairs - bad_pairs)

solve()

#############################################################################################



