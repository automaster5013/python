def solve_v1():
    try:
        line = input().split()
        if not line: return
        n, b = map(int, line)
        
        # 16진수까지 대응하는 변환 문자열
        chars = "0123456789ABCDEF"
        result = []
        
        if n == 0:
            print(0); return
            
        while n > 0:
            # 진수로 나눈 나머지를 결과에 추가
            result.append(chars[n % b])
            # 몫을 다음 연산에 사용
            n //= b
            
        # 역순으로 저장되었으므로 뒤집어서 출력
        print("".join(result[::-1]))
    except: pass

solve_v1()

#################################################################

def solve_v2():
    try:
        n, b = map(int, input().split())
        
        if b == 2:
            print(bin(n)[2:])
        elif b == 8:
            print(oct(n)[2:])
        elif b == 16:
            # hex()는 소문자로 나오므로 upper() 사용
            print(hex(n)[2:].upper())
    except: pass

solve_v2()

#################################################################

def convert(n, b, chars):
    if n < b:
        return chars[n]
    else:
        # n을 b로 나눈 몫을 재귀 호출 + 현재 나머지
        return convert(n // b, b, chars) + chars[n % b]

def solve_v3():
    try:
        n, b = map(int, input().split())
        chars = "0123456789ABCDEF"
        print(convert(n, b, chars))
    except: pass

solve_v3()

#################################################################

def solve_v4():
    try:
        n, b = map(int, input().split())
        chars = "0123456789ABCDEF"
        ans = ""
        
        if n == 0:
            print(0); return
            
        while n:
            # 몫(n)과 나머지(rem)를 동시에 얻음
            n, rem = divmod(n, b)
            ans = chars[rem] + ans # 앞에 붙여서 뒤집기 생략
            
        print(ans)
    except: pass

solve_v4()

#################################################################

def solve_v5():
    try:
        line = input().split()
        if len(line) < 2: return
        n, b = int(line[0]), int(line[1])
        
        chars = "0123456789ABCDEF"
        stack = []
        
        while n > 0:
            stack.append(chars[n % b])
            n //= b
            
        # 스택이 빌 때까지 하나씩 꺼내기 (pop)
        while stack:
            print(stack.pop(), end="")
        print()
    except: pass

solve_v5()

#################################################################


