def solve_v1():
    try:
        n = int(input())
        if n % 2 == 0: return # 홀수 조건
    except: return

    # n x n 매트릭스 0으로 초기화
    magic = [[0] * n for _ in range(n)]
    
    # 시작 위치: 첫 번째 행 가운데
    r, c = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic[r][c] = num
        
        # 1. n의 배수이면 바로 아래행으로 이동
        if num % n == 0:
            r += 1
        # 2. 그렇지 않으면 왼쪽 위로 이동
        else:
            r -= 1
            c -= 1
            # 행이 범위를 벗어나면 마지막 행으로
            if r < 0: r = n - 1
            # 열이 범위를 벗어나면 마지막 열로
            if c < 0: c = n - 1
            
    # 출력
    for row in magic:
        print(*(row))

solve_v1()

###########################################################################

def solve_v2():
    n = int(input())
    magic = [[0] * n for _ in range(n)]
    r, c = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic[r][c] = num
        # n의 배수 여부에 따른 좌표 이동
        if num % n == 0:
            r = (r + 1) % n
        else:
            r = (r - 1) % n
            c = (c - 1) % n
            
    for row in magic:
        print(" ".join(map(str, row)))

solve_v2()

###########################################################################

def solve_v3():
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    
    curr_r, curr_c = 0, n // 2
    
    for i in range(1, n * n + 1):
        grid[curr_r][curr_c] = i
        
        # 방향 결정
        dr, dc = (1, 0) if i % n == 0 else (-1, -1)
        
        # 좌표 업데이트 및 순환 처리
        curr_r = (curr_r + dr) % n
        curr_c = (curr_c + dc) % n
        
    for line in grid:
        print(*(line))

solve_v3()

###########################################################################

def solve_v4():
    n = int(input())
    # 각 숫자의 (r, c) 좌표를 저장할 리스트
    pos_list = []
    
    r, c = 0, n // 2
    for i in range(1, n * n + 1):
        pos_list.append((r, c))
        if i % n == 0:
            r = (r + 1) % n
        else:
            r = (r - 1) % n
            c = (c - 1) % n
            
    # 좌표 정보를 바탕으로 매트릭스 완성
    res = [[0] * n for _ in range(n)]
    for num, (tr, tc) in enumerate(pos_list, 1):
        res[tr][tc] = num
        
    for row in res:
        print(*(row))

solve_v4()

###########################################################################

def solve_v5():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]
    
    r, c = 0, n // 2
    num = 1
    
    while num <= n * n:
        matrix[r][c] = num
        
        if num % n == 0:
            # 배수일 때: 아래로
            r = (r + 1) % n
        else:
            # 아닐 때: 왼쪽 위로
            r = (r - 1) % n
            c = (c - 1) % n
            
        num += 1
        
    for row in matrix:
        print(*(row))

solve_v5()

###########################################################################


