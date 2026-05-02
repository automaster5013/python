import sys

def ccw(p1, p2, p3):
    """세 점의 방향성을 판별 (양수: 좌회전, 음수: 우회전, 0: 일직선)"""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    points = []
    for i in range(n):
        points.append((int(input_data[2*i + 1]), int(input_data[2*i + 2])))
    
    # 1. 점 정렬 (x좌표 순, x가 같으면 y좌표 순)
    points.sort()
    
    # 2. Monotone Chain으로 볼록 껍질 구축
    # 하단 껍질 구축
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
        
    # 상단 껍질 구축
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
        
    # 마지막 점들은 중복되므로 제거하고 합침
    hull = lower[:-1] + upper[:-1]
    
    # 3. 신발끈 공식으로 면적 계산
    area_sum = 0
    m = len(hull)
    for i in range(m):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % m]
        area_sum += (x1 * y2) - (x2 * y1)
        
    area = abs(area_sum) / 2.0
    
    # 4. 출력 형식 맞추기 (20.0 -> 20, 27.5 -> 27.5)
    if area == int(area):
        print(int(area))
    else:
        print(f"{area:.1f}")

if __name__ == "__main__":
    solve()

#######################################################################

