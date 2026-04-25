n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

sum_divisors = 0
sum_multiples = 0

for x in numbers:
    # 약수 조건: m을 x로 나누었을 때 나머지가 0
    if m % x == 0:
        sum_divisors += x
    
    # 배수 조건: x를 m으로 나누었을 때 나머지가 0
    if x % m == 0:
        sum_multiples += x

print(sum_divisors)
print(sum_multiples)

###########################################################

n = int(input())
nums = [int(x) for x in input().split()]
m = int(input())

# 약수들만 모아서 합산
div_sum = sum([x for x in nums if m % x == 0])

# 배수들만 모아서 합산
mul_sum = sum([x for x in nums if x % m == 0])

print(div_sum)
print(mul_sum)

###########################################################

n = int(input())
data = list(map(int, input().split()))
m = int(input())

# filter 함수는 조건이 True인 요소만 남깁니다.
divisors = filter(lambda x: m % x == 0, data)
multiples = filter(lambda x: x % m == 0, data)

print(sum(divisors))
print(sum(multiples))

###########################################################

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

ans_div = 0
ans_mul = 0

for x in arr:
    # (m % x == 0)이 참이면 x * 1, 거짓이면 x * 0이 더해집니다.
    ans_div += x * (m % x == 0)
    ans_mul += x * (x % m == 0)

print(ans_div)
print(ans_mul)

###########################################################

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

def classify_and_sum(target, numbers):
    # (약수 합, 배수 합) 튜플을 반환하는 구조
    d_sum, m_sum = 0, 0
    for val in numbers:
        is_div = 1 if target % val == 0 else 0
        is_mul = 1 if val % target == 0 else 0
        
        d_sum += val * is_div
        m_sum += val * is_mul
    return d_sum, m_sum

res_div, res_mul = classify_and_sum(m, nums)
print(res_div)
print(res_mul)

###########################################################


