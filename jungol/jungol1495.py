def solve_v1():
    try:
        n = int(input())
        if n < 1: return
    except: return

    matrix = [[0] * n for _ in range(n)]
    num = 1
    
    # 대각선의 합 s = r + c (0부터 2n-2까지)
    for s in range(2 * n - 1):
        # 해당 대각선에서 r이 가질 수 있는 최소/최대 범위
        r_min = max(0, s - (n - 1))
        r_max = min(s, n - 1)
        
        if s % 2 == 0:
            # 짝수: 아래로 (r이 작은 것에서 큰 것으로)
            for r in range(r_min, r_max + 1):
                matrix[r][s - r] = num
                num += 1
        else:
            # 홀수: 위로 (r이 큰 것에서 작은 것으로)
            for r in range(r_max, r_min - 1, -1):
                matrix[r][s - r] = num
                num += 1

    for row in matrix:
        print(*(row))

solve_v1()

####################################################################

def solve_v2():
    try:
        n = int(input())
        if n == 1: print(1); return
    except: return
    
    matrix = [[0] * n for _ in range(n)]
    r, c, num = 0, 0, 1
    
    for _ in range(n * n):
        matrix[r][c] = num
        num += 1
        
        if (r + c) % 2 == 0: # 아래 대각선 방향
            if r == n - 1: c += 1 # 아래 벽이면 오른쪽으로
            elif c == 0: r += 1    # 왼쪽 벽이면 아래로 (이 순서가 중요)
            else: r += 1; c -= 1
        else: # 위 대각선 방향
            if c == n - 1: r += 1 # 오른쪽 벽이면 아래로
            elif r == 0: c += 1    # 위쪽 벽이면 오른쪽으로
            else: r -= 1; c += 1

    for row in matrix:
        print(*(row))

solve_v2()

####################################################################

def solve_v3():
    try:
        line = input()
        if not line: return
        n = int(line)
        
        coords = []
        for r in range(n):
            for c in range(n):
                coords.append((r, c))
        
        # 정렬 기준: 1. 합(r+c) 순서, 2. 합이 짝수면 r 오름차순, 홀수면 r 내림차순
        coords.sort(key=lambda x: (x[0]+x[1], x[0] if (x[0]+x[1]) % 2 == 0 else -x[0]))
        
        matrix = [[0] * n for _ in range(n)]
        for i, (r, c) in enumerate(coords, 1):
            matrix[r][c] = i
            
        for row in matrix:
            print(*(row))
    except: return

solve_v3()

####################################################################

def solve_v4():
    try:
        n = int(input())
        res = [[0] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                s = r + c
                # s번째 대각선 이전까지의 숫자 합
                if s < n:
                    before = s * (s + 1) // 2
                else:
                    before = n * n - (2 * n - 1 - s) * (2 * n - s) // 2
                
                # 현재 대각선 내에서의 순서(offset)
                r_min = max(0, s - n + 1)
                r_max = min(s, n - 1)
                if s % 2 == 0: offset = r - r_min + 1
                else: offset = r_max - r + 1
                
                res[r][c] = before + offset

        for row in res:
            print(*(row))
    except: return

solve_v4()

####################################################################

def diagonal_path(n):
    for s in range(2 * n - 1):
        r_min, r_max = max(0, s - n + 1), min(s, n - 1)
        if s % 2 == 0:
            for r in range(r_min, r_max + 1): yield (r, s - r)
        else:
            for r in range(r_max, r_min - 1, -1): yield (r, s - r)

def solve_v5():
    try:
        n = int(input())
        matrix = [[0] * n for _ in range(n)]
        
        for num, (r, c) in enumerate(diagonal_path(n), 1):
            matrix[r][c] = num
            
        for row in matrix:
            print(*(row))
    except: return

solve_v5()

####################################################################

