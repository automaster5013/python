n = int(input())
# print(n)
for i in range(-10, n + 1):
    print(i, end=" ")

########################################################(방법01)

n = int(input())
# print(n)
pie = -10
while pie <= n:
    print(pie, end=" ")
    pie += 1  

########################################################(방법02)

n = int(input())
# print(n)
print(*(i for i in range(-10, n + 1)))

########################################################(방법03)

N = int(input())
# print(N)

for x in range(-10, N+1):
    print(x, end=' ')

########################################################(방법04)

N = int(input())
lst = []
for i in range(-10, N+1):
    lst.append(i)
print(*lst)

########################################################(방법05)

