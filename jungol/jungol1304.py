n = int(input())

for i in range(n):
    for j in range(n):
        # j(열 번호)만큼 n이 건너뛰어지고, i(행 번호)만큼 더해짐
        num = (j * n) + (i + 1)
        print(num, end=' ')
    print()

####################################################################

n = int(input())
# n x n 빈 사각형 틀 만들기
matrix = [[0] * n for _ in range(n)]

num = 1
for j in range(n):      # 열(Column) 먼저 순회
    for i in range(n):  # 행(Row) 순회
        matrix[i][j] = num
        num += 1

# 조립된 사각형 출력
for row in matrix:
    print(*(row))

####################################################################

n = int(input())

for i in range(1, n + 1):
    current = i
    for j in range(n):
        print(current, end=' ')
        current += n  # 옆 칸으로 갈 때마다 한 변의 길이(n)만큼 증가
    print()

####################################################################

n = int(input())
all_nums = list(range(1, n * n + 1))

for i in range(n):
    row = []
    # i번째 인덱스부터 n 간격으로 인덱스를 추출
    for j in range(i, n * n, n):
        row.append(all_nums[j])
    print(*(row))

####################################################################

n = int(input())

row = 0
while row < n:
    col = 0
    while col < n:
        # 현재 위치의 숫자를 직접 계산 (방식 1과 유사하나 구조가 다름)
        val = (col * n) + row + 1
        print(val, end=' ')
        col += 1
    print()
    row += 1

####################################################################


