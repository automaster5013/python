import sys

def solve():
    # 1. 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])  # 동전의 종류 수
    coins = list(map(int, input_data[1:n+1]))  # 동전 단위들
    w_target = int(input_data[n+1])  # 목표 잔돈
    
    # 2. DP 테이블 초기화
    # 최대 잔돈이 64,000이므로 64,001은 도달 불가능한 큰 값을 의미함
    inf = 64001
    dp = [inf] * (w_target + 1)
    dp[0] = 0
    
    # 3. DP 수행 (무한 배낭 방식과 동일하게 정방향 순회)
    for coin in coins:
        for i in range(coin, w_target + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                
    # 4. 결과 출력
    result = dp[w_target]
    if result >= inf:
        print("impossible")
    else:
        print(result)

if __name__ == "__main__":
    solve()

##########################################################################


