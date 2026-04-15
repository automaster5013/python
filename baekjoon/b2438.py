n = int(input())
# print(n)

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

############################################(방법01)

n = int(input())
# print(n)

for i in range(1, n + 1):
    print('*' * i)

############################################(방법02)

def print_stars(limit, current):        # 재귀함수 사용
    if current > limit:
        return
    
    print('*' * current)
    
    print_stars(limit, current + 1)

n = int(input())
# print(n)
print_stars(n, 1)

############################################(방법03)

N = int(input())
print(N)

for i in range(N):
    for j in range(N):
        if i >= j:
            print("*", end='')
    print()

############################################(방법04)

N = int(input())
for i in range(1, N+1):
    print('*'*i)

############################################(방법05)

n = int(input())

i = 1
while i <= n:
    print("*" * i)
    i += 1

############################################(방법06)

