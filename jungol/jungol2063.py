import sys

def solve():
    # 데이터 입력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    points = sorted([int(x) for x in input_data[1:n+1]])
    truck_cost = int(input_data[n+1])
    heli_cost = int(input_data[n+2])
    
    # 누적 합 전처리 (1-based indexing)
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i-1] + points[i-1]
        
    # dp[i]: i번째 물품까지 배송하는 최소 비용
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # 1. 기본값: i번째 물품을 본점에서 트럭으로 개별 배송
        dp[i] = dp[i-1] + points[i-1] * truck_cost
        
        # 2. j~i번째 물품을 헬리콥터 1대로 묶어서 배송하는 경우 탐색
        for j in range(1, i + 1):
            # 중앙값의 인덱스 (1-based 기준)
            m = (j + i) // 2
            p_m = points[m-1]
            
            # 구간 내 중앙값과의 거리 합 계산
            dist_sum = (s[i] - s[m] - s[m-1] + s[j-1]) + (2*m - i - j) * p_m
            
            # 현재까지의 최소 비용 갱신
            current_total = dp[j-1] + heli_cost + dist_sum * truck_cost
            if current_total < dp[i]:
                dp[i] = current_total
                
    print(dp[n])

if __name__ == "__main__":
    solve()

################################################################################

