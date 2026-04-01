def get_sum(a, b):
    return a + b

def get_diff(a, b):
    return abs(a - b)

n1, n2 = map(int, input().split())
# print(n1, n2)
print(f"두 수의 합 = {get_sum(n1, n2)}")
print(f"두 수의 차 = {get_diff(n1, n2)}")

######################################################(방법01)

def calculate(a, b):
    return a + b, abs(a - b)

n1, n2 = map(int, input().split())

s, d = calculate(n1, n2)
# print(s, d)
print(f"두 수의 합 = {s}")
print(f"두 수의 차 = {d}")

######################################################(방법02)

def get_results(a, b):
    return {
        "합": a + b,
        "차": abs(a - b)
    }

n1, n2 = map(int, input().split())
res = get_results(n1, n2)

print(f"두 수의 합 = {res['합']}")
print(f"두 수의 차 = {res['차']}")

######################################################(방법03)

def func_plus(n1, n2):
    return n1 + n2

def func_minus(p1, p2):
    if p1 > p2:
        return p1 - p2
    else:
        return p2 - p1

n1, n2 = map(inp, input().split())
# print(n1, n2)

ret1 = func_plus(n1, n2)
print(f"두 수의 합 = {ret1}")

ret2 = func_minus(p1, p2)
print(f"두 수의 차 = {ret2}")

######################################################(방법04)

def calc(p1, p2):
    sun = p1 + p2
    minus = 0
    if p1 > p2:
        minus = p1 - p2
    else:
        minus = p2 - p1

    return [sum, minus]

r1, r2 = calc(50, 30)
print(r1, r2)

######################################################(방법05)

N, M = map(int,input().split())
Y = abs(N - M)
def f():
    print(f'두 수의 합 = {N + M}')
    print(f'두 수의 차 =', Y)
f()

######################################################(방법06)

def A(x, y):
    return x + y

def B(x, y):
    return abs(x - y)

n1, n2 = map(int, input().split())

print(f"두 수의 합 = {A(n1, n2)}")
print(f"두 수의 차 = {B(n1, n2)}")

######################################################(방법07)

