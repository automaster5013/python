N = int(input())
# print(N)
for i in range(N, 0, -1):
    print(i, end=" ")

########################################################(방법01)

N = int(input())
# print(N)
for i in reversed(range(1, N + 1)):
    print(i, end=" ")

# ########################################################(방법02)

N = int(input())
# print(N)
while N >= 1:
    print(N, end=" ")
    N -= 1

########################################################(방법03)

N = int(input())
# print(N)
for i in range(N, 0, -1):
    print(i, end=' ')

########################################################(방법04)

N = int(input())
# print(N)
while N >= 1:
    print(N, end=' ')
    N = N - 1   # N -= 1과 동일

########################################################(방법05)

lst = []
N = int(input())
for i in range(1, N+1):
    lst.append(i)

lst2 = list(reversed(lst))
print(*lst2, end = ' ')

########################################################(방법06)

