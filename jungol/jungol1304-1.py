n = int(input())
# print(n)
for i in range(n):
    for j in range(n):
        # j(열 번호)만큼 n이 건너뛰어지고, i(행 번호)만큼 더해짐
        num = (j * n) + (i + 1)
        print(num, end=' ')
    print()

##############################################################(방법01)

n = int(input())
# print(n)
matrix = [[0] * n for _ in range(n)]

num = 1
for j in range(n):      
    for i in range(n):  
        matrix[i][j] = num
        num += 1

for row in matrix:
    print(*(row))

##############################################################(방법02)

n = int(input())
# print(n)
for i in range(1, n + 1):
    current = i
    for j in range(n):
        print(current, end=' ')
        current += n  
    print()

##############################################################(방법03)

n = int(input())
# print(n)
all_nums = list(range(1, n * n + 1))

for i in range(n):
    row = []
    # i번째 인덱스부터 n 간격으로 인덱스를 추출
    for j in range(i, n * n, n):
        row.append(all_nums[j])
    print(*(row))

##############################################################(방법04)

n = int(input())
# print(n)
row = 0
while row < n:
    col = 0
    while col < n:
        val = (col * n) + row + 1
        print(val, end=' ')
        col += 1
    print()
    row += 1

##############################################################(방법05)







