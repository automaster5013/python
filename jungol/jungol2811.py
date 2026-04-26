def check_number(n):
    if n == 1:
        return "number one"
    
    # 2부터 루트 n까지 검사 (O(sqrt(N)))
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "composite number"
            
    return "prime number"

try:
    nums = list(map(int, input().split()))
    for x in nums:
        print(check_number(x))
except:
    pass

#######################################################################

def is_prime_optimized(n):
    if n == 1: return "number one"
    if n <= 3: return "prime number"
    if n % 2 == 0 or n % 3 == 0: return "composite number"
    
    # 5부터 시작해서 6씩 건너뛰며 검사 (5, 7, 11, 13...)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "composite number"
        i += 6
    return "prime number"

data = input().split()
if data:
    for val in map(int, data):
        print(is_prime_optimized(val))

#######################################################################

def solve_pythonic():
    try:
        nums = map(int, input().split())
        for n in nums:
            if n == 1:
                print("number one")
                continue
            
            # 2부터 루트 n까지 나누어 떨어지는 것이 하나도 없는지(all) 확인
            if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
                print("prime number")
            else:
                print("composite number")
    except:
        pass

solve_pythonic()

#######################################################################

def get_type(n):
    if n == 1: return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return 1
    return 2

# 결과 메시지 매핑
res_map = {0: "number one", 1: "composite number", 2: "prime number"}

raw = input().split()
if raw:
    for x in map(int, raw):
        print(res_map[get_type(x)])

#######################################################################

def solve_flag():
    try:
        raw_input = input().split()
        for s in raw_input:
            n = int(s)
            if n == 1:
                print("number one")
                continue
            
            is_composite = False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    is_composite = True
                    break
            
            if is_composite:
                print("composite number")
            else:
                print("prime number")
    except:
        pass

solve_flag()

#######################################################################

