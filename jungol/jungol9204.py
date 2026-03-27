import sys
a1, a2, a3, a4, a5, a6, a7 = map(int, sys.stdin.read().split())
# print(a1, a2, a3, a4, a5, a6, a7)

res = (a1 + 2, a2 - 2, a3 * 2, a4 / 2, a5 // 2, a6 % 2, a7 ** 2)

print(*res)

###############################################################(방법01)

inp1 = input()
inp2 = input()
inp3 = input()
inp4 = input()
inp5 = input()
inp6 = input()
inp7 = input()

#print(a1, a2, a3, a4, a5, a6, a7)

n1 = int(inp1)
n2 = int(inp2)
n3 = int(inp3)
n4 = int(inp4)
n5 = int(inp5)
n6 = int(inp6)
n7 = int(inp7)

print((n1 + 2), end=' ')
print((n2 - 2), end=' ')
print((n3 * 2), end=' ')
print((n4 / 2), end=' ')
print((n5 // 2), end=' ')
print((n6 % 2), end=' ')
print((n7 ** 2), end=' ')

###############################################################(방법02)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())

print(f"{a+2} {b-2} {c*2} {d/2} {e//2} {f%2} {g**2}")

###############################################################(방법03)
