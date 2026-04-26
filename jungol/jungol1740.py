def solve_v1():
    try:
        m = int(input())
        n = int(input())
    except: return

    # 1. 10,000까지의 소수 판별 배열 생성
    limit = 10000
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    # 2. 범위 내의 소수 필터링
    primes = [i for i in range(m, n + 1) if is_prime[i]]

    # 3. 결과 출력
    if not primes:
        print(-1)
    else:
        print(sum(primes))
        print(min(primes))

solve_v1()

#######################################################################

def check_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def solve_v2():
    try:
        m, n = int(input()), int(input())
        primes = []
        for i in range(m, n + 1):
            if check_prime(i):
                primes.append(i)
        
        if not primes:
            print(-1)
        else:
            print(sum(primes))
            print(primes[0]) # 리스트의 첫 번째 원소가 최솟값
    except: pass

solve_v2()

#######################################################################

def solve_v3():
    # 10,000까지의 모든 소수 리스트 미리 생성
    is_p = [True] * 10001
    is_p[0] = is_p[1] = False
    all_primes = []
    for i in range(2, 10001):
        if is_p[i]:
            all_primes.append(i)
            for j in range(i*i, 10001, i):
                is_p[j] = False

    try:
        m, n = int(input()), int(input())
        # 소수 리스트에서 범위에 맞는 것만 수집
        result = [p for p in all_primes if m <= p <= n]
        
        if not result:
            print(-1)
        else:
            print(sum(result))
            print(result[0])
    except: pass

solve_v3()

#######################################################################

def solve_v4():
    def is_p(x):
        if x < 2: return False
        return all(x % i != 0 for i in range(2, int(x**0.5) + 1))

    try:
        m, n = int(input()), int(input())
        # 범위 내의 숫자를 소수 판별 함수로 필터링
        primes = [i for i in range(m, n + 1) if is_p(i)]
        
        if not primes:
            print(-1)
        else:
            print(sum(primes))
            print(min(primes))
    except: pass

solve_v4()

#######################################################################

def solve_v5():
    try:
        m = int(input())
        n = int(input())
        
        total_sum = 0
        min_prime = -1
        
        for num in range(m, n + 1):
            if num < 2: continue
            
            # 소수 판별
            is_p = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_p = False
                    break
            
            if is_p:
                total_sum += num
                # 첫 번째 소수를 발견했을 때만 min_prime 설정
                if min_prime == -1:
                    min_prime = num
        
        if min_prime == -1:
            print(-1)
        else:
            print(total_sum)
            print(min_prime)
    except: pass

solve_v5()

#######################################################################

