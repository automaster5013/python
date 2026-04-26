import sys

def solve_v1():
    # 입력 받기
    try:
        line = sys.stdin.readline().split()
        if not line: return
        
        x = int(line[0])
        y = int(line[1])
        mod = 20091024
        
        # pow(base, exp, mod)는 (base^exp) % mod를 매우 빠르게 계산합니다.
        # 문제 조건대로 0^0은 1로 처리됩니다.
        print(pow(x, y, mod))
    except EOFError:
        pass

if __name__ == "__main__":
    solve_v1()

##########################################################################

import sys

def solve_v2():
    input_data = sys.stdin.readline().split()
    if not input_data: return
    
    x = int(input_data[0])
    y = int(input_data[1])
    m = 20091024
    
    if y == 0:
        print(1)
        return
        
    res = 1
    x %= m # x가 m보다 클 수 있으므로 미리 나머지 처리
    
    while y > 0:
        # 지수가 홀수라면 현재의 x를 결과에 곱함
        if y % 2 == 1:
            res = (res * x) % m
        
        # x를 제곱하고 지수를 반으로 줄임
        x = (x * x) % m
        y //= 2
        
    print(res)

solve_v2()

##########################################################################

def power_recursive(x, y, m):
    if y == 0:
        return 1
    
    # x^(y//2)를 먼저 구함 (한 번만 계산)
    half = power_recursive(x, y // 2, m)
    
    # (half * half) % m 계산
    res = (half * half) % m
    
    # 지수가 홀수였다면 x를 한 번 더 곱함
    if y % 2 == 1:
        res = (res * (x % m)) % m
        
    return res

def solve_v3():
    import sys
    line = sys.stdin.readline().split()
    if line:
        x, y = map(int, line)
        print(power_recursive(x, y, 20091024))

solve_v3()

##########################################################################

