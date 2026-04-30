import sys

def solve():
    # 1. 입력 처리
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)
    
    # 2. 예외 처리 (n이 1, 2일 때)
    if n <= 2:
        print(1)
        return

    # 3. DP 테이블(Tabulation) 구축
    # n이 100,000이므로 배열을 사용하여 결과값을 저장합니다.
    # 메모리를 더 아끼고 싶다면 변수 2개(a, b)만 사용할 수도 있습니다.
    dp = [0] * (n + 1)
    mod = 1000000007
    
    # 4. 초기값 설정 (Base Cases)
    dp[1] = 1
    dp[2] = 1
    
    # 5. 상향식(Bottom-up) 반복문 진행
    # 작은 문제(1, 2)부터 차례대로 큰 문제(n)로 나아갑니다.
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
        
    # 6. 결과 출력
    print(dp[n])

if __name__ == "__main__":
    solve()

#########################################################################

