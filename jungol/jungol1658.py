a, b = map(int, input().split())

def gcd(x, y):
    # 나머지가 0이 되는 순간의 나누는 수가 최대공약수
    if y == 0:
        return x
    return gcd(y, x % y)

# 최대공약수 계산
g = gcd(a, b)
# 최소공배수 공식: (a * b) / 최대공약수
l = (a * b) // g

print(g)
print(l)

########################################################

a, b = map(int, input().split())
original_a, original_b = a, b

# b가 0이 될 때까지 반복
while b > 0:
    a, b = b, a % b

gcd_val = a
lcm_val = (original_a * original_b) // gcd_val

print(gcd_val)
print(lcm_val)

########################################################

a, b = map(int, input().split())

# 1. 두 수 중 작은 값부터 1까지 거꾸로 확인 (최대공약수)
gcd_val = 1
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        gcd_val = i
        break

# 2. 두 수 중 큰 값부터 곱한 값까지 확인 (최소공배수)
# 하지만 효율성을 위해 공식 (a*b)//gcd 를 쓰는 것이 좋습니다.
lcm_val = (a * b) // gcd_val

print(gcd_val)
print(lcm_val)

########################################################

x, y = map(int, input().split())
a, b = x, y

# 두 수가 같아질 때까지 큰 수에서 작은 수를 뺌
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

gcd_val = a
print(gcd_val)
print((x * y) // gcd_val)

########################################################

a, b = map(int, input().split())
original_a, original_b = a, b

gcd_val = 1
divisor = 2

# 2부터 시작해서 두 수를 동시에 나눌 수 있는 수를 찾음
while divisor <= min(a, b):
    if a % divisor == 0 and b % divisor == 0:
        gcd_val *= divisor
        a //= divisor
        b //= divisor
    else:
        divisor += 1

print(gcd_val)
print((original_a * original_b) // gcd_val)

########################################################


