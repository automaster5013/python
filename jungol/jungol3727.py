import sys
import math

def solve():
    # 입력을 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    if N <= 2:
        print(N)
        return
    
    points = []
    ptr = 1
    for _ in range(N):
        x = int(input_data[ptr])
        y = int(input_data[ptr+1])
        points.append((x, y))
        ptr += 2
        
    max_pts = 0
    
    # 각 점을 기준으로 다른 점들과의 기울기를 확인합니다.
    for i in range(N):
        slopes = {}
        curr_max = 0
        x1, y1 = points[i]
        
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            
            # 최대공약수로 나누어 기울기를 정규화 (기약 분수 형태)
            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
            
            # 방향 일관성 유지 (dx가 음수거나, 수직선에서 dy가 음수인 경우 처리)
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            
            slope = (dx, dy)
            slopes[slope] = slopes.get(slope, 0) + 1
            if slopes[slope] > curr_max:
                curr_max = slopes[slope]
        
        # 현재 점 i를 포함해야 하므로 +1
        if curr_max + 1 > max_pts:
            max_pts = curr_max + 1
            
    print(max_pts)

if __name__ == "__main__":
    solve()

################################################################################

