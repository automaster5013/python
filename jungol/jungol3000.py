import sys

# 반복문 기반 DFS를 사용하여 재귀 깊이 문제를 방지하고 속도를 높임
def solve():
    # 빠른 입출력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    Q = int(input_data[ptr]); ptr += 1
    
    adj = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        p = int(input_data[ptr]); ptr += 1
        adj[p].append(i)
        
    # 오일러 투어 및 LCA를 위한 준비
    tin = [0] * (N + 1)
    tout = [0] * (N + 1)
    depth = [0] * (N + 1)
    LOG = 18
    up = [[0] * (N + 1) for _ in range(LOG + 1)]
    timer = 0
    
    # Iterative DFS
    stack = [1]
    visited_count = [0] * (N + 1)
    depth[1] = 0
    while stack:
        u = stack[-1]
        if visited_count[u] == 0:
            timer += 1
            tin[u] = timer
        
        if visited_count[u] < len(adj[u]):
            v = adj[u][visited_count[u]]
            visited_count[u] += 1
            depth[v] = depth[u] + 1
            up[0][v] = u
            stack.append(v)
        else:
            tout[u] = timer
            stack.pop()

    # LCA Binary Lifting 테이블 구성
    for j in range(1, LOG + 1):
        prev_up = up[j-1]
        curr_up = up[j]
        for i in range(1, N + 1):
            mid = prev_up[i]
            if mid != 0:
                curr_up[i] = prev_up[mid]

    def get_lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for j in range(LOG + 1):
            if (diff >> j) & 1:
                u = up[j][u]
        if u == v:
            return u
        for j in range(LOG, -1, -1):
            if up[j][u] != up[j][v]:
                u = up[j][u]
                v = up[j][v]
        return up[0][u]

    # 펜윅 트리 (구간 업데이트, 점 쿼리용)
    bit = [0] * (N + 2)
    def bit_update(i, delta):
        while i <= N:
            bit[i] += delta
            i += i & (-i)
    
    def bit_query(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & (-i)
        return res

    marked = [False] * (N + 1)
    results = []
    
    # 작업 수행
    for _ in range(Q):
        if ptr >= len(input_data): break
        b = int(input_data[ptr]); ptr += 1
        c = int(input_data[ptr]); ptr += 1
        d = int(input_data[ptr]); ptr += 1
        
        lca = get_lca(b, c)
        
        # 경로 상에 마킹된 정점이 있는지 확인
        sb = bit_query(tin[b])
        sc = bit_query(tin[c])
        slca = bit_query(tin[lca])
        
        # b->LCA와 c->LCA 경로 모두 마킹된 정점이 없어야 연결됨
        is_connected = (sb == slca) and (sc == slca)
        
        if is_connected:
            results.append("YES")
            if d == 1:
                if b != 1 and not marked[b]:
                    marked[b] = True
                    bit_update(tin[b], 1)
                    bit_update(tout[b] + 1, -1)
        else:
            results.append("NO")
            if d == 1:
                if c != 1 and not marked[c]:
                    marked[c] = True
                    bit_update(tin[c], 1)
                    bit_update(tout[c] + 1, -1)

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

#####################################################################

