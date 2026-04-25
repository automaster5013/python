n = int(input())

# n x n 격자 초기화
matrix = [["" for _ in range(n)] for _ in range(n)]

current_char = ord('A')

for j in range(n):
    if j % 2 == 0:
        # 짝수 열 (0, 2...): 위에서 아래로
        for i in range(n):
            matrix[i][j] = chr(current_char)
            # A-Z 순환 로직
            current_char = ord('A') + (current_char - ord('A') + 1) % 26
    else:
        # 홀수 열 (1, 3...): 아래에서 위로
        for i in range(n - 1, -1, -1):
            matrix[i][j] = chr(current_char)
            current_char = ord('A') + (current_char - ord('A') + 1) % 26

# 결과 출력
for row in matrix:
    print(*row)

######################################################################################

n = int(input())

for i in range(n):
    for j in range(n):
        # j열이 짝수면 위에서 i번째, 홀수면 아래에서 i번째(n-1-i)
        if j % 2 == 0:
            count = j * n + i
        else:
            count = j * n + (n - 1 - i)
            
        # 26으로 나눈 나머지를 이용해 알파벳 결정
        char = chr(ord('A') + (count % 26))
        print(char, end=" ")
    print()

######################################################################################

n = int(input())

# 전체 칸에 들어갈 알파벳을 순서대로 생성
total_chars = [chr(ord('A') + (k % 26)) for k in range(n * n)]

# n개씩 잘라서 리스트에 담기
cols = []
for i in range(n):
    col_data = total_chars[i * n : (i + 1) * n]
    # 홀수 번째 열(인덱스 1, 3...)은 진행 방향이 반대이므로 뒤집기
    if i % 2 != 0:
        col_data = col_data[::-1]
    cols.append(col_data)

# 행과 열을 바꿔서 출력 (Transpose 개념)
for i in range(n):
    for j in range(n):
        print(cols[j][i], end=" ")
    print()

######################################################################################

n = int(input())

for i in range(n):
    for j in range(n):
        # 현재 출력하려는 (i, j)가 몇 번째 알파벳인지 계산
        # 짝수 열이면 j * n + i 번째
        # 홀수 열이면 j * n + (n - 1 - i) 번째
        order = j * n + (i if j % 2 == 0 else (n - 1 - i))
        
        # 알파벳 출력
        print(chr(65 + (order % 26)), end=" ")
    print()

######################################################################################

n = int(input())
matrix = [[""] * n for _ in range(n)]

r, c = 0, 0
step = 1 # 1이면 아래로, -1이면 위로
char_code = 0

for j in range(n):
    # 현재 열(c)을 step 방향으로 채움
    for _ in range(n):
        matrix[r][c] = chr(65 + (char_code % 26))
        char_code += 1
        if _ < n - 1: # 열의 마지막 칸이 아닐 때만 행 이동
            r += step
    
    # 한 열이 끝나면 다음 열로 이동하고 방향 반전
    c += 1
    step *= -1

for row in matrix:
    print(" ".join(row))

######################################################################################


