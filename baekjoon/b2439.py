n = int(input())
# print(n)
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

################################################(방법01)

n = int(input())
# print(n)
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
        
    for j in range(i):
        print("*", end="")
        
    print()

################################################(방법02)

N = int(input())
# print(N)

for row in range(N):
    for col in range(N-row-1):
        print("?", end='')

    for col2 in range(row+1):
        print("*", end='')
    print()

################################################(방법03)

a=int(input())
for i in range(1,a+1):
    print((i*"*").rjust(a))     # 우측 정렬

################################################(방법04)







