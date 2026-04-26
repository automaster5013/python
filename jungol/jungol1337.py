n = int(input())
# 삼각형 구조의 2차원 리스트 생성 (-1로 초기화)
matrix = [[-1] * i for i in range(1, n + 1)]

# 1. 오른쪽 아래, 2. 왼쪽, 3. 위쪽
dr = [1, 0, -1]
dc = [1, -1, 0]

r, c, d = 0, 0, 0
total = n * (n + 1) // 2

for num in range(total):
    matrix[r][c] = num % 10
    
    # 다음 칸 예상 위치
    nr, nc = r + dr[d], c + dc[d]
    
    # 범위를 벗어나거나 이미 채워진 칸을 만난 경우 방향 전환
    # nr < nc 조건은 삼각형의 오른쪽 대각선 경계를 체크함
    if not (0 <= nr < n and 0 <= nc <= nr and matrix[nr][nc] == -1):
        d = (d + 1) % 3
        nr, nc = r + dr[d], c + dc[d]
    
    r, c = nr, nc

# 결과 출력
for row in matrix:
    print(*(row))

#########################################################################

n = int(input())
matrix = [[0] * i for i in range(1, n + 1)]

r, c = -1, -1  # 시작 위치 보정
num = 0
limit = n

while limit > 0:
    # 1. 대각선 아래로 이동 (limit개)
    for _ in range(limit):
        r += 1; c += 1
        matrix[r][c] = num % 10
        num += 1
    limit -= 1
    if limit <= 0: break
    
    # 2. 왼쪽으로 이동 (limit개)
    for _ in range(limit):
        c -= 1
        matrix[r][c] = num % 10
        num += 1
    limit -= 1
    if limit <= 0: break
    
    # 3. 위로 이동 (limit개)
    for _ in range(limit):
        r -= 1
        matrix[r][c] = num % 10
        num += 1
    limit -= 1

for row in matrix:
    print(*(row))

#########################################################################

n = int(input())
matrix = [[None] * i for i in range(1, n + 1)]
r, c, num = 0, 0, 0
mode = "DOWN_RIGHT"

for _ in range(n * (n + 1) // 2):
    matrix[r][c] = num % 10
    num += 1
    
    if mode == "DOWN_RIGHT":
        if r + 1 < n and matrix[r+1][c+1] is None:
            r += 1; c += 1
        else:
            mode = "LEFT"; c -= 1
    elif mode == "LEFT":
        if c - 1 >= 0 and matrix[r][c-1] is None:
            c -= 1
        else:
            mode = "UP"; r -= 1
    elif mode == "UP":
        if r - 1 >= 0 and matrix[r-1][c] is None:
            r -= 1
        else:
            mode = "DOWN_RIGHT"; r += 1; c += 1

for row in matrix:
    print(*(row))

#########################################################################

n = int(input())
matrix = [[0] * i for i in range(1, n + 1)]

def fill(r, c, size, start_num):
    if size <= 0: return
    if size == 1:
        matrix[r][c] = start_num % 10
        return
    
    curr_num = start_num
    # 대각선 아래
    for i in range(size):
        matrix[r + i][c + i] = curr_num % 10; curr_num += 1
    # 왼쪽
    for i in range(1, size):
        matrix[r + size - 1][c + size - 1 - i] = curr_num % 10; curr_num += 1
    # 위쪽
    for i in range(1, size - 1):
        matrix[r + size - 1 - i][c] = curr_num % 10; curr_num += 1
        
    # 안쪽 삼각형 호출 (시작점은 (r+2, c+1), 크기는 size-3)
    fill(r + 2, c + 1, size - 3, curr_num)

fill(0, 0, n, 0)

for row in matrix:
    print(*(row))

#########################################################################

def solve_flat_mapping():
    try:
        line = input().split()
        if not line: return
        n = int(line[0])
        
        # 1. 1차원 리스트로 전체 공간 확보
        total_size = n * (n + 1) // 2
        flat_matrix = [0] * total_size
        
        # 방향: 0(하), 1(좌), 2(상) - 이번엔 인덱스 계산 편의상 순서 조정
        # 하지만 문제의 '오른쪽 아래 대각선' 규칙을 지키기 위해 1번 방식의 로직 차용
        dr = [1, 0, -1]
        dc = [1, -1, 0]
        
        r, c, d = 0, 0, 0
        
        # 이미 방문한 곳을 체크하기 위한 1차원 불리언 배열
        visited = [False] * total_size
        
        for num in range(total_size):
            # (r, c)를 1차원 인덱스로 변환하여 값 대입
            idx = (r * (r + 1) // 2) + c
            flat_matrix[idx] = num % 10
            visited[idx] = True
            
            if num == total_size - 1: break
            
            while True:
                nr, nc = r + dr[d], c + dc[d]
                # 2차원 범위 체크 및 1차원 인덱스 변환 후 방문 체크
                if 0 <= nr < n and 0 <= nc <= nr:
                    n_idx = (nr * (nr + 1) // 2) + nc
                    if not visited[n_idx]:
                        r, c = nr, nc
                        break
                # 벽이나 방문지에 부딪히면 방향 전환
                d = (d + 1) % 3
        
        # 2. 출력 (1차원 리스트를 다시 삼각형 모양으로 끊어서 출력)
        curr_idx = 0
        for i in range(1, n + 1):
            print(*(flat_matrix[curr_idx : curr_idx + i]))
            curr_idx += i
            
    except:
        print("INPUT ERROR!")

solve_flat_mapping()

#########################################################################

