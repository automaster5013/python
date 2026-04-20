A = []

while True:
    n = int(input())
    # print(n)
    if n == -1:
        break
    A.append(n)

print(*A[-3:])

##########################################################(방법01)

A = []

while True:
    n = int(input())
    # print(n)
    if n == -1:
        break
    A.append(n)

start_idx = max(0, len(A)-3)

for i in range(start_idx, len(A)):
    print(A[i], end=" ")

##########################################################(방법02)

A = []

for val in iter(input, "-1"):
    A.append(int(val))

print(*A[-3:])

##########################################################(방법03)

list = []

while True:
    n = int(input())
    if n == -1:
        break
    list.append(n)

print(*list[-3:])

#-------------------

list = []
for i in range(n):
    n = int(input())
    if n == -1:
        break
    list.append(n)

print(*list[-3:])


##########################################################(방법04)

