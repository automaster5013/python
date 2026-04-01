s = input()
chars = list(s)
chars.reverse()
print("".join(chars))

#######################################(방법01)

s = input()
print(s[::-1])

#######################################(방법02)

s = input()
print("".join(reversed(s)))

#######################################(방법03)

s = input()
reversed_str = ""

for char in s:
    reversed_str = char + reversed_str
print(reversed_str)

#######################################(방법04)

s = input()
reversed_str = ""

for i in range(len(s)-1, -1, -1):
    reversed_str += s[i]
print(reversed_str)

#######################################(방법05)

s = input()
reversed_str = ""

for i in range(len(s)):
    reversed_str = s[i] + reversed_str
print(reversed_str)

#######################################(방법06)

inp = input()
# print(len(inp))
# print(inp[8])
for x in range(len(inp)-1, -1, -1):
    print(inp[x], end="")

#######################################(방법07)

inp = input()
s = "".join(reversed(inp))
print(s)

#######################################(방법08)

