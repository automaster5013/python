import sys

def solve_v1():
    # 고속 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    # 색깔별로 좌표를 담을 리스트 (N+1개 생성)
    points_by_color = [[] for _ in range(n + 1)]
    
    idx = 1
    for _ in range(n):
        x, y = int(input_data[idx]), int(input_data[idx+1])
        points_by_color[y].append(x)
        idx += 2
        
    total_dist = 0
    for color_group in points_by_color:
        if len(color_group) <= 1:
            continue
            
        # 좌표 정렬 (O(N log N))
        color_group.sort()
        
        for i in range(len(color_group)):
            if i == 0:
                # 첫 번째 점: 오른쪽과의 거리
                total_dist += color_group[1] - color_group[0]
            elif i == len(color_group) - 1:
                # 마지막 점: 왼쪽과의 거리
                total_dist += color_group[i] - color_group[i-1]
            else:
                # 중간 점: 양옆 중 최소값
                dist_left = color_group[i] - color_group[i-1]
                dist_right = color_group[i+1] - color_group[i]
                total_dist += min(dist_left, dist_right)
                
    print(total_dist)

solve_v1()

#############################################################################

import sys

def solve_v2():
    input = sys.stdin.read().split()
    n = int(input[0])
    points = []
    
    ptr = 1
    for _ in range(n):
        x, y = int(input[ptr]), int(input[ptr+1])
        points.append((y, x)) # 색깔 우선, 그다음 좌표 순으로 정렬되게 함
        ptr += 2
        
    # 색깔별로 묶이고 그 안에서 좌표순으로 정렬됨
    points.sort()
    
    total = 0
    for i in range(n):
        color, x = points[i]
        
        dist_left = float('inf')
        dist_right = float('inf')
        
        # 왼쪽 점이 존재하고 같은 색깔인지 확인
        if i > 0 and points[i-1][0] == color:
            dist_left = x - points[i-1][1]
            
        # 오른쪽 점이 존재하고 같은 색깔인지 확인
        if i < n - 1 and points[i+1][0] == color:
            dist_right = points[i+1][1] - x
            
        # 두 거리 중 최솟값 선택 (둘 다 inf면 단독 점이므로 0)
        res = min(dist_left, dist_right)
        if res != float('inf'):
            total += res
            
    print(total)

solve_v2()

#############################################################################

from collections import defaultdict
import sys

def solve_v3():
    n = int(sys.stdin.readline())
    color_map = defaultdict(list)
    
    for _ in range(n):
        x, c = map(int, sys.stdin.readline().split())
        color_map[c].append(x)
        
    ans = 0
    for coords in color_map.values():
        if len(coords) < 2: continue
        coords.sort()
        
        # 슬라이싱과 zip을 이용한 파이썬스러운 거리 계산
        ans += coords[1] - coords[0] # 첫 점
        ans += coords[-1] - coords[-2] # 끝 점
        
        # 중간 점들 처리
        for i in range(1, len(coords) - 1):
            ans += min(coords[i] - coords[i-1], coords[i+1] - coords[i])
            
    print(ans)

solve_v3()

#############################################################################

class Point:
    def __init__(self, x, color):
        self.x = x
        self.color = color

def solve_v5():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    points = [Point(int(data[i*2+1]), int(data[i*2+2])) for i in range(n)]
    
    # 색깔 기준 정렬 후 좌표 기준 정렬
    points.sort(key=lambda p: (p.color, p.x))
    
    total_sum = 0
    for i in range(n):
        d = float('inf')
        # 왼쪽 이웃 확인
        if i > 0 and points[i].color == points[i-1].color:
            d = min(d, points[i].x - points[i-1].x)
        # 오른쪽 이웃 확인
        if i < n-1 and points[i].color == points[i+1].color:
            d = min(d, points[i+1].x - points[i].x)
        
        if d != float('inf'):
            total_sum += d
            
    print(total_sum)

solve_v5()

#############################################################################

