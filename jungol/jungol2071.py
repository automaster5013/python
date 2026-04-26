n, m = map(int, input().split())

# 1. 표준 파스칼 삼각형 생성
pascal = [[0] * n for _ in range(n)]
for i in range(n):
    pascal[i][0] = 1
    for j in range(1, i + 1):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

# 2. 종류별 출력
if m == 1:
    for i in range(n):
        print(*(pascal[i][:i+1]))
elif m == 2:
    for i in range(n-1, -1, -1):
        # n-1-i 개의 공백 출력 후 해당 행 출력
        print(" " * (n - 1 - i), end="")
        print(*(pascal[i][:i+1]))
elif m == 3:
    for i in range(n):
        # Type 3는 열과 행의 인덱스를 역산하여 출력
        row_to_print = []
        for j in range(i + 1):
            row_to_print.append(pascal[n-1-j][i-j])
        print(*(row_to_print))

##################################################################

def nCr(n, r):
    if r < 0 or r > n: return 0
    num = den = 1
    for i in range(r):
        num = num * (n - i)
        den = den * (i + 1)
    return num // den

n, m = map(int, input().split())

if m == 1:
    for i in range(n):
        print(*(nCr(i, j) for j in range(i + 1)))
elif m == 2:
    for i in range(n - 1, -1, -1):
        print(" " * (n - 1 - i), end="")
        print(*(nCr(i, j) for j in range(i + 1)))
elif m == 3:
    for i in range(n):
        print(*(nCr(n - 1 - j, i - j) for j in range(i + 1)))

##################################################################

n, m = map(int, input().split())

# 기본 행 생성
rows = [[1]]
for i in range(1, n):
    prev = rows[-1]
    # 양끝에 0을 붙여 더하는 트릭: [0,1,1] + [1,1,0] = [1,2,1]
    curr = [a + b for a, b in zip([0] + prev, prev + [0])]
    rows.append(curr)

if m == 1:
    for row in rows: print(*(row))
elif m == 2:
    for i, row in enumerate(rows[::-1]):
        print(" " * i + " ".join(map(str, row)))
elif m == 3:
    # 각 줄마다 필요한 요소를 뽑아 재조합
    for i in range(n):
        line = [rows[n-1-j][i-j] for j in range(i+1)]
        print(*(line))

##################################################################

n, m = map(int, input().split())
data = {}

# 데이터 빌드
for r in range(n):
    for c in range(r + 1):
        if c == 0 or c == r: data[(r, c)] = 1
        else: data[(r, c)] = data[(r-1, c-1)] + data[(r-1, c)]

# 매핑 출력
if m == 1:
    for r in range(n):
        print(*(data[(r, c)] for c in range(r + 1)))
elif m == 2:
    for r in range(n-1, -1, -1):
        print(" " * (n - 1 - r) + " ".join(str(data[(r, c)]) for c in range(r + 1)))
elif m == 3:
    for c in range(n):
        # Type 3의 규칙: r-c가 일정하게 감소하는 패턴
        print(*(data[(n-1-j, c-j)] for j in range(c + 1)))

##################################################################

def get_pascal_row(n):
    row = [1]
    for _ in range(n):
        yield row
        row = [sum(pair) for pair in zip([0] + row, row + [0])]

n, m = map(int, input().split())
all_rows = list(get_pascal_row(n))

if m == 1:
    for r in all_rows: print(*(r))
elif m == 2:
    for i, r in enumerate(all_rows[::-1]):
        print(" " * i, *(r))
elif m == 3:
    # 전치 행렬(Transpose)의 원리를 응용한 세로형 출력
    for i in range(n):
        res = []
        for j in range(i + 1):
            res.append(all_rows[n - 1 - j][i - j])
        print(*(res))

##################################################################


