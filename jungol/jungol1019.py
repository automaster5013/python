import sys

def solve():
    # 데이터 읽기 (빠른 입력을 위해 split 사용)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 객차의 수
    passengers = [0] + list(map(int, input_data[1:n+1])) # 각 객차의 손님 수
    m = int(input_data[n+1]) # 소형 기관차가 끌 수 있는 최대 객차 수
    
    # 1. 누적 합 계산
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i-1] + passengers[i]
        
    # 2. DP 테이블 초기화 (4행 N+1열)
    # dp[k][i]는 k대의 기관차로 i번 객차까지 고려했을 때의 최대 손님 수
    dp = [[0] * (n + 1) for _ in range(4)]
    
    # 3. DP 수행
    for k in range(1, 4): # 소형 기관차 3대 배치
        for i in range(m * k, n + 1):
            # 현재 구간(M개)을 선택하는 경우 vs 선택하지 않는 경우
            current_window_sum = s[i] - s[i-m]
            dp[k][i] = max(dp[k][i-1], dp[k-1][i-m] + current_window_sum)
            
    # 최대로 운송할 수 있는 손님 수 출력
    print(dp[3][n])

if __name__ == "__main__":
    solve()

#########################################################################################

