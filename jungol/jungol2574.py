import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    N = int(input[ptr]); ptr += 1
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(N - 1):
        u = int(input[ptr]); ptr += 1
        v = int(input[ptr]); ptr += 1
        adj[u].append(v)
        adj[v].append(u)
        
    # DP 테이블 초기화: [얼리X일때 최소값, 얼리O일때 최소값]
    dp = [[0, 1] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    parent = [0] * (N + 1)
    
    # 1. BFS 또는 DFS를 사용하여 순회 순서(자식->부모 순서)를 만듭니다.
    order = []
    stack = [1]
    visited[1] = True
    
    while stack:
        curr = stack.pop()
        order.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr
                stack.append(neighbor)
                
    # 2. 리프 노드부터 거꾸로 올라오며(후위 순회 방식) DP 값을 채웁니다.
    for i in range(N - 1, -1, -1):
        curr = order[i]
        p = parent[curr]
        
        # 루트 노드가 아닌 경우에만 부모의 DP 값을 갱신
        if p != 0:
            dp[p][0] += dp[curr][1]
            dp[p][1] += min(dp[curr][0], dp[curr][1])
            
    # 루트 노드(1번)에서 두 경우 중 최소값 출력
    print(min(dp[1][0], dp[1][1]))

if __name__ == "__main__":
    solve()

##########################################################################

