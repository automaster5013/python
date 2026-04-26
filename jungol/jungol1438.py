def solve_v1():
    try:
        n = int(input())
        # 100x100 도화지 생성 (0으로 초기화)
        canvas = [[0] * 100 for _ in range(100)]
        
        for _ in range(n):
            x, y = map(int, input().split())
            # 색종이의 가로세로 10칸씩 1로 표시
            for i in range(x, x + 10):
                for j in range(y, y + 10):
                    canvas[i][j] = 1
        
        # 100x100 전체를 돌며 1의 개수 합산
        total_area = sum(sum(row) for row in canvas)
        print(total_area)
    except: pass

solve_v1()

#############################################################

def solve_v2():
    try:
        n = int(input())
        black_squares = set()
        
        for _ in range(n):
            x, y = map(int, input().split())
            for i in range(x, x + 10):
                for j in range(y, y + 10):
                    # (i, j) 좌표를 튜플로 저장하여 중복 자동 제거
                    black_squares.add((i, j))
        
        print(len(black_squares))
    except: pass

solve_v2()

#############################################################

def solve_v3():
    try:
        n = int(input())
        # 10,000칸의 1차원 리스트
        canvas = [0] * 10000
        
        for _ in range(n):
            x, y = map(int, input().split())
            for i in range(x, x + 10):
                for j in range(y, y + 10):
                    # 2차원 좌표를 1차원으로 매핑
                    canvas[i * 100 + j] = 1
        
        print(sum(canvas))
    except: pass

solve_v3()

#############################################################

def solve_v4():
    try:
        n = int(input())
        # 각 행마다 100비트 정수를 0으로 초기화 (총 100행)
        rows = [0] * 100
        
        for _ in range(n):
            x, y = map(int, input().split())
            # 10칸을 채우는 비트 마스크 생성 (예: 1111111111)
            # x 위치에 맞게 시프트
            mask = ((1 << 10) - 1) << x
            
            # y부터 y+9행까지 마스크 적용
            for i in range(y, y + 10):
                rows[i] |= mask
                
        # 각 행에서 1로 켜진 비트의 개수를 모두 합산
        total_area = sum(bin(row).count('1') for row in rows)
        print(total_area)
    except: pass

solve_v4()

#############################################################

def solve_v5():
    try:
        n = int(input())
        # 불리언 배열 생성
        is_black = [[False] * 100 for _ in range(100)]
        
        for _ in range(n):
            start_x, start_y = map(int, input().split())
            for r in range(start_x, start_x + 10):
                # 슬라이싱과 대입을 통한 최적화
                is_black[r][start_y : start_y + 10] = [True] * 10
        
        # True인 칸만 필터링하여 합계 계산
        count = sum(row.count(True) for row in is_black)
        print(count)
    except: pass

solve_v5()

#############################################################

