import sys

# 재귀 깊이 제한 해제 또는 반복문 DFS 권장
sys.setrecursionlimit(500000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    adj = [[] for _ in range(n + 1)]
    ptr = 1
    for _ in range(n - 1):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    
    # 1. 반복문 DFS를 통해 방문 순서(Post-order)와 깊이 계산
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)
                
    # 2. 서브트리 크기 계산 (역순 방문)
    sz = [1] * (n + 1)
    total_depth_sum = 0
    lca_depth_contribution = 0
    
    for u in reversed(order):
        if u == 1: 
            total_depth_sum += depth[u]
            continue
            
        total_depth_sum += depth[u]
        # 해당 노드 u의 부모로 가는 간선이 LCA 경로에 포함되는 횟수
        lca_depth_contribution += sz[u] * (sz[u] - 1) // 2
        
        p = parent[u]
        if p != -1:
            sz[p] += sz[u]
            
    # 3. 최종 공식 적용
    # (N-1) * sum(depth) - sum(sz*(sz-1)//2)
    ans = (n - 1) * total_depth_sum - lca_depth_contribution
    print(ans)

if __name__ == "__main__":
    solve()

####################################################################

