def solve_v1():
    try:
        line = input().split()
        if not line: return
        m, n = map(int, line)
        if n < 2:
            print(0); return

        # bytearray로 메모리 사용량 최소화 (10MB)
        is_prime = bytearray([1]) * (n + 1)
        is_prime[0] = is_prime[1] = 0
        
        # 에라토스테네스의 체: 슬라이싱 최적화
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # i*i부터 n까지 i 간격으로 0 대입
                is_prime[i*i : n+1 : i] = bytearray(len(range(i*i, n+1, i)))
        
        # 범위 내의 1(True) 개수만 카운트
        print(is_prime[m : n+1].count(1))
    except: pass

solve_v1()

##########################################################

def solve_v2():
    try:
        m, n = map(int, input().split())
        sieve = bytearray([1]) * (n + 1)
        sieve[0] = sieve[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                sieve[i*i : n+1 : i] = bytearray(len(range(i*i, n+1, i)))
        
        # 누적 합 배열 생성
        prefix = [0] * (n + 1)
        count = 0
        for i in range(n + 1):
            if sieve[i]:
                count += 1
            prefix[i] = count
            
        print(prefix[n] - prefix[m-1])
    except: pass

solve_v2()

##########################################################

def solve_v3():
    try:
        m, n = map(int, input().split())
        if n < 2:
            print(0); return
        
        # 홀수만 관리 (index i -> 2*i + 1)
        size = (n + 1) // 2
        sieve = bytearray([1]) * size
        sieve[0] = 0 # 1 제외
        
        for i in range(1, int(n**0.5) // 2 + 1):
            if sieve[i]:
                p = 2 * i + 1
                start = (p * p) // 2
                sieve[start::p] = bytearray(len(range(start, size, p)))
        
        count = 1 if m <= 2 <= n else 0 # 2 포함 여부
        start_idx = (m if m % 2 != 0 else m + 1) // 2
        if start_idx < size:
            count += sieve[start_idx:].count(1)
        print(count)
    except: pass

solve_v3()

##########################################################

def solve_v4():
    try:
        m, n = map(int, input().split())
        limit = int(n**0.5) + 1
        base = bytearray([1]) * limit
        base[0] = base[1] = 0
        for i in range(2, int(limit**0.5) + 1):
            if base[i]:
                base[i*i:limit:i] = bytearray(len(range(i*i, limit, i)))
        primes = [i for i, v in enumerate(base) if v]
        
        seg_size = n - m + 1
        segment = bytearray([1]) * seg_size
        if m == 1: segment[0] = 0
        
        for p in primes:
            start = max(p * p, (m + p - 1) // p * p)
            if start <= n:
                segment[start-m : seg_size : p] = bytearray(len(range(start-m, seg_size, p)))
        print(segment.count(1))
    except: pass

solve_v4()

##########################################################

def solve_v5():
    try:
        m, n = map(int, input().split())
        if n < 2:
            print(0); return

        # 소수 판별 배열과 소수 목록 리스트
        is_prime = bytearray([1]) * (n + 1)
        primes = []
        
        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)
            # 현재 i와 소수 목록을 곱해 합성수 제거
            for p in primes:
                if i * p > n: break
                is_prime[i * p] = 0
                # i가 p로 나누어지면 p가 i*p의 최소 소인수이므로 중단
                if i % p == 0: break
        
        # 범위 내 소수 카운트 (이진 탐색이나 리스트 컴프리헨션 활용)
        ans = sum(1 for p in primes if p >= m)
        print(ans)
    except: pass

solve_v5()

##########################################################


