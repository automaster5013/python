import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 인덱스를 편하게 맞추기 위해 앞에 0을 추가 (1번 계단부터 시작)
    stairs = [0] + [int(x) for x in input_data[1:]]
    
    # 계단이 1개 또는 2개인 경우 예외 처리
    if n == 1:
        print(stairs[1])
        return
    if n == 2:
        print(stairs[1] + stairs[2])
        return

    # 2. DP 테이블 초기화
    dp = [0] * (n + 1)
    
    # 3. 초기값 설정
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    
    # 4. 점화식을 이용한 반복문 진행
    for i in range(4, n + 1):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
        
    # 5. 결과 출력
    print(dp[n])

if __name__ == "__main__":
    solve()

###################################################################################

