import sys

def solve():
    # 데이터 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr]); ptr += 1 # 벽장의 개수
    o1 = int(input_data[ptr]); ptr += 1 # 초기 열린 벽장 1
    o2 = int(input_data[ptr]); ptr += 1 # 초기 열린 벽장 2
    m = int(input_data[ptr]); ptr += 1 # 사용할 벽장 순서의 길이
    
    # 사용할 벽장 리스트
    targets = [int(input_data[i]) for i in range(ptr, ptr + m)]
    
    INF = float('inf')
    # dp[x] : 한 문은 '직전 목표물'에 있고, 나머지 한 문은 x에 있을 때의 최소 이동 횟수
    dp = [INF] * (n + 1)
    
    # 첫 번째 목표 처리
    first_target = targets[0]
    dp[o2] = abs(first_target - o1)
    dp[o1] = abs(first_target - o2)
    
    prev_target = first_target
    
    # 두 번째 목표부터 순차적으로 처리
    for i in range(1, m):
        curr_target = targets[i]
        next_dp = [INF] * (n + 1)
        
        for x in range(1, n + 1):
            if dp[x] == INF:
                continue
            
            # 1. '직전 목표(prev_target)'에 있던 문을 '현재 목표(curr_target)'로 이동
            if next_dp[x] > dp[x] + abs(curr_target - prev_target):
                next_dp[x] = dp[x] + abs(curr_target - prev_target)
            
            # 2. '다른 위치(x)'에 있던 문을 '현재 목표(curr_target)'로 이동
            # 이 경우 나머지 한 문은 '직전 목표(prev_target)' 위치에 있게 됨
            if next_dp[prev_target] > dp[x] + abs(curr_target - x):
                next_dp[prev_target] = dp[x] + abs(curr_target - x)
        
        dp = next_dp
        prev_target = curr_target

    # 모든 요청을 처리한 후의 최솟값 출력
    print(min(dp))

if __name__ == "__main__":
    solve()

####################################################################################

