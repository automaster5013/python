def solve_v1():
    try:
        line = input().split()
        if not line: return
        d, k = map(int, line)
        
        # a[i]: A의 계수, b[i]: B의 계수
        a, b = [0] * (d + 1), [0] * (d + 1)
        a[1], a[2] = 1, 0
        b[1], b[2] = 0, 1
        
        for i in range(3, d + 1):
            a[i] = a[i-1] + a[i-2]
            b[i] = b[i-1] + b[i-2]
            
        # a[d]*A + b[d]*B = k 를 만족하는 A 찾기
        for A in range(1, k):
            # 남은 양이 B의 계수로 나누어 떨어지는지 확인
            rem = k - (a[d] * A)
            if rem % b[d] == 0:
                B = rem // b[d]
                if A <= B: # 조건: 1 <= A <= B
                    print(A)
                    print(B)
                    return
    except: pass

solve_v1()

#####################################################################

def solve_v2():
    try:
        d, k = map(int, input().split())
        
        # 피보나치 수열로 계수 계산
        fib = [0] * (d + 1)
        fib[1], fib[2] = 1, 1
        for i in range(3, d + 1):
            fib[i] = fib[i-1] + fib[i-2]
            
        # 수식: fib[d-2]*A + fib[d-1]*B = k
        # d=3인 경우 예외 처리를 위해 계수 직접 지정
        X = fib[d-2] if d > 2 else 1
        Y = fib[d-1]
        
        for A in range(1, k // X + 1):
            if (k - X * A) % Y == 0:
                B = (k - X * A) // Y
                if A <= B:
                    print(f"{A}\n{B}")
                    return
    except: pass

solve_v2()

#####################################################################

def solve_v3():
    try:
        d, k = map(int, input().split())
        
        # d번째 날의 A와 B의 계수를 구함
        # f(d) = f(d-2)*A + f(d-1)*B
        x1, x2 = 1, 0 # A의 계수 변화
        y1, y2 = 0, 1 # B의 계수 변화
        
        for _ in range(3, d + 1):
            x1, x2 = x2, x1 + x2
            y1, y2 = y2, y1 + y2
        
        # x2*A + y2*B = k
        # A와 B의 최종 계수는 x2, y2
        for a in range(1, k):
            rem = k - (x2 * a)
            if rem > 0 and rem % y2 == 0:
                b = rem // y2
                if a <= b:
                    print(a)
                    print(b)
                    return
    except: pass

solve_v3()

#####################################################################

def solve_v4():
    try:
        d, k = map(int, input().split())
        
        # dp[i] = (A의 계수, B의 계수)
        dp = [(0, 0)] * (d + 1)
        dp[1], dp[2] = (1, 0), (0, 1)
        
        for i in range(3, d + 1):
            dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
            
        coef_a, coef_b = dp[d]
        
        for A in range(1, k // coef_a + 1):
            target = k - (coef_a * A)
            if target % coef_b == 0:
                B = target // coef_b
                if A <= B:
                    print(A)
                    print(B)
                    return
    except: pass

solve_v4()

#####################################################################

def solve_v5():
    try:
        line = input().split()
        if not line: return
        D, K = map(int, line)
        
        # 피보나치 계수 f1(A의 계수), f2(B의 계수)
        f = [0] * 31
        f[1], f[2] = 1, 1
        for i in range(3, 31):
            f[i] = f[i-1] + f[i-2]
            
        # K = f[D-2]*A + f[D-1]*B
        ca = f[D-2] if D > 2 else 1
        cb = f[D-1]
        
        # B는 최소 K // cb 보다는 작아야 함
        for B in range(K // cb, 0, -1):
            rem = K - (cb * B)
            if rem > 0 and rem % ca == 0:
                A = rem // ca
                if 1 <= A <= B:
                    # 결과가 여러 개일 수 있으므로 찾자마자 출력 후 종료
                    # 하지만 A가 작을수록 좋으므로 루프 방향에 따라 결과가 다를 수 있음
                    # 여기서는 B를 큰 값부터 확인하므로 다시 정렬해서 출력
                    pass
        
        # 올바른 순차 탐색을 위해 A 기준 탐색 재구현
        for A in range(1, K):
            if (K - ca * A) % cb == 0:
                B = (K - ca * A) // cb
                if A <= B:
                    print(A)
                    print(B)
                    return
    except: pass

solve_v5()

#####################################################################

