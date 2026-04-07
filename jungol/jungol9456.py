def ElonMusk(x, a, b, c):
    return a * (x**2) + b * x + c

a, b, c = map(int, input().split())
# print(a, b, c)
for x in [2, 3, 5]:
    print(ElonMusk(x, a, b, c))

############################################################(방법01)

def Trump(a, b, c):
    def f(x):
        return a*x**2 + b*x + c
    return f

a, b, c = map(int, input().split())
# print(a, b, c)
f = Trump(a, b, c)
print(*(f(x) for x in [2, 3, 5]), sep='\n')

############################################################(방법02)

a, b, c = map(int, input().split())
print(a, b, c)

def func(x, a, b, c):
    res = a * x * x + b * x + c
    return res

print(func(2, a, b, c))
print(func(3, a, b, c))
print(func(5, a, b, c))

############################################################(방법03)


