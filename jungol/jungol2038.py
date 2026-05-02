import sys

def solve():
    # 데이터를 한 번에 읽어와 처리 속도를 높입니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # (x, |y|) 형태로 저장하고 x 좌표 기준으로 정렬
    buildings = []
    ptr = 1
    for _ in range(n):
        x = int(input_data[ptr])
        y = abs(int(input_data[ptr+1]))
        buildings.append((x, y))
        ptr += 2
    
    buildings.sort()
    
    # x와 |y|를 분리하여 지역 변수 리스트로 관리 (접근 속도 향상)
    xs = [b[0] for b in buildings]
    ys = [b[1] for b in buildings]
    
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # i번째 건물의 x좌표
        curr_x = xs[i-1]
        max_y = 0
        
        # 초기값: 직전 DP + 현재 건물 하나만 포함하는 기지국 비용
        res = dp[i-1] + (ys[i-1] * 2)
        
        # 역순으로 탐색하며 기지국 범위를 확장
        for j in range(i - 1, 0, -1):
            # y값의 최대치 갱신
            if ys[j-1] > max_y:
                max_y = ys[j-1]
            
            # 현재 기지국이 j~i번 건물을 포함할 때의 가로 거리
            dist = curr_x - xs[j-1]
            
            # [핵심 가지치기] 
            # 가로 거리 자체가 이미 현재 최솟값 res보다 크다면 
            # 더 멀리 있는 j를 확인할 필요가 없음
            if dist > res:
                break
                
            # 통신폭 = max(가로 거리, 세로 높이 제약)
            width = dist if dist > (max_y * 2) else (max_y * 2)
            
            # 최솟값 갱신
            if dp[j-1] + width < res:
                res = dp[j-1] + width
                
        dp[i] = res
        
    print(dp[n])

if __name__ == "__main__":
    solve()

######################################################################

