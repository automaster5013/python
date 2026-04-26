def solve_v1():
    try:
        # 입력받은 2진수 문자열의 공백을 제거
        binary_str = input().strip()
        if not binary_str: return
        
        # 2진수 문자열을 10진수 정수로 즉시 변환
        decimal_num = int(binary_str, 2)
        print(decimal_num)
    except EOFError:
        pass

solve_v1()

###############################################################

def solve_v2():
    try:
        binary_str = input().strip()
        decimal = 0
        for digit in binary_str:
            # 기존 값에 2를 곱해 자릿수를 올리고 현재 비트를 더함
            decimal = decimal * 2 + int(digit)
        print(decimal)
    except:
        pass

solve_v2()

###############################################################

def solve_v3():
    try:
        binary_str = input().strip()
        length = len(binary_str)
        total = 0
        
        for i in range(length):
            # i번째 글자가 '1'이면 해당 자릿수(2의 거듭제곱)를 더함
            if binary_str[i] == '1':
                # 자릿수는 뒤에서부터 0, 1, 2... 순서임
                power = length - 1 - i
                total += 2 ** power
        print(total)
    except:
        pass

solve_v3()

###############################################################

def solve_v4():
    try:
        s = input().strip()
        ans = 0
        for bit in s:
            # 비트를 왼쪽으로 1칸 밀고(2 곱하기와 동일), 현재 비트와 OR 연산
            ans = (ans << 1) | int(bit)
        print(ans)
    except:
        pass

solve_v4()

###############################################################

def solve_v5():
    try:
        b = input().strip()
        # 뒤집어서 인덱스(i)를 곧 2의 지수로 활용
        # 예: '101' -> '1', '0', '1' -> (1*2^0) + (0*2^1) + (1*2^2)
        res = sum(int(digit) * (2 ** i) for i, digit in enumerate(reversed(b)))
        print(res)
    except:
        pass

solve_v5()

###############################################################


