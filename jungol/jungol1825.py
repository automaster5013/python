import sys

def solve():
    # 투자 금액 N, 기업의 개수 M 입력
    line1 = sys.stdin.readline().split()
    if not line1:
        return
    n, m = map(int, line1)

    # profit[기업번호][투자액] 테이블 초기화 (1-indexed)
    profit = [[0] * (n + 1) for _ in range(m + 1)]

    # 투자 정보 입력 (첫 번째 컬럼은 투자 액수 k, 이후 m개의 숫자는 각 기업의 이익)
    for _ in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        k = data[0]
        for i in range(1, m + 1):
            profit[i][k] = data[i]

    # dp[i][j]: i번째 기업까지 고려하여 j원 투자 시 최대 이익
    # path[i][j]: 그때 i번째 기업에 투자한 액수
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    path = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    for i in range(1, m + 1): # 기업 순회
        for j in range(n + 1): # 총 투자액 순회
            for k in range(j + 1): # i번째 기업에 투자할 액수 k 결정
                current_profit = dp[i-1][j-k] + profit[i][k]
                if current_profit > dp[i][j]:
                    dp[i][j] = current_profit
                    path[i][j] = k

    # 최대 이익 출력
    print(dp[m][n])

    # 경로 역추적 (각 기업에 투자한 액수 찾기)
    result_investments = [0] * (m + 1)
    remaining_budget = n
    for i in range(m, 0, -1):
        invested = path[i][remaining_budget]
        result_investments[i] = invested
        remaining_budget -= invested

    # 각 기업별 투자액 출력 (공백 구분)
    print(*(result_investments[1:]))

if __name__ == "__main__":
    solve()

#######################################################################

