import sys
import math

def solve():
    # 데이터 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    points = []
    idx = 1
    for _ in range(n):
        x = float(input_data[idx])
        y = float(input_data[idx+1])
        points.append((x, y))
        idx += 2
        
    # x-좌표 순으로 정렬 (문제 조건상 x는 모두 다름)
    points.sort()
    
    # 점들 사이의 거리 미리 계산
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            
    # DP 테이블 초기화 (충분히 큰 값)
    inf = float('inf')
    dp = [[inf] * n for _ in range(n)]
    
    # 초기 상태: 1번 점(index 0)에서 시작하여 2번 점(index 1)까지 연결됨
    dp[0][1] = dist[0][1]
    
    # DP 진행
    for j in range(1, n - 1):
        for i in range(j):
            if dp[i][j] == inf:
                continue
            
            # 다음 점(j+1)을 j번에 붙이는 경우
            dp[i][j+1] = min(dp[i][j+1], dp[i][j] + dist[j][j+1])
            
            # 다음 점(j+1)을 i번에 붙이는 경우 (끝점이 바뀜)
            dp[j][j+1] = min(dp[j][j+1], dp[i][j] + dist[i][j+1])
            
    # 마지막 점(n-1)과 i번 점을 연결하여 사이클 완성
    ans = inf
    for i in range(n - 1):
        ans = min(ans, dp[i][n-1] + dist[i][n-1])
        
    # 소수점 둘째 자리까지 반올림 출력
    print("{:.2f}".format(round(ans, 2)))

if __name__ == "__main__":
    solve()

##############################################################################

