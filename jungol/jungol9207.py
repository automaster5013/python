a, b = map(int, input().split())
a, b = a % 2, b + 10
print(f"{a} {b} {a + b}")

#################################################(방법01)

a, b = map(int, input().split())
res = [a % 2, b + 10]
print(*(res + [sum(res)]))

#################################################(방법02)

a, b = map(int, input().split())
cal_a, cal_b = a % 2, b + 10
print(cal_a, cal_b, cal_a + cal_b)

#################################################(방법03)

a, b = map(int, input().split())
a, b = a & 1, b + 10
print(a, b, a + b)

#################################################(방법04)

def cal(N, M):
    A = N % 2
    B = M + 10
    return A, B, A + B

N, M = map(int, input().split())
a, b, c = cal(N, M)
print(*cal(N, M))

#################################################(방법05)

a, b = map(int, input().split())

first = a % 2
second = b + 10
total = first + second

print(first, second, total)

#################################################(방법06)



