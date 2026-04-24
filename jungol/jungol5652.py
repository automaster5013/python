import sys

def solve():
    # 입력 속도 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    adj = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        u = int(input_data[2 + 2*i])
        v = int(input_data[3 + 2*i])
        adj[u].append(v)
        adj[v].append(u)

    # 1. 부모 노드와 방문 순서를 정하기 위한 BFS (위상 정렬 효과)
    parent = [0] * (N + 1)
    order = []
    queue = [1]
    visited = [False] * (N + 1)
    visited[1] = True
    
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    
    # 2. 리프 노드부터 거꾸로 올라오며 DP 수행 (Bottom-up)
    dp = [0] * (N + 1)
    ans = 0
    
    for u in reversed(order):
        m1, m2 = -1, -1
        for v in adj[u]:
            if v == parent[u]:
                continue
            
            # 자식 노드의 dp 값이 -1이면 이미 그쪽 분기에 주유소가 설치됨
            if dp[v] == -1:
                d = -1
            else:
                d = dp[v] + 1 # u에서 v의 서브트리로 내려가는 경로 길이
            
            if d > m1:
                m2 = m1
                m1 = d
            elif d > m2:
                m2 = d
        
        # 주유소 설치 조건 체크
        if m1 >= K or (m1 != -1 and m2 != -1 and m1 + m2 >= K):
            ans += 1
            dp[u] = -1 # u에 주유소를 설치함
        else:
            dp[u] = max(0, m1)
                
    print(ans)

if __name__ == '__main__':
    solve()

#############################################################################(방법01)


