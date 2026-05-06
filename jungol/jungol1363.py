import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    curr = 1
    for _ in range(T):
        K = int(input_data[curr])
        a = int(input_data[curr+1])
        b = int(input_data[curr+2])
        curr += 3
        
        # 기약분수 체크
        if gcd(a, b) != 1:
            print("Error")
            continue
            
        # 앞의 분수 p/q 구하기 (aq - bp = 1)
        # b(-p) + a(q) = 1 형태에서 확장 유클리드 적용
        g, p_inv, q0 = extended_gcd(b, a)
        # q = q0 + k*b, q <= K 인 최대 q 찾기
        k = (K - q0) // b
        q = q0 + k * b
        p = (a * q - 1) // b
        
        ans_prev = f"{p}/{q}" if q > 0 and p > 0 else "None"
        
        # 뒤의 분수 r/s 구하기 (br - as = 1)
        # a(-s) + b(r) = 1 형태
        g, s_inv, r0 = extended_gcd(a, b)
        # s = s0 + k*b, s <= K 인 최대 s 찾기
        k = (K - s_inv) // b # 여기서 s_inv는 음수일 수 있으므로 조정 필요
        # s = -s_inv 이므로 as - br = -1 => br - as = 1 활용
        
        # 더 간단한 방법: p/q를 알면 r/s = (a*(floor((K+q)/b))-p) / (b*(floor((K+q)/b))-q)
        # 하지만 독립적으로 계산:
        g, x, y = extended_gcd(a, b)
        # ax - by = 1  => b(K-y) - a(K-x) 관련 성질 이용
        # br - as = 1 만족하는 s 구하기
        # a(-s) + br = 1 => x = -s, y = r
        s0 = -x
        k_s = (K - s0) // b
        s = s0 + k_s * b
        r = (a * s + 1) // b
        
        ans_next = f"{r}/{s}" if s <= K and r < s else "None"
        
        print(f"{ans_prev} {ans_next}")

if __name__ == "__main__":
    solve()

#############################################################################################



