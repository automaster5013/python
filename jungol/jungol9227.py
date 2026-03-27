a, b = map(int, input().split())

if a > b:
    print(a)
else:
    print(b)

##########################################################

a, b = map(int, input().split())
print(a if a > b else b)

