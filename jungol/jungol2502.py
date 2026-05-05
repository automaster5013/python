import sys

input_data = sys.stdin.read().split()

def solve():
    if not input_data:
        return
    
    N = int(input_data[0])
    pref_friends = [[0] * (N + 1) for _ in range(N + 1)]
    
    ptr = 1
    total_edges = 0
    for i in range(1, N + 1):
        row = pref_friends[i]
        while True:
            friend = int(input_data[ptr])
            ptr += 1
            if friend == 0:
                break
            row[friend] = 1
            if i < friend:
                total_edges += 1
        
        s = 0
        for j in range(1, N + 1):
            if row[j]:
                s += 1
            row[j] = s

    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    best_l = [0] * (N + 1) 
    
    pairs = [s * (s - 1) // 2 for s in range(N + 1)]
    
    for r in range(1, N + 1):
        edges_in_module = 0
        for l in range(r, 0, -1):
            edges_in_module += pref_friends[l][r] - pref_friends[l][l]
            
            cost = pairs[r - l + 1] - (edges_in_module << 1)
            val = dp[l - 1] + cost
            
            if val < dp[r]:
                dp[r] = val
                best_l[r] = l

    print(int(dp[N] + total_edges))
    
    res = []
    curr = N
    while curr > 0:
        l = best_l[curr]
        res.append(curr - l + 1)
        curr = l - 1
    
    res.reverse()
    print(len(res), *res)

if __name__ == "__main__":
    solve()

########################################################################################3



