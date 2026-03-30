def plus_ten(n):
    print(f"{n} + 10 = {n + 10}")

def minus_ten(n):
    print(f"{n} - 10 = {n - 10}")

num = int(input())
# print(num)
plus_ten(num)
minus_ten(num)

###################################################(방법01)

def solve(n, task):
    if task == 'plus10':
        return f"{n} + 10 = {n + 10}"
    elif task == 'minus10':
        return f"{n} - 10 = {n - 10}"

num = int(input())
print(solve(num, 'plus10'))
print(solve(num, 'minus10'))

###################################################(방법02)

def func_plus(param):
    return param + 10

def func_minus(param):
    return param - 10

inp = int(input())
ret1 = func_plus(inp)
ret2 = func_minus(inp)
print(f"{inp} + 10 = {ret1}")
print(f"{inp} - 10 = {ret2}")

###################################################(방법03)

a = int(input())

def Number():
    print(f"{a} + 10 = {a + 10}")
    print(f"{a} - 10 = {a - 10}")

Number()

###################################################(방법04)

