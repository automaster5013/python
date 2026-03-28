a, b = map(int, input().split())

if a > b:
    print(a)
else:
    print(b)

##########################################################(방법01)

a, b = map(int, input().split())
print(a if a > b else b)

##########################################################(방법02)
