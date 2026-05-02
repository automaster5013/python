import sys

def solve():
    # 1. 입력 데이터 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    # N x N 배열 생성
    board = []
    for _ in range(n):
        board.append([int(next(it)) for _ in range(n)])

    # 2. DP 테이블 초기화
    # dp[i][j]는 (i, j)에 도달했을 때의 최대 점수
    dp = [[0] * n for _ in range(n)]

    # 3. 첫 번째 행 초기화 (왼쪽에서 오른쪽으로만 이동 가능)
    dp[0][0] = board[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + board[0][j]

    # 4. 두 번째 행부터 N번째 행까지 DP 진행
    for i in range(1, n):
        # 왼쪽에서 오른쪽으로 가는 경우 (L)
        left_to_right = [0] * n
        left_to_right[0] = dp[i-1][0] + board[i][0]
        for j in range(1, n):
            left_to_right[j] = max(dp[i-1][j], left_to_right[j-1]) + board[i][j]
            
        # 오른쪽에서 왼쪽으로 가는 경우 (R)
        right_to_left = [0] * n
        right_to_left[n-1] = dp[i-1][n-1] + board[i][n-1]
        for j in range(n-2, -1, -1):
            right_to_left[j] = max(dp[i-1][j], right_to_left[j+1]) + board[i][j]
            
        # 두 경우 중 최댓값을 dp 테이블에 기록
        for j in range(n):
            dp[i][j] = max(left_to_right[j], right_to_left[j])

    # 5. 최종 목적지 A[N][N] 결과 출력
    print(dp[n-1][n-1])

if __name__ == "__main__":
    solve()

####################################################################################

