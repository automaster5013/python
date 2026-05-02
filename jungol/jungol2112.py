import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    try:
        n = int(input_data[0])
    except ValueError:
        return

    # N이 홀수라면 타일로 가득 채울 수 없습니다.
    if n % 2 != 0:
        print(0)
        return

    # dp[i]는 3 * i 크기를 채우는 경우의 수
    dp = [0] * (n + 1)
    
    # 기저 사례 (Base Case)
    dp[0] = 1 # 0인 경우 아무것도 놓지 않는 한 가지 경우로 간주
    if n >= 2:
        dp[2] = 3

    # DP 테이블 채우기
    for i in range(4, n + 1, 2):
        # f(i-2)에서 3가지 경우가 파생됨
        dp[i] = dp[i-2] * 3
        # i-4, i-6... 등 이전 단계에서 발생하는 2가지씩의 특수 모양 합산
        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2

    print(dp[n])

if __name__ == "__main__":
    solve()

#############################################################################


