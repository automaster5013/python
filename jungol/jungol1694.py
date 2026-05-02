import sys

def ccw(p1, p2, p3):
    """세 점의 방향성을 판별하는 함수"""
    val = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - \
          (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])
    if val > 0: return 1
    if val < 0: return -1
    return 0

def intersect(s1, s2):
    """두 선분이 교차하는지 판별하는 함수 (끝점 포함)"""
    p1, p2 = s1; p3, p4 = s2
    res1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    res2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    return res1 <= 0 and res2 <= 0

def get_intersection_point(s1, s2):
    """두 직선의 교점 좌표를 계산하는 함수"""
    (x1, y1), (x2, y2) = s1
    (x3, y3), (x4, y4) = s2
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0: return None # 평행한 경우
    
    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    return px, py

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N = int(input_data[0])
    lines = []
    ptr = 1
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input_data[ptr:ptr+4])
        lines.append(((x1, y1), (x2, y2)))
        ptr += 4
    
    # 정사각형의 네 변 (경계선)
    square_edges = [
        ((-10, 10), (10, 10)),   # Top
        ((10, 10), (10, -10)),   # Right
        ((10, -10), (-10, -10)), # Bottom
        ((-10, -10), (-10, 10))  # Left
    ]
    
    # 1. 정사각형을 실제로 통과하는 선분만 필터링
    valid_lines = []
    for line in lines:
        passes = False
        for edge in square_edges:
            if intersect(line, edge):
                # 선분이 경계를 지나는지 확인 (내부를 지나는지 엄밀히 체크)
                p = get_intersection_point(line, edge)
                if p:
                    px, py = p
                    # 교점이 정사각형 경계(모서리 포함)에 있는지 확인
                    if -10 <= px <= 10 and -10 <= py <= 10:
                        passes = True
                        break
        if passes:
            valid_lines.append(line)
            
    # 2. 영역 수 계산: 1 + 선분 수 + 내부 교점 수
    num_regions = 1 + len(valid_lines)
    
    num_valid = len(valid_lines)
    for i in range(num_valid):
        for j in range(i + 1, num_valid):
            if intersect(valid_lines[i], valid_lines[j]):
                p = get_intersection_point(valid_lines[i], valid_lines[j])
                if p:
                    px, py = p
                    # 교점이 정사각형 '내부'에 있는지 확인
                    if -10 < px < 10 and -10 < py < 10:
                        num_regions += 1
                        
    print(num_regions)

if __name__ == "__main__":
    solve()

############################################################################

