import sys

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 2차원 배열(행렬) 구성
    matrix = []
    for i in range(n):
        matrix.append(input_data[1 + i*n : 1 + (i+1)*n])

    def compress(r, c, size):
        first_val = matrix[r][c]
        is_uniform = True
        
        # 현재 영역이 모두 같은 값인지 검사
        for i in range(r, r + size):
            for j in range(c, c + size):
                if matrix[i][j] != first_val:
                    is_uniform = False
                    break
            if not is_uniform:
                break
        
        # 모두 같으면 해당 숫자 반환
        if is_uniform:
            return first_val
        else:
            # 섞여 있으면 X를 붙이고 4등분 재귀 호출
            half = size // 2
            res = "X"
            res += compress(r, c, half)              # 좌상
            res += compress(r, c + half, half)       # 우상
            res += compress(r + half, c, half)       # 좌하
            res += compress(r + half, c + half, half) # 우하
            return res

    # 결과 출력
    print(compress(0, 0, n))

if __name__ == "__main__":
    solve_v1()

####################################################################

def solve_v2():
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    # 누적합 계산을 위해 정수로 변환
    grid = [list(map(int, input_data[1+i*n : 1+(i+1)*n])) for i in range(n)]
    
    # 2차원 누적합 배열(Integral Image) 생성
    sum_table = [[0] * (n + 1) for _ in range(n + 1)]
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            sum_table[r][c] = grid[r-1][c-1] + sum_table[r-1][c] + sum_table[r][c-1] - sum_table[r-1][c-1]

    def get_sum(r1, c1, r2, c2):
        return sum_table[r2+1][c2+1] - sum_table[r1][c2+1] - sum_table[r2+1][c1] + sum_table[r1][c1]

    def quadtree(r, c, size):
        s = get_sum(r, c, r + size - 1, c + size - 1)
        if s == 0: return "0"
        if s == size * size: return "1"
        
        m = size // 2
        return "X" + quadtree(r, c, m) + quadtree(r, c + m, m) + \
                     quadtree(r + m, c, m) + quadtree(r + m, c + m, m)

    print(quadtree(0, 0, n))

solve_v2()

####################################################################

def solve_v3():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    board = [data[1+i*n : 1+(i+1)*n] for i in range(n)]
    output = []

    def run(r, c, s):
        target = board[r][c]
        mixed = False
        for i in range(r, r + s):
            for j in range(c, c + s):
                if board[i][j] != target:
                    mixed = True
                    break
            if mixed: break
        
        if not mixed:
            output.append(target)
        else:
            output.append("X")
            h = s // 2
            run(r, c, h)
            run(r, c + h, h)
            run(r + h, c, h)
            run(r + h, c + h, h)

    run(0, 0, n)
    print("".join(output))

solve_v3()

####################################################################

