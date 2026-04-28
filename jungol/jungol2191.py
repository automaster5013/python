import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 문자열 a와 그 길이 n
    n = int(input_data[0])
    a = input_data[1]
    
    # 문자열 b와 그 길이 m
    m = int(input_data[2])
    b = input_data[3]

    # 1. DP 테이블 초기화 (n+1) x (m+1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 2. 초기값 설정
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # 3. DP 수행
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 두 문자가 같다면 연산 불필요
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르다면 삽입, 삭제, 치환 중 최소값 + 1
            else:
                dp[i][j] = 1 + min(dp[i-1][j],      # 삭제
                                   dp[i][j-1],      # 삽입
                                   dp[i-1][j-1])    # 치환

    # 4. 결과 출력
    print(dp[n][m])

if __name__ == "__main__":
    solve()

#################################################################



