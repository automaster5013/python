import sys

def solve():
    # 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    left = list(map(int, input_data[1:n+1]))
    right = list(map(int, input_data[n+1:2*n+1]))

    # dp[i][j]는 왼쪽 i번째, 오른쪽 j번째 카드부터 시작했을 때의 최대 점수
    # 계산의 편의를 위해 (n+1)x(n+1) 크기로 설정
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 뒤에서부터 거꾸로 채워나가는 Bottom-up 방식
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # 규칙 (2): 오른쪽 카드가 왼쪽보다 작은 경우 (득점 찬스!)
            if right[j] < left[i]:
                # 오른쪽만 버리고 점수를 챙기는 것이 항상 이득
                dp[i][j] = dp[i][j+1] + right[j]
            else:
                # 규칙 (1): 왼쪽만 버리거나 둘 다 버리는 것 중 큰 값 선택
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])

    print(dp[0][0])

if __name__ == "__main__":
    solve()

#############################################################################

