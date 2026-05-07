import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

def solve():
    getcontext().prec = 50
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N = int(input_data[0])
    pts = []
    idx = 1
    for _ in range(N):
        pts.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
        
    # 다각형의 변 리스트화
    edges = []
    for i in range(N):
        edges.append((pts[i], pts[(i+1)%N]))
        
    # 다각형 내부 판별 함수 (Ray Casting from point to +x direction)
    def is_inside(px, py):
        count = 0
        for (x1, y1), (x2, y2) in edges:
            if min(y1, y2) <= py < max(y1, y2):
                intersect_x = x1 + (px - x1) * (y2 - y1) # dummy, actually we need below
                if y1 != y2:
                    ix = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
                    if px < ix:
                        count += 1
        return count % 2 == 1

    # 다각형 면적 구하는 함수 (Shoelace Formula)
    def polygon_area(poly):
        area = 0
        sz = len(poly)
        for i in range(sz):
            x1, y1 = poly[i]
            x2, y2 = poly[(i+1)%sz]
            area += (x1 * y2 - x2 * y1)
        return abs(area) / 2.0

    max_eff = 0.0
    
    # 각 꼭짓점(안쪽으로 꺾인 곳)에서 4방향으로 둑 생성 시도
    for i in range(N):
        # Reflex Vertex (오목한 꼭짓점) 필터링은 생략하고 모든 점에서 쏜다
        # 4방향 쏘기 (+x, -x, +y, -y)
        cx, cy = pts[i]
        
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            closest_dist = float('inf')
            hit_point = None
            hit_edge_idx = -1
            
            for j, ((x1, y1), (x2, y2)) in enumerate(edges):
                # 인접한 변은 패스
                if i == j or i == (j+1)%N: continue
                
                if dx != 0: # 수평 방향 쏘기
                    if y1 <= cy <= y2 or y2 <= cy <= y1:
                        if y1 != y2:
                            # 변이 수직선일 때만 유효하게 만남 (섬은 수직/수평변만 있음)
                            if x1 == x2:
                                if (dx > 0 and x1 > cx) or (dx < 0 and x1 < cx):
                                    dist = abs(x1 - cx)
                                    if dist < closest_dist:
                                        closest_dist = dist
                                        hit_point = (x1, cy)
                                        hit_edge_idx = j
                else: # 수직 방향 쏘기
                    if x1 <= cx <= x2 or x2 <= cx <= x1:
                        if x1 != x2:
                            # 변이 수평선일 때만 유효하게 만남
                            if y1 == y2:
                                if (dy > 0 and y1 > cy) or (dy < 0 and y1 < cy):
                                    dist = abs(y1 - cy)
                                    if dist < closest_dist:
                                        closest_dist = dist
                                        hit_point = (cx, y1)
                                        hit_edge_idx = j
                                        
            if hit_point and hit_edge_idx != -1:
                mid_x = (cx + hit_point[0]) / 2.0
                mid_y = (cy + hit_point[1]) / 2.0
                
                # 둑의 중점이 바다(다각형 외부)에 있어야 함 (간척지 만들기)
                if not is_inside(mid_x, mid_y):
                    # 둑을 이으면 다각형이 2개로 쪼개짐
                    # 쪼개진 폴리곤 1
                    poly1 = [pts[i]]
                    curr = (i + 1) % N
                    while curr != (hit_edge_idx + 1) % N:
                        poly1.append(pts[curr])
                        curr = (curr + 1) % N
                    poly1.append(hit_point)
                    
                    # 쪼개진 폴리곤 2
                    poly2 = [hit_point]
                    curr = (hit_edge_idx + 1) % N
                    while curr != i:
                        poly2.append(pts[curr])
                        curr = (curr + 1) % N
                    poly2.append(pts[i])
                    
                    area1 = polygon_area(poly1)
                    area2 = polygon_area(poly2)
                    
                    # 간척지 넓이는 쪼개진 두 넓이 중 작은 쪽 (큰 쪽은 나머지 바다/육지)
                    reclaimed_area = min(area1, area2)
                    if reclaimed_area > 0:
                        eff = reclaimed_area / closest_dist
                        if eff > max_eff:
                            max_eff = eff

    # 파이썬 decimal을 이용한 정확한 반올림 (소수 둘째 자리)
    ans = Decimal(str(max_eff)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(ans)

if __name__ == '__main__':
    solve()

##########################################################################################


