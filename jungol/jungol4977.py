def solve_v1():
    try:
        n = float(input())
        # 1. 정수 부분 변환
        int_part = int(n)
        bin_int = bin(int_part)[2:]
        
        # 2. 소수 부분 변환 (4자리까지)
        frac_part = n - int_part
        bin_frac = ""
        
        for _ in range(4):
            frac_part *= 2
            bit = int(frac_part)
            bin_frac += str(bit)
            frac_part -= bit
            
        print(f"{bin_int}.{bin_frac}")
    except: pass

solve_v1()

##################################################################

def solve_v2():
    try:
        n = float(input())
        # 소수점 4자리까지 구해야 하므로 2^4인 16을 곱함
        # '내림' 처리를 위해 int()로 소수점 이하를 버림
        scaled_int = int(n * 16)
        bin_str = bin(scaled_int)[2:]
        
        # 전체 이진수 문자열에서 뒤의 4자리를 소수점으로 분리
        # 자릿수가 부족할 경우를 대비해 앞을 0으로 채움 (zfill)
        bin_str = bin_str.zfill(5) 
        print(f"{bin_str[:-4]}.{bin_str[-4:]}")
    except: pass

solve_v2()

##################################################################

def solve_v3():
    n = float(input())
    
    # 정수 부분
    res_int = bin(int(n))[2:]
    
    # 소수 부분
    frac = n - int(n)
    res_frac = []
    
    for _ in range(4):
        # 2를 곱한 뒤 몫(비트)과 나머지(다음 소수)를 분리
        bit, frac = divmod(frac * 2, 1)
        res_frac.append(str(int(bit)))
        
    print(res_int + "." + "".join(res_frac))

solve_v3()

##################################################################

def solve_v4():
    n = float(input())
    
    def get_frac_bits(f, count):
        for _ in range(count):
            f *= 2
            yield str(int(f))
            f %= 1
            
    integer_part = bin(int(n))[2:]
    fraction_part = "".join(get_frac_bits(n % 1, 4))
    
    print(f"{integer_part}.{fraction_part}")

solve_v4()

##################################################################

def solve_v5():
    try:
        data = input().split('.')
        int_val = int(data[0])
        # 소수점이 없는 경우를 위해 0.0 처리
        frac_val = float("0." + data[1]) if len(data) > 1 else 0.0
        
        # 정수부 이진수
        res = bin(int_val)[2:] + "."
        
        # 소수부 4자리 채우기
        for _ in range(4):
            frac_val *= 2
            if frac_val >= 1:
                res += "1"
                frac_val -= 1
            else:
                res += "0"
        print(res)
    except: pass

solve_v5()

##################################################################

