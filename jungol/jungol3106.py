def to_base_b(n, b):
    if n == 0: return "0"
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, rem = divmod(n, b)
        res += chars[rem]
    return res[::-1]

def solve_v1():
    while True:
        try:
            line = input().split()
            if not line or line[0] == '0': break
            
            a, s, b = int(line[0]), line[1], int(line[2])
            
            # 1. A진법 S를 10진수로 변환
            decimal_val = int(s, a)
            
            # 2. 10진수를 B진법으로 변환하여 출력
            print(to_base_b(decimal_val, b))
        except EOFError:
            break

solve_v1()

##################################################################

def solve_v2():
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        line = input().split()
        if not line or line[0] == '0': break
        a, s, b = int(line[0]), line[1], int(line[2])
        
        # A진법 -> 10진수 (Horner's Method)
        dec = 0
        for char in s:
            val = chars.find(char.upper())
            dec = dec * a + val
            
        # 10진수 -> B진법
        if dec == 0: print(0); continue
        res = ""
        while dec > 0:
            res = chars[dec % b] + res
            dec //= b
        print(res)

solve_v2()

##################################################################

def convert(n, b, mapping):
    if n < b: return mapping[n]
    return convert(n // b, b, mapping) + mapping[n % b]

def solve_v3():
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        data = input().split()
        if not data or data[0] == '0': break
        a, s, b = int(data[0]), data[1], int(data[2])
        
        dec = int(s, a)
        print(convert(dec, b, mapping))

solve_v3()

##################################################################

def solve_v4():
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    to_val = {c: i for i, c in enumerate(digits)}
    
    while True:
        try:
            raw = input().split()
            if not raw or raw[0] == '0': break
            a, s, b = int(raw[0]), raw[1].upper(), int(raw[2])
            
            # Base A -> Decimal
            dec = 0
            for char in s:
                dec = dec * a + to_val[char]
                
            # Decimal -> Base B
            if dec == 0: print(0); continue
            res = []
            while dec:
                dec, rem = divmod(dec, b)
                res.append(digits[rem])
            print("".join(reversed(res)))
        except: break

solve_v4()

##################################################################

def solve_v5():
    m = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        li = input().split()
        if not li or li[0] == '0': break
        a, s, b = int(li[0]), li[1], int(li[2])
        
        n = int(s, a)
        res = ""
        while n:
            res = m[n % b] + res
            n //= b
        print(res if res else "0")

solve_v5()

##################################################################


