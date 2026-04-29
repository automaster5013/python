import sys

def solve():
    # 1. 입력 처리
    s = sys.stdin.readline().strip()
    if not s:
        return
    
    n = len(s)
    # dp[i]: i번째 문자까지 확인했을 때 가능한 배열의 수
    dp = [0] * (n + 1)
    
    # 2. 초기값 설정 (Base Case)
    dp[0] = 1
    
    # 첫 번째 문자가 '0'이면 어떤 카드도 만들 수 없음
    if s[0] == '0':
        print(0)
        return
    
    dp[1] = 1
    
    # 3. DP 진행
    for i in range(2, n + 1):
        # 한 자리 수 체크 (s[i-1])
        one_digit = int(s[i-1])
        if 1 <= one_digit <= 9:
            dp[i] += dp[i-1]
            
        # 두 자리 수 체크 (s[i-2:i])
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 34:
            dp[i] += dp[i-2]
            
    # 4. 결과 출력
    print(dp[n])

if __name__ == "__main__":
    solve()

###########################################################

