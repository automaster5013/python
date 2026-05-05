import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    K = int(input_data[0])
    S = input_data[1]
    N = len(S)
    num_chunks = N // K
    
    matches_in = [[0] * K for _ in range(K)]
    matches_between = [[0] * K for _ in range(K)]
    
    for i in range(num_chunks):
        chunk = S[i*K : (i+1)*K]
        for u in range(K):
            char_u = chunk[u]
            for v in range(u + 1, K):
                if char_u == chunk[v]:
                    matches_in[u][v] += 1
                    matches_in[v][u] += 1
                    
    for i in range(num_chunks - 1):
        c1 = S[i*K : (i+1)*K]
        c2 = S[(i+1)*K : (i+2)*K]
        for u in range(K):
            char_u = c1[u]
            for v in range(K):
                if char_u == c2[v]:
                    matches_between[u][v] += 1

    max_total_matches = 0
    pow2 = [1 << i for i in range(K)]
    full_mask = (1 << K) - 1
    
    for s in range(K):
        dp = [-1] * (K << K)
        dp[pow2[s] * K + s] = 0
        
        for mask in range(1, 1 << K):
            mask_k = mask * K
            for u in range(K):
                score = dp[mask_k + u]
                if score == -1:
                    continue
                
                remaining = full_mask ^ mask
                m_in_u = matches_in[u]
                while remaining:
                    lsb = remaining & -remaining
                    v = lsb.bit_length() - 1
                    remaining &= remaining - 1
                    
                    new_idx = (mask | lsb) * K + v
                    new_score = score + m_in_u[v]
                    if new_score > dp[new_idx]:
                        dp[new_idx] = new_score
        
        full_idx_base = full_mask * K
        m_btw_row = [matches_between[e][s] for e in range(K)]
        for e in range(K):
            final_score = dp[full_idx_base + e]
            if final_score != -1:
                total = final_score + m_btw_row[e]
                if total > max_total_matches:
                    max_total_matches = total
                    
    print(N - max_total_matches)

if __name__ == "__main__":
    solve()

##########################################################################



