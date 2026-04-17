def solve():
    # 1. 테스트 케이스 수 입력
    t_input = input()
    if not t_input:
        return
    T_cases = int(t_input)
    
    MOD = 1000000007

    # 팩토리얼 사전 계산 (결과값 해시용)
    fact = [1] * 100005
    for i in range(2, 100005):
        fact[i] = (fact[i-1] * i) % MOD

    for t_idx in range(1, T_cases + 1):
        # N 입력 처리 (빈 줄이 있을 수 있으므로 체크)
        n_line = input()
        while not n_line.strip():
            n_line = input()
        N = int(n_line)
        
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        
        # 2. 트리 순회 순서 생성 (Iterative DFS)
        # sys.setrecursionlimit을 못 쓰므로 무조건 반복문으로 순서를 뽑아야 합니다.
        order = []
        parent = [0] * (N + 1)
        stack = [1]
        parent[1] = -1
        
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == 0:
                    parent[v] = u
                    stack.append(v)
        
        # 3. Bottom-up DP (자식 -> 부모 방향)
        # dp0[u]: u를 포함하지 않는 u 서브트리의 최대 독립 집합(MIS)
        # dp1[u]: u를 포함하는 u 서브트리의 최대 독립 집합(MIS)
        dp0 = [0] * (N + 1)
        dp1 = [0] * (N + 1)
        
        for u in reversed(order):
            dp0[u] = 0
            dp1[u] = 1
            for v in adj[u]:
                if v != parent[u]:
                    dp0[u] += max(dp0[v], dp1[v])
                    dp1[u] += dp0[v]
        
        # 4. Top-down DP (부모 -> 자식 방향, Rerooting)
        # up0[v]: v의 부모쪽 컴포넌트에서 부모 u를 포함하지 않을 때의 MIS
        # up1[v]: v의 부모쪽 컴포넌트에서 부모 u를 포함할 때의 MIS
        up0 = [0] * (N + 1)
        up1 = [0] * (N + 1)
        
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    # u를 제외한 상단부의 MIS 계산
                    # v 입장에서 부모 u를 선택하지 않는 경우
                    up0[v] = max(up0[u], up1[u]) + (dp0[u] - max(dp0[v], dp1[v]))
                    # v 입장에서 부모 u를 선택하는 경우
                    up1[v] = 1 + up0[u] + (dp1[u] - 1 - dp0[v])
        
        # 5. Ai 계산 및 결과 합산
        # Ai = i번 노드를 제거했을 때 남은 포레스트의 MIS 총합
        ans = 0
        for i in range(1, N + 1):
            Ai = dp0[i] + max(up0[i], up1[i])
            # 문제에서 요구하는 특정 해시 합산 방식 (A_i * i!)
            ans = (ans + (Ai * fact[i])) % MOD
            
        print(f"#{t_idx} {ans}")

# 프로그램 시작
if __name__ == "__main__":
    solve()