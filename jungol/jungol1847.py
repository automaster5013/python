import sys

sys.setrecursionlimit(5000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    K = int(input_data[1])
    
    adj = [[] for _ in range(N + 1)]
    idx = 2
    for _ in range(N - 1):
        u, v, w = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3

    children = [[] for _ in range(N + 1)]
    bfs_order = []
    q = [1]
    visited = [False] * (N + 1)
    visited[1] = True
    idx_q = 0
    while idx_q < len(q):
        u = q[idx_q]
        idx_q += 1
        bfs_order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                children[u].append((v, w))
                q.append(v)
    
    post_order = bfs_order[::-1]
    
    INF = 10**15
    dp = [None] * (N + 1)
    sz = [0] * (N + 1)
    history = [[] for _ in range(N + 1)]
    
    for u in post_order:
        sz[u] = 1
        dp[u] = [[INF, INF] for _ in range(2)]
        dp[u][0][0] = 0
        dp[u][1][1] = 0
        
        for v, w in children[u]:
            dp_u = dp[u]
            dp_v = dp[v]
            sz_u = sz[u]
            sz_v = sz[v]
            
            limit = min(K, sz_u + sz_v)
            next_dp0 = [INF] * (limit + 1)
            next_dp1 = [INF] * (limit + 1)
            # hist[k][state] = kv * 2 + sv
            hist_uv0 = [0] * (limit + 1)
            hist_uv1 = [0] * (limit + 1)
            
            for ku in range(min(K, sz_u) + 1):
                u0, u1 = dp_u[ku][0], dp_u[ku][1]
                if u0 >= INF and u1 >= INF: continue
                
                for kv in range(min(K - ku, sz_v) + 1):
                    v0, v1 = dp_v[kv][0], dp_v[kv][1]
                    new_k = ku + kv
                    
                    if u0 < INF:
                        val0 = u0 + v0 + w
                        val1 = u0 + v1
                        if val0 < val1:
                            if val0 < next_dp0[new_k]:
                                next_dp0[new_k] = val0
                                hist_uv0[new_k] = (kv << 1) | 0
                        else:
                            if val1 < next_dp0[new_k]:
                                next_dp0[new_k] = val1
                                hist_uv0[new_k] = (kv << 1) | 1
                                
                    if u1 < INF:
                        val1 = u1 + v1 + w
                        val0 = u1 + v0
                        if val1 < val0:
                            if val1 < next_dp1[new_k]:
                                next_dp1[new_k] = val1
                                hist_uv1[new_k] = (kv << 1) | 1
                        else:
                            if val0 < next_dp1[new_k]:
                                next_dp1[new_k] = val0
                                hist_uv1[new_k] = (kv << 1) | 0
            
            dp[u] = [ [next_dp0[k], next_dp1[k]] for k in range(limit + 1) ]
            sz[u] += sz_v
            history[u].append((v, hist_uv0, hist_uv1))

    if dp[1][K][0] <= dp[1][K][1]:
        print(dp[1][K][0])
        start_state = 0
    else:
        print(dp[1][K][1])
        start_state = 1
    
    ans_nodes = []
    def backtrack(u, k, state):
        if state == 1:
            ans_nodes.append(u)
        curr_k = k
        for v, h0, h1 in reversed(history[u]):
            packed = h0[curr_k] if state == 0 else h1[curr_k]
            kv = packed >> 1
            sv = packed & 1
            backtrack(v, kv, sv)
            curr_k -= kv
            
    backtrack(1, K, start_state)
    ans_nodes.sort()
    print(*(ans_nodes))

if __name__ == '__main__':
    solve()

################################################################################



