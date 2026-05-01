import sys
from bisect import bisect_right

sys.setrecursionlimit(100000)

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    m = int(input[1])
    
    a = list(map(int, input[2:2+n]))
    queries = []
    curr = 2 + n
    for _ in range(m):
        queries.append(list(map(int, input[curr:curr+3])))
        curr += 3

    tree = [None] * (4 * n)
    
    def build(node, start, end):
        if start == end:
            tree[node] = [a[start]]
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = sorted(tree[2 * node] + tree[2 * node + 1])

    build(1, 0, n - 1)

    def count_le(node, start, end, l, r, val):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return bisect_right(tree[node], val)
        mid = (start + end) // 2
        return count_le(2 * node, start, mid, l, r, val) + \
               count_le(2 * node + 1, mid + 1, end, l, r, val)

    sorted_a = sorted(a)
    
    results = []
    for q_i, q_j, q_k in queries:
        l, r, k = q_i - 1, q_j - 1, q_k
        
        low = 0
        high = n - 1
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            mid_val = sorted_a[mid]
            
            if count_le(1, 0, n - 1, l, r, mid_val) >= k:
                ans = mid_val
                high = mid - 1
            else:
                low = mid + 1
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

######################################################################

