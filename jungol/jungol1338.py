n = int(input())
# n x n 빈 행렬 생성
matrix = [["" for _ in range(n)] for _ in range(n)]

char_code = ord('A')

# 대각선의 시작점은 (0, n-1), (1, n-1), ..., (n-1, n-1)
for start_row in range(n):
    r, c = start_row, n - 1
    # 왼쪽 아래 대각선 방향으로 이동하며 채움
    while r < n and c >= 0:
        matrix[r][c] = chr(char_code)
        # 알파벳 순환 (A=65, Z=90)
        char_code = ord('A') + (char_code - ord('A') + 1) % 26
        r += 1
        c -= 1

# 출력 포맷팅
for i in range(n):
    # 앞에 공백 출력: (n - 1 - i) * 2개
    print("  " * (n - 1 - i), end="")
    # i행에 있는 문자들 중 비어있지 않은 것만 출력
    row_chars = [matrix[i][j] for j in range(n) if matrix[i][j] != ""]
    print(" ".join(row_chars))

################################################################################

n = int(input())

for i in range(n):
    # 선행 공백 출력
    print("  " * (n - 1 - i), end="")
    row_data = []
    for j in range(n - 1 - i, n):
        # (i, j)가 속한 대각선의 번호 k 계산
        k = i + j - (n - 1)
        # 이전 대각선들까지 채워진 문자의 총 개수: k개 대각선의 합
        # n + (n-1) + ... + (n-k+1)
        count = k * n - (k * (k - 1) // 2)
        # 현재 대각선에서의 순서 (i - k)
        order = count + (i - k)
        row_data.append(chr(ord('A') + (order % 26)))
    print(" ".join(row_data))

################################################################################

n = int(input())
matrix = [[""] * n for _ in range(n)]

# 각 열(j)의 시작 문자 순서 계산
for j in range(n - 1, -1, -1):
    # j번째 열의 첫 글자(가장 윗행)의 시작 번호
    # (n-1-j)번째 대각선의 시작점임
    k = n - 1 - j
    start_val = k * n - (k * (k - 1) // 2)
    
    # 해당 열의 데이터를 위에서 아래로 채움
    for i in range(k, n):
        matrix[i][j] = chr(65 + (start_val % 26))
        start_val += 1

# 출력
for i in range(n):
    print(" " * ((n - 1 - i) * 2), end="")
    print(" ".join(matrix[i][n-1-i : n]))

################################################################################

n = int(input())
from_rows = {i: [] for i in range(n)}

char_code = 0
# 총 n(n+1)/2 개의 문자를 대각선 순서로 생성
for k in range(n):
    # k번째 대각선은 (k, n-1)에서 시작
    r, c = k, n - 1
    while r < n and c >= 0:
        from_rows[r].append(chr(65 + (char_code % 26)))
        char_code += 1
        r += 1
        c -= 1

# 딕셔너리에 쌓인 데이터를 출력
for i in range(n):
    spaces = "  " * (n - 1 - i)
    print(f"{spaces}{' '.join(from_rows[i])}")

################################################################################

n = int(input())
# 1. 채워질 좌표들을 순서대로 리스트에 담기
coords = []
for k in range(n):
    r, c = k, n - 1
    while r < n and c >= 0:
        coords.append((r, c))
        r += 1
        c -= 1

# 2. 좌표에 알파벳 매칭하여 저장
result_map = {}
for idx, pos in enumerate(coords):
    result_map[pos] = chr(65 + (idx % 26))

# 3. 행별로 좌표를 찾아 출력
for i in range(n):
    print("  " * (n - 1 - i), end="")
    line = []
    for j in range(n):
        if (i, j) in result_map:
            line.append(result_map[(i, j)])
    print(" ".join(line))

################################################################################

