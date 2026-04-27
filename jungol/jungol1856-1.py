n, m = map(int, input().split())
# print(n, m)
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            num = i * m + j + 1
        else:
            num = i * m + (m - j)
        print(num, end=' ')
    print()

####################################################(방법01)

n, m = map(int, input().split())
# print(n, m)
current_num = 1
for i in range(n):
    row = []
    if i % 2 == 0:
        for j in range(m):
            row.append(current_num)
            current_num += 1
    else:
        for j in range(m):
            row.insert(0, current_num)
            current_num += 1
    print(*row)

####################################################(방법02)

n, m = map(int, input().split())
# print(n, m)
for i in range(n):
    row = list(range(i * m + 1, (i + 1) * m + 1))
    
    if i % 2 != 0:
        row = row[::-1]
    
    print(*row)

####################################################(방법03)

n, m = map(int, input().split())
# print(n, m)
row = 0
while row < n:
    if row % 2 == 0:
        col = 0
        while col < m:
            print(row * m + col + 1, end=' ')
            col += 1
    else:
        col = m - 1
        while col >= 0:
            print(row * m + col + 1, end=' ')
            col -= 1
    print()
    row += 1

####################################################(방법04)

n, m = map(int, input().split())
# print(n, m)
for i in range(n):
    if i % 2 == 0:
        start, end, step = i * m + 1, (i + 1) * m + 1, 1
    else:
        start, end, step = (i + 1) * m, i * m, -1
        
    for num in range(start, end, step):
        print(num, end=' ')
    print()

####################################################(방법05)

n, m = map(int, input().split())

num = 1
for i in range(n):
    row = []

    for j in range(m):
        row.append(num)
        num += 1

    if i % 2 == 0:
        print(*row)
    else:
        print(*row[::-1])

####################################################(방법06)

N, M = map(int, input().split())

EX = N * M

j = 1

for i in range(N):
    for _ in range(M):
        if j > EX:
            break
        print(j, end=" ")
        j += 1
    print()

    Q=[]

    for _ in range(M):
        if j > EX:
            break
        Q.append(j)
        j += 1
        
    Q.reverse()

    print(*Q, end=" ")
    print()

####################################################(방법07)





