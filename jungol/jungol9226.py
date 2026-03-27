
for n in sorted(map(int, input().split())):
    print(n)

###############################################################(방법01)

a, b = map(int, input().split())
print(min(a, b))
print(max(a, b))

###############################################################(방법02)

a, b = map(int, input().split())

if a > b:
    a, b = b, a
print(a)
print(b)

###############################################################(방법03)

a, b = map(int, input().split())
print(a, b)

if a < b:
    print(a)
    print(b)
else:
    print(b)
    print(a)

###############################################################(방법04)

