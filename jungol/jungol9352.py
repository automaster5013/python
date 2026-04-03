inp = [int(input()) for i in range(50)]
# print(inp)
print(*reversed(inp))

###############################################(방법01)

inp = []
for i in range(50):
    inp.append(int(input()))

for i in range(49, -1, -1):
    print(inp[i], end=" ")

###############################################(방법02)

inp = [int(input()) for i in range(50)]
# print(inp)
print(*inp[::-1])

###############################################(방법03)

inp = [int(input()) for i in range(50)]
# print(inp)
inp.reverse()
print(*inp)

###############################################(방법04)

inp = []
for i in range(5):
    x = input()
    inp.append(x)

# print(inp)
# print(len(inp))
# print(inp[0])
# print(inp[len(inp)-1])

for x in range(len(inp)-1, -1, -1):
    print(inp[x], end=' ')

###############################################(방법05)

L =[]
for i in range(50):
    L.append(int(input()))
print(*L[::-1])

###############################################(방법06)

list1=list(map(int, [input() for _ in range(50)]))
for i in reversed(list1):
    print(i,end=" ")

###############################################(방법07)


