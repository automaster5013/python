import sys

def solve():
    # 모든 입력을 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    # 1. 다각형 정점 개수 N 읽기
    try:
        n = int(input_data[ptr])
        ptr += 1
    except (IndexError, ValueError):
        return
    
    # 2. 다각형 정점 좌표 읽기
    polygon = []
    for _ in range(n):
        x = int(input_data[ptr])
        y = int(input_data[ptr+1])
        polygon.append((x, y))
        ptr += 2
    
    # 3. 판별할 점의 좌표 (px, py) 읽기
    # 정올 2395번은 Q 없이 바로 하나의 점 좌표만 주어집니다.
    if ptr + 1 >= len(input_data):
        return
    px = int(input_data[ptr])
    py = int(input_data[ptr+1])

    is_on_boundary = False
    crossings = 0
    
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        
        # [조건 1] BOUNDARY 판별
        # 점이 에지의 Bounding Box 안에 있는지 먼저 확인
        if (min(p1[0], p2[0]) <= px <= max(p1[0], p2[0]) and
            min(p1[1], p2[1]) <= py <= max(p1[1], p2[1])):
            # 외적(Cross Product)을 이용해 세 점이 일직선 위에 있는지 확인
            if (p2[0] - p1[0]) * (py - p1[1]) == (p2[1] - p1[1]) * (px - p1[0]):
                is_on_boundary = True
                break
        
        # [조건 2] Ray Casting (INTERIOR/EXTERIOR 판별)
        # 반직선이 정점을 지날 때의 중복 계산을 피하기 위해 한쪽 끝점은 포함하고 한쪽은 제외
        if ((p1[1] <= py < p2[1]) or (p2[1] <= py < p1[1])):
            # 교차점의 x좌표 계산: x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            intersect_x = p1[0] + (py - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
            if px < intersect_x:
                crossings += 1
                
    if is_on_boundary:
        print("BOUNDARY")
    elif crossings % 2 == 1:
        print("INTERIOR")
    else:
        print("EXTERIOR")

if __name__ == "__main__":
    solve()

##########################################################################################


