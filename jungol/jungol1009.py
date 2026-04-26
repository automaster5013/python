def solve_v1():
    while True:
        try:
            line = input().split()
            if not line: continue
            
            for word in line:
                n_str = word
                if n_str == '0': return # 종료 조건
                
                # 1. 역순 계산: 문자열 뒤집기 후 정수 변환 (앞의 0 제거)
                reversed_n = int(n_str[::-1])
                
                # 2. 각 자리 합 계산
                digit_sum = sum(int(digit) for digit in n_str)
                
                print(f"{reversed_n} {digit_sum}")
        except EOFError:
            break

solve_v1()

###########################################################################

def solve_v2():
    while True:
        n = int(input())
        if n == 0: break
        
        temp = n
        reversed_num = 0
        digit_sum = 0
        
        while temp > 0:
            digit = temp % 10
            # 역순 숫자 빌드: 기존 숫자에 10을 곱하고 새 숫자를 더함
            reversed_num = reversed_num * 10 + digit
            # 자리수 합 누적
            digit_sum += digit
            temp //= 10
            
        print(reversed_num, digit_sum)

solve_v2()

###########################################################################

def get_sum(n):
    if n < 10: return n
    return n % 10 + get_sum(n // 10)

def get_reverse(n, res):
    if n == 0: return res
    return get_reverse(n // 10, res * 10 + n % 10)

def solve_v3():
    while True:
        num = int(input())
        if num == 0: break
        print(get_reverse(num, 0), get_sum(num))

solve_v3()

###########################################################################

def solve_v4():
    while True:
        s = input().strip()
        if s == '0': break
        
        # map을 이용해 각 문자를 정수로 변환한 리스트 생성
        digits = list(map(int, s))
        
        # 뒤집기는 문자열로 처리 후 int 변환
        rev = int(s[::-1])
        # 합계는 sum 함수 활용
        total = sum(digits)
        
        print(f"{rev} {total}")

solve_v4()

###########################################################################

def solve_v5():
    while True:
        s = input().strip()
        if s == '0': break
        
        stack = list(s) # 각 자릿수를 리스트(스택)에 저장
        
        digit_sum = 0
        rev_str = ""
        
        # 스택이 빌 때까지 뒤에서부터 꺼내기
        while stack:
            char = stack.pop()
            rev_str += char
            digit_sum += int(char)
            
        # int()로 감싸서 유효하지 않은 '0' 제거
        print(int(rev_str), digit_sum)

solve_v5()

###########################################################################

