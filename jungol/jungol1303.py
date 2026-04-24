n, m = map(int, input().split())
# print(n, m)
num = 1
for i in range(n):
    for j in range(m):
        print(num, end=" ")
        num += 1
    print()

###############################################(방법01)

n, m = map(int, input().split())
# print(n, m)
for i in range(n):
    for j in range(1, m + 1):
        print(i * m + j, end=" ")
    print()

###############################################(방법02)

n, m = map(int, input().split())
# print(n, m)
for i in range(n):
    row = [str(num) for num in range(i * m + 1, i * m + m + 1)]
    print(" ".join(row))

###############################################(방법03)

n, m = map(int, input().split())
# print(n, m)
for i in range(1, n * m + 1):
    print(i, end=" ")
    if i % m == 0:
        print()

###############################################(방법04)

n, m = map(int,input().split())
# print(n, m)
num = 1
for row in range(n):   # 행
    for col in range(m):   # 열
        print(num, end=" ")
        num += 1
    print()

###############################################(방법05)







