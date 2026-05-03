import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])  # 그림의 개수
    s = int(input_data[1])  # 판매 가능 기준 높이
    
    pics = []
    idx = 2
    for _ in range(n):
        h = int(input_data[idx])
        c = int(input_data[idx+1])
        pics.append((h, c))
        idx += 2
        
    # 1. 높이(H) 기준으로 오름차순 정렬
    pics.sort()
    
    # 2. DP 및 투 포인터 최적화
    dp = [0] * n
    max_prev_dp = 0
    left = 0
    
    for right in range(n):
        # 현재 그림(right)과 높이 차이가 S 이상인 이전 그림들 중 최댓값을 갱신
        while left < right and pics[left][0] <= pics[right][0] - s:
            if dp[left] > max_prev_dp:
                max_prev_dp = dp[left]
            left += 1
        
        # 현재 그림의 가격 + 조건을 만족하는 이전 최댓값
        dp[right] = pics[right][1] + max_prev_dp
        
    # 3. 모든 경우 중 최대 합 출력
    print(max(dp))

if __name__ == "__main__":
    solve()

####################################################################################


