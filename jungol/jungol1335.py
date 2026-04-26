import sys

def solve_v1():
    # 모든 데이터를 한 번에 읽어와 토큰화
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N = int(input_data[0])
    # 2차원 배열로 변환
    board = []
    for i in range(N):
        board.append(list(map(int, input_data[1 + i*N : 1 + (i+1)*N])))

    white = 0 # 0
    blue = 0  # 1

    def divide_conquer(r, c, n):
        nonlocal white, blue
        color = board[r][c]
        
        # 현재 영역이 모두 같은 색인지 확인
        for i in range(r, r + n):
            for j in range(c, c + n):
                if board[i][j] != color:
                    # 색이 다르면 4등분 재귀 호출
                    m = n // 2
                    divide_conquer(r, c, m)             # I (왼쪽 위)
                    divide_conquer(r, c + m, m)         # II (오른쪽 위)
                    divide_conquer(r + m, c, m)         # III (왼쪽 아래)
                    divide_conquer(r + m, c + m, m)     # IV (오른쪽 아래)
                    return

        # 모두 같은 색인 경우
        if color == 0: white += 1
        else: blue += 1

    divide_conquer(0, 0, N)
    print(white)
    print(blue)

if __name__ == "__main__":
    solve_v1()

#############################################################################

def solve_v2():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    grid = [list(map(int, data[1+i*n : 1+(i+1)*n])) for i in range(n)]
    
    res = [0, 0] # res[0]: 하얀색, res[1]: 파란색

    def check(r, c, size):
        # 해당 영역의 모든 값의 합을 구함
        total = 0
        for i in range(r, r + size):
            total += sum(grid[i][c:c+size])
            
        # 합이 0이면 모두 하얀색, 합이 size^2이면 모두 파란색
        if total == 0:
            res[0] += 1
        elif total == size * size:
            res[1] += 1
        else:
            # 섞여 있으면 분할
            m = size // 2
            for dr, dc in [(0, 0), (0, m), (m, 0), (m, m)]:
                check(r + dr, c + dc, m)

    check(0, 0, n)
    print(f"{res[0]}\n{res[1]}")

solve_v2()

#############################################################################

class PaperCutter:
    def __init__(self, n, matrix):
        self.matrix = matrix
        self.counts = {0: 0, 1: 0}

    def cut(self, r, c, size):
        first_color = self.matrix[r][c]
        is_uniform = True
        
        for i in range(r, r + size):
            for j in range(c, c + size):
                if self.matrix[i][j] != first_color:
                    is_uniform = False
                    break
            if not is_uniform: break
            
        if is_uniform:
            self.counts[first_color] += 1
        else:
            m = size // 2
            self.cut(r, c, m)
            self.cut(r, c + m, m)
            self.cut(r + m, c, m)
            self.cut(r + m, c + m, m)

def solve_v3():
    import sys
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    mat = [[int(next(it)) for _ in range(n)] for _ in range(n)]
    
    cutter = PaperCutter(n, mat)
    cutter.cut(0, 0, n)
    print(cutter.counts[0])
    print(cutter.counts[1])

solve_v3()

#############################################################################

def solve_v4():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    board = [list(map(int, input[1+i*n : 1+(i+1)*n])) for i in range(n)]

    def get_counts(sub_grid):
        n_sub = len(sub_grid)
        first = sub_grid[0][0]
        # 모든 칸이 첫 번째 칸과 같은지 검사
        if all(all(cell == first for cell in row) for row in sub_grid):
            return (1, 0) if first == 0 else (0, 1)
        
        m = n_sub // 2
        # 슬라이싱을 통한 영역 분할
        quad1 = [row[:m] for row in sub_grid[:m]]
        quad2 = [row[m:] for row in sub_grid[:m]]
        quad3 = [row[:m] for row in sub_grid[m:]]
        quad4 = [row[m:] for row in sub_grid[m:]]
        
        w_sum, b_sum = 0, 0
        for quad in [quad1, quad2, quad3, quad4]:
            w, b = get_counts(quad)
            w_sum += w
            b_sum += b
        return w_sum, b_sum

    white, blue = get_counts(board)
    print(f"{white}\n{blue}")

solve_v4()

#############################################################################

def solve_v5():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    board = [data[1+i*n : 1+(i+1)*n] for i in range(n)]

    def count_paper(r, c, d):
        target = board[r][c]
        for i in range(r, r + d):
            for j in range(c, c + d):
                if board[i][j] != target:
                    # 4개 영역의 결과를 합산하여 반환
                    half = d // 2
                    res = [0, 0]
                    for nr, nc in [(r, c), (r, c+half), (r+half, c), (r+half, c+half)]:
                        sub = count_paper(nr, nc, half)
                        res[0] += sub[0]
                        res[1] += sub[1]
                    return res
        
        # 단일 색상인 경우
        return [1, 0] if target == 0 else [0, 1]

    ans = count_paper(0, 0, n)
    print('\n'.join(map(str, ans)))

solve_v5()

#############################################################################

