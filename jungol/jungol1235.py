import sys

sys.setrecursionlimit(5000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    p = int(input_data[0])
    brands = list(map(int, input_data[1:]))
    
    brand_indices = [[] for _ in range(101)]
    for idx, b in enumerate(brands):
        brand_indices[b].append(idx)
        
    memo = [[-1] * p for _ in range(p)]

    def get_max_matches(i, j):
        if i >= j:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        res = get_max_matches(i + 1, j)
        
        target_brand = brands[i]
        indices = brand_indices[target_brand]
        
        for k in indices:
            if k <= i: continue
            if k > j: break
            
            if (k - i) % 2 == 1:
                val = 1 + get_max_matches(i + 1, k - 1) + get_max_matches(k + 1, j)
                if val > res:
                    res = val
        
        memo[i][j] = res
        return res

    print(get_max_matches(0, p - 1))

if __name__ == "__main__":
    solve()

####################################################################################3

