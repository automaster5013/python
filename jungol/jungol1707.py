n = int(input())
matrix = [[0] * n for _ in range(n)]

# 우, 하, 좌, 상 순서의 방향 벡터
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r, c, d = 0, 0, 0
for i in range(1, n * n + 1):
    matrix[r][c] = i
    
    # 다음 칸 예상
    nr, nc = r + dr[d], c + dc[d]
    
    # 벽에 부딪히거나 이미 숫자가 있으면 방향 전환
    if nr < 0 or nr >= n or nc < 0 or nc >= n or matrix[nr][nc] != 0:
        d = (d + 1) % 4
        nr, nc = r + dr[d], c + dc[d]
        
    r, c = nr, nc

# 출력
for row in matrix:
    print(*(row))

####################################################################################

n = int(input())
matrix = [[0] * n for _ in range(n)]

top, bottom = 0, n - 1
left, right = 0, n - 1
num = 1

while num <= n * n:
    # 1. 왼쪽 -> 오른쪽 (상단 고정)
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    
    # 2. 위 -> 아래 (오른쪽 고정)
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    
    # 3. 오른쪽 -> 왼쪽 (하단 고정)
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    
    # 4. 아래 -> 위 (왼쪽 고정)
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(*(row))

####################################################################################

n = int(input())
matrix = [[0] * n for _ in range(n)]

def fill_shell(start_r, start_c, size, val):
    if size <= 0: return
    if size == 1:
        matrix[start_r][start_c] = val
        return
        
    r, c = start_r, start_c
    # 상, 우, 하, 좌 순서로 테두리 채우기
    for i in range(size - 1): matrix[r][c + i] = val; val += 1
    for i in range(size - 1): matrix[r + i][start_c + size - 1] = val; val += 1
    for i in range(size - 1): matrix[start_r + size - 1][start_c + size - 1 - i] = val; val += 1
    for i in range(size - 1): matrix[start_r + size - 1 - i][start_c] = val; val += 1
    
    # 안쪽 사각형으로 진입
    fill_shell(start_r + 1, start_c + 1, size - 2, val)

fill_shell(0, 0, n, 1)

for row in matrix:
    print(*(row))

####################################################################################

n = int(input())
matrix = [[0] * n for _ in range(n)]

r, c = 0, -1 # 초기 열 위치를 -1로 시작
num = 1
dist = n     # 이동 거리
sign = 1     # 증감 방향 (1 또는 -1)

while dist > 0:
    # 가로 이동
    for _ in range(dist):
        c += sign
        matrix[r][c] = num
        num += 1
    
    dist -= 1 # 가로 한 번 가면 이동 거리 감소
    if dist == 0: break
    
    # 세로 이동
    for _ in range(dist):
        r += sign
        matrix[r][c] = num
        num += 1
    
    sign *= -1 # 한 사이클이 끝나면 방향 반전

for row in matrix:
    print(*(row))

####################################################################################

def snail_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    # 숫자를 거꾸로 역산하여 채우는 방식이나 회전 기법은 복잡하므로 
    # 여기서는 리스트 조작의 묘미를 보여주는 구조로 대체합니다.
    def rotate(m):
        return [list(row) for row in zip(*m[::-1])]

    # 1D 리스트를 만들고 2D로 배치하는 기법 등을 연구해보세요!
    # (실무에서는 1번이나 2번 방식이 가장 권장됩니다.)

# 1번 방식을 토대로 가장 파이썬다운 가독성을 갖춘 최종 코드로 마무리합니다.
def final_snail(n):
    res = [[0]*n for _ in range(n)]
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    r, c, d = 0, 0, 0
    for i in range(1, n*n + 1):
        res[r][c] = i
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < n and 0 <= nc < n and res[nr][nc] == 0):
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
        r, c = nr, nc
    return res

n = int(input())
for row in final_snail(n):
    print(*(row))

####################################################################################


