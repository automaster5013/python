import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    MOD = 1000000003
    
    # 절반보다 많이 선택하는 것은 불가능 (인접하지 않아야 하므로)
    if n < 2 * k:
        print(0)
        return

    # dp[i][j]: i개 색 중에서 j개를 인접하지 않게 고르는 경우의 수 (직선)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # 초기화
    for i in range(n + 1):
        dp[i][0] = 1  # 아무것도 고르지 않는 경우 1가지
        dp[i][1] = i  # i개 중 1개를 고르는 경우 i가지
        
    # DP 테이블 채우기
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            # i번째를 선택하지 않음 + i번째를 선택함(i-2개 중 j-1개 선택)
            dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % MOD
            
    # 원형 색상환 공식 적용
    # 1번 색을 선택한 경우: dp[n-3][k-1]
    # 1번 색을 선택하지 않은 경우: dp[n-1][k]
    # 단, n=4, k=2 같은 케이스에서 n-3이 1이 될 수 있으므로 인덱스 주의
    ans = (dp[n-3][k-1] + dp[n-1][k]) % MOD
    print(ans)

if __name__ == "__main__":
    solve()

###########################################################################3


