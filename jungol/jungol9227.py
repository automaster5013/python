a, b = map(int, input().split())
# print(a, b)

if a > b:
    print(a)
else:
    print(b)

##########################################################(방법01)

a, b = map(int, input().split())
# print(a, b)

print(a if a > b else b)

##########################################################(방법02)

a, b = map(int, input().split())
c = [a, b]

print(max(c))   # = print(max(a, b))

##########################################################(방법03)
