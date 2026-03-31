s = input()
for i in range(0, len(s), 2):
    print(s[i], end=" ")

########################################(방법01)

s = input()
print(*s[::2])

########################################(방법02)

s = input()
for i, char in enumerate(s):
    if i % 2 == 0:
        print(char, end=" ")

########################################(방법03)

inp = input()
for i in range(len(inp)):
    if i % 2 == 0:
        print(inp[i], end=' ')

########################################(방법04)

