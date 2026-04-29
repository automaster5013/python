import sys

def solve():
    # 입력 처리 (두 줄의 문자열)
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return
    
    str1 = lines[0].strip()
    str2 = lines[1].strip()
    
    n = len(str1)
    m = len(str2)
    
    # 1. DP 테이블 초기화 (인덱스 에러 방지를 위해 (n+1) x (m+1) 크기)
    # 초기값은 모두 0으로 설정
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 2. DP 수행
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 두 문자가 같다면 대각선 왼쪽 위 값 + 1
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # 두 문자가 다르다면 위쪽과 왼쪽 값 중 큰 값 선택
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    # 3. 결과 출력 (테이블의 가장 오른쪽 아래 값)
    print(dp[n][m])

if __name__ == "__main__":
    solve()

########################################################################
