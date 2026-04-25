n = int(input())

# n x n 빈 격자 생성
matrix = [["" for _ in range(n)] for _ in range(n)]

char_code = ord('A')
# 열(j)은 n-1부터 0까지 감소
for j in range(n - 1, -1, -1):
    # 행(i)은 n-1부터 0까지 감소
    for i in range(n - 1, -1, -1):
        matrix[i][j] = chr(char_code)
        char_code += 1
        # Z(90)를 넘어가면 다시 A(65)로 초기화
        if char_code > ord('Z'):
            char_code = ord('A')

# 결과 출력
for row in matrix:
    print(*row)

##################################################################

n = int(input())

for i in range(n):
    for j in range(n):
        # 오른쪽 끝 열부터 j열까지 채워진 총 개수 + 현재 열에서 아래부터 i행까지 개수
        # 채워지는 순서 번호 = (n - 1 - j) * n + (n - 1 - i)
        order = (n - 1 - j) * n + (n - 1 - i)
        # 알파벳은 26개마다 반복됨
        char = chr(ord('A') + (order % 26))
        print(char, end=" ")
    print()

##################################################################

n = int(input())

for i in range(n):
    row = []
    for j in range(n):
        # i행 j열에 들어갈 문자의 순번 규칙 찾기
        # 오른쪽 아래(n-1, n-1)가 0번일 때, (i, j)는 (n-1-j)*n + (n-1-i)번
        diff = (n - 1 - j) * n + (n - 1 - i)
        row.append(chr(ord('A') + (diff % 26)))
    print(" ".join(row))

##################################################################

n = int(input())
# A부터 순서대로 n*n개를 담은 리스트 생성
total_chars = [chr(ord('A') + (k % 26)) for k in range(n * n)]

# 출력용 행렬 생성
res = [["" for _ in range(n)] for _ in range(n)]
idx = 0

# 문제의 조건대로 오른쪽 열 -> 왼쪽 열, 아래 행 -> 위 행 순으로 리스트 값을 배정
for j in range(n - 1, -1, -1):
    for i in range(n - 1, -1, -1):
        res[i][j] = total_chars[idx]
        idx += 1

for r in res:
    print(*r)

##################################################################

n = int(input())

# 각 열의 가장 아래 행(n-1)에 올 문자들의 기준점 계산
# j번째 열의 아래 끝 문자는 (n-1-j) * n 번째 문자임
for i in range(n):
    for j in range(n):
        # i행 j열의 문자는 (n-1-j)*n + (n-1-i)
        offset = (n - 1 - j) * n + (n - 1 - i)
        print(chr(65 + (offset % 26)), end=" ")
    print()

##################################################################

