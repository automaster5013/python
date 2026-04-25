n = int(input())
arr = list(map(int, input().split()))

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    if a == 0 or b == 0: return 0
    return (a * b) // get_gcd(a, b)

# 초기값 설정
final_gcd = arr[0]
final_lcm = arr[0]

# 순차적으로 연산 적용
for i in range(1, n):
    final_gcd = get_gcd(final_gcd, arr[i])
    final_lcm = get_lcm(final_lcm, arr[i])

print(final_gcd, final_lcm)

#############################################################

n = int(input())
nums = list(map(int, input().split()))

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def solve(arr):
    if len(arr) == 1:
        return arr[0], arr[0] # (gcd, lcm)
    
    mid = len(arr) // 2
    gcd_l, lcm_l = solve(arr[:mid])
    gcd_r, lcm_r = solve(arr[mid:])
    
    res_gcd = gcd(gcd_l, gcd_r)
    # 두 구간의 lcm을 구할 때도 lcm 공식 적용
    res_lcm = (lcm_l * lcm_r) // gcd(lcm_l, lcm_r)
    
    return res_gcd, res_lcm

g, l = solve(nums)
print(g, l)

#############################################################

n = int(input())
nums = list(map(int, input().split()))

all_factors = {} # {소수: [각 수에서의 지수들]}

for x in nums:
    d = 2
    temp = x
    current_factors = {}
    while d * d <= temp:
        while temp % d == 0:
            current_factors[d] = current_factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        current_factors[temp] = current_factors.get(temp, 0) + 1
    
    # 전체 소수 목록 업데이트
    for f in current_factors:
        if f not in all_factors: all_factors[f] = [0] * n
        
# 다시 돌며 지수 채우기 (생략된 소수는 지수 0)
for i in range(n):
    temp = nums[i]
    for f in all_factors:
        count = 0
        while temp % f == 0:
            count += 1
            temp //= f
        all_factors[f][i] = count

final_gcd, final_lcm = 1, 1
for f, exponents in all_factors.items():
    # GCD는 모든 지수 중 최소값, LCM은 최대값 사용
    final_gcd *= (f ** min(exponents))
    final_lcm *= (f ** max(exponents))

print(final_gcd, final_lcm)

#############################################################

n = int(input())
arr = list(map(int, input().split()))

# GCD 구하기
temp_gcd = arr[0]
for i in range(1, n):
    a, b = temp_gcd, arr[i]
    while b: a, b = b, a % b
    temp_gcd = a

# LCM 구하기 (사다리 방식 시뮬레이션)
lcm_res = 1
work_arr = list(arr)
d = 2
while d <= max(work_arr):
    divisible_indices = [i for i, v in enumerate(work_arr) if v % d == 0]
    if len(divisible_indices) >= 2: # 최소 두 개 이상 나누어지면
        lcm_res *= d
        for idx in divisible_indices:
            work_arr[idx] //= d
    else:
        d += 1

# 남은 모든 수 곱하기
for v in work_arr:
    lcm_res *= v

print(temp_gcd, lcm_res)

#############################################################

def get_calculator():
    def gcd(a, b):
        while b: a, b = b, a % b
        return a
    
    def process(func, values):
        res = values[0]
        for v in values[1:]:
            if func == 'gcd': res = gcd(res, v)
            else: res = (res * v) // gcd(res, v)
        return res
    
    return process

n = int(input())
nums = list(map(int, input().split()))

calc = get_calculator()
print(calc('gcd', nums), calc('lcm', nums))

#############################################################


