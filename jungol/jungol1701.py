import sys

def solve():
    s = sys.stdin.readline().strip()
    if not s:
        print(0)
        return
    
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    def is_pair(x, y):
        return (x == 'a' and y == 't') or (x == 'g' and y == 'c')

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            
            if is_pair(s[i], s[j]):
                if l == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2
            
            for k in range(i, j):
                if dp[i][j] < dp[i][k] + dp[k+1][j]:
                    dp[i][j] = dp[i][k] + dp[k+1][j]

    print(dp[0][n-1])

if __name__ == "__main__":
    solve()

####################################################################


