numbers = [int(input()) for _ in range(30)]
print(*numbers)

###################################################(방법01)

numbers = []
for _ in range(30):
    n = int(input())
    numbers.append(n)
print(*numbers)

###################################################(방법02)

lst = []
for i in range(5):
    lst.appand(int(input()))

for i in lst:
    print(i, end=' ')

###################################################(방법03)

