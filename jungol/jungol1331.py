def solve_standard():
    n = int(input())
    size = 2 * n - 1
    matrix = [[None] * size for _ in range(size)]
    
    char_code = 0
    # 반시계 방향 벡터: 하좌, 하우, 상우, 상좌
    dr = [1, 1, -1, -1]
    dc = [-1, 1, 1, -1]
    
    for s in range(n):
        r, c = s, n - 1
        length = n - 1 - s
        
        if length == 0:
            matrix[r][c] = chr(ord('A') + char_code % 26)
            char_code += 1
        else:
            for d in range(4):
                for _ in range(length):
                    matrix[r][c] = chr(ord('A') + char_code % 26)
                    char_code += 1
                    r += dr[d]
                    c += dc[d]

    # 출력 루프
    for r in range(size):
        row_str = []
        # 해당 줄의 마지막 문자가 어디인지 확인
        last_c = -1
        for c in range(size):
            if matrix[r][c]: last_c = c
            
        for c in range(last_c + 1):
            val = matrix[r][c]
            row_str.append(val if val else " ")
        print(" ".join(row_str))

solve_standard()

########################################################################

def solve_buffer():
    n = int(input())
    size = 2 * n - 1
    grid = [[""] * size for _ in range(size)]
    
    # 'A' ~ 'Z'를 무한히 생성하는 제너레이터
    def char_gen():
        curr = 0
        while True:
            yield chr(ord('A') + (curr % 26))
            curr += 1
    
    gen = char_gen()
    
    for s in range(n):
        side = n - 1 - s
        r, c = s, n - 1
        if side == 0:
            grid[r][c] = next(gen)
            continue
            
        for dr, dc in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
            for _ in range(side):
                grid[r][c] = next(gen)
                r += dr; c += dc

    for row in grid:
        # 우측 공백 제거를 위한 슬라이싱
        last_idx = 0
        for i, char in enumerate(row):
            if char: last_idx = i
        print(" ".join(char if char else " " for char in row[:last_idx+1]))

solve_buffer()

########################################################################

def solve_v1():
    try:
        n = int(input())
        if n == 1: print("A"); return
    except: return

    size = 2 * n - 1
    matrix = [[""] * size for _ in range(size)]
    char_count = 0
    # 방향: 하좌(↙), 하우(↘), 상우(↗), 상좌(↖)
    dr, dc = [1, 1, -1, -1], [-1, 1, 1, -1]

    for s in range(n):
        r, c = s, n - 1
        side = n - 1 - s
        if side == 0:
            matrix[r][c] = chr(ord('A') + (char_count % 26))
            char_count += 1
        else:
            for d in range(4):
                for _ in range(side):
                    matrix[r][c] = chr(ord('A') + (char_count % 26))
                    char_count += 1
                    r += dr[d]; c += dc[d]

    # 공통 출력 로직
    for r in range(size):
        last = -1
        for c in range(size):
            if matrix[r][c]: last = c
        if last == -1: continue
        print(" ".join(matrix[r][c] if matrix[r][c] else " " for c in range(last + 1)))

solve_v1()

########################################################################

