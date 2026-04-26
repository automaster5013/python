def solve_v1():
    k = int(input())
    sides = []
    for _ in range(6):
        # 방향은 무시하고 길이만 사용해도 무방 (인덱스로 판별 가능)
        dir, length = map(int, input().split())
        sides.append(length)

    max_w = 0
    max_h = 0
    w_idx = 0
    h_idx = 0

    # 가로(1,2)와 세로(3,4) 중 최대값과 그 인덱스를 찾음
    # 여기서는 입력 순서에 따라 짝수/홀수 인덱스가 가로/세로로 나뉨
    for i in range(6):
        if i % 2 == 0:
            if max_w < sides[i]:
                max_w = sides[i]
                w_idx = i
        else:
            if max_h < sides[i]:
                max_h = sides[i]
                h_idx = i

    # 작은 사각형의 가로세로는 최대 가로/세로 인덱스에서 3칸 떨어진 곳
    small_w = abs(sides[(w_idx + 5) % 6] - sides[(w_idx + 1) % 6])
    small_h = abs(sides[(h_idx + 5) % 6] - sides[(h_idx + 1) % 6])
    
    # 또는 더 간단하게:
    sub_w = sides[(w_idx + 3) % 6]
    sub_h = sides[(h_idx + 3) % 6]

    area = (max_w * max_h) - (sub_w * sub_h)
    print(area * k)

solve_v1()

##########################################################################

def solve_v2():
    k = int(input())
    info = [list(map(int, input().split())) for _ in range(6)]
    
    # 방향 정보를 확장하여 패턴 탐색을 용이하게 함 (원형 리스트 대응)
    dirs = [info[i][0] for i in range(6)] * 2
    
    max_w = max(info[i][1] for i in range(6) if info[i][0] in [1, 2])
    max_h = max(info[i][1] for i in range(6) if info[i][0] in [3, 4])
    
    sub_w, sub_h = 0, 0
    for i in range(len(dirs) - 3):
        # 방향이 A B A B 형태로 반복되는 구간 찾기
        if dirs[i] == dirs[i+2] and dirs[i+1] == dirs[i+3]:
            sub_w = info[(i+1)%6][1]
            sub_h = info[(i+2)%6][1]
            break
            
    print(((max_w * max_h) - (sub_w * sub_h)) * k)

solve_v2()

##########################################################################

def solve_v3():
    k = int(input())
    x, y = 0, 0
    points = [(0, 0)]
    
    # 동(1), 서(2), 남(3), 북(4)
    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    
    for _ in range(6):
        d, l = map(int, input().split())
        x += dx[d] * l
        y += dy[d] * l
        points.append((x, y))
        
    # 신발끈 공식 (Shoelace Formula)
    area = 0
    for i in range(6):
        area += (points[i][0] * points[i+1][1])
        area -= (points[i+1][0] * points[i][1])
        
    print(abs(area) // 2 * k)

solve_v3()

##########################################################################

def solve_v4():
    k = int(input())
    s = [list(map(int, input().split())) for _ in range(6)]
    
    max_w = max(x[1] for x in s if x[0] in [1, 2])
    max_h = max(x[1] for x in s if x[0] in [3, 4])
    
    sub_area = 1
    for i in range(6):
        # 현재 변의 양옆 두 변의 합이 최대 변의 길이와 같은지 체크
        # 예: 가로 변 양옆의 세로 변 두 개를 더해서 max_h가 나오면, 그 가로 변은 파여진 부분임
        side_before = s[(i-1)%6][1]
        side_after = s[(i+1)%6][1]
        
        target_max = max_h if s[i][0] in [1, 2] else max_w
        
        if side_before + side_after == target_max:
            sub_area *= s[i][1]
            
    print(((max_w * max_h) - sub_area) * k)

solve_v4()

##########################################################################

def solve_v5():
    k = int(input())
    moves = []
    dir_count = {1:0, 2:0, 3:0, 4:0}
    
    for _ in range(6):
        d, l = map(int, input().split())
        moves.append((d, l))
        dir_count[d] += 1
        
    big_sides = []
    small_sides = []
    
    for i in range(6):
        # 해당 방향이 1번만 나타났다면 큰 사각형의 변임
        if dir_count[moves[i][0]] == 1:
            big_sides.append(moves[i][1])
        else:
            # 방향이 2번 나타난 변들 중, 양옆에 큰 변이 없는 경우가 작은 사각형의 변
            if dir_count[moves[(i-1)%6][0]] == 2 and dir_count[moves[(i+1)%6][0]] == 2:
                small_sides.append(moves[i][1])
                
    print(((big_sides[0] * big_sides[1]) - (small_sides[0] * small_sides[1])) * k)

solve_v5()

##########################################################################


