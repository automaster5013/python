import sys
from bisect import bisect_right

def solve():
    # 데이터 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    intervals = []
    ptr = 1
    for _ in range(N):
        l = int(input_data[ptr])
        r = int(input_data[ptr+1])
        intervals.append((l, r))
        ptr += 2
        
    # 1. 오른쪽 끝점(R) 기준 정렬
    intervals.sort(key=lambda x: x[1])
    
    # 2. DP 테이블 및 오른쪽 끝점 리스트 초기화
    MOD = 20070713
    dp = [0] * (N + 1)
    dp[0] = 1  # 공집합 (기저 사례)
    
    r_endpoints = [x[1] for x in intervals]
    
    # 3. DP 진행
    for i in range(1, N + 1):
        curr_l = intervals[i-1][0]
        
        # 4. 이진 탐색으로 현재 로봇과 겹치지 않는 최대 인덱스 j 찾기
        # R_j < curr_l 을 만족하는 가장 큰 j를 찾습니다.
        j = bisect_right(r_endpoints, curr_l - 1)
        
        # 점화식: (포함하지 않는 경우) + (포함하는 경우)
        dp[i] = (dp[i-1] + dp[j]) % MOD
        
    # 최종 결과 출력
    print(dp[N])

if __name__ == "__main__":
    solve()

######################################################################


