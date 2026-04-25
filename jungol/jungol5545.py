# 입력: P(도색 성공 주기), V(광택 성공 주기), K(전체 개수)
p, v, k = map(int, input().split())

# 실패 주기는 성공 횟수 + 1
fail_p = p + 1
fail_v = v + 1

# 최대공약수(GCD) 구하기 (유클리드 호제법)
a, b = fail_p, fail_v
while b:
    a, b = b, a % b
gcd = a

# 최소공배수(LCM) 구하기: (x * y) / GCD
lcm = (fail_p * fail_v) // gcd

# 1. 도색 실패 총 개수 (D + B)
total_fail_p = k // fail_p
# 2. 광택 실패 총 개수 (C + B)
total_fail_v = k // fail_v
# 3. 둘 다 실패한 연필 (B)
b_count = k // lcm

# 4. 각 영역 계산
d_count = total_fail_p - b_count  # 도색 실패 & 광택 성공
c_count = total_fail_v - b_count  # 광택 실패 & 도색 성공
a_count = k - (total_fail_p + total_fail_v - b_count) # 전체 - (적어도 하나 실패)

print(a_count, b_count, c_count, d_count)

####################################################################################

p, v, k = map(int, input().split())
fp, fv = p + 1, v + 1

# GCD를 이용한 LCM 도출
a, b = fp, fv
while b: a, b = b, a % b
lcm = (fp * fv) // a

# 한 주기(LCM) 내에서의 개수 계산 함수
def get_counts(limit):
    if limit <= 0: return 0, 0, 0, 0
    fb = limit // lcm
    fp_total = limit // fp
    fv_total = limit // fv
    
    b = fb
    c = fv_total - b
    d = fp_total - b
    a = limit - (fp_total + fv_total - b)
    return a, b, c, d

# 전체 몫과 나머지로 최종 결과 조립
q, r = divmod(k, lcm)
a1, b1, c1, d1 = get_counts(lcm)
a2, b2, c2, d2 = get_counts(r)

print(a1*q + a2, b1*q + b2, c1*q + c2, d1*q + d2)

####################################################################################

P, V, K = map(int, input().split())
PaintFailStep, PolishFailStep = P + 1, V + 1

# LCM 계산
x, y = PaintFailStep, PolishFailStep
while y: x, y = y, x % y
BothFailStep = (PaintFailStep * PolishFailStep) // x

# 실패 건수 측정
FailBoth = K // BothFailStep
FailPaint = K // PaintFailStep
FailPolish = K // PolishFailStep

# 문제에서 요구하는 4가지 카테고리 정의
B = FailBoth                                # 도색X, 광택X (교집합)
C = FailPolish - FailBoth                   # 도색O, 광택X (광택실패 차집합)
D = FailPaint - FailBoth                    # 광택O, 도색X (도색실패 차집합)
A = K - (FailPaint + FailPolish - FailBoth) # 도색O, 광택O (여집합)

print(A, B, C, D)

####################################################################################

def solve():
    P, V, K = map(int, input().split())
    
    # 내부 함수로 GCD 정의
    def get_gcd(a, b):
        return a if b == 0 else get_gcd(b, a % b)
    
    fP, fV = P + 1, V + 1
    fBoth = (fP * fV) // get_gcd(fP, fV)
    
    # 헬퍼 함수: 특정 주기의 실패 횟수 반환
    count_fail = lambda period: K // period
    
    b = count_fail(fBoth)
    d = count_fail(fP) - b
    c = count_fail(fV) - b
    a = K - (count_fail(fP) + count_fail(fV) - b)
    
    print(f"{a} {b} {c} {d}")

solve()

####################################################################################

p, v, k = map(int, input().split())
p_cycle, v_cycle = p + 1, v + 1

# 최소공배수(LCM) 수동 계산
m, n = p_cycle, v_cycle
while n: m, n = n, m % n
lcm = (p_cycle * v_cycle) // m

# 단계별 계산
both_fail = k // lcm      # [B]
only_p_fail = k // p_cycle - both_fail # [D]
only_v_fail = k // v_cycle - both_fail # [C]

# 적어도 하나의 공정에서 실패한 연필들의 합
any_fail = both_fail + only_p_fail + only_v_fail

# 둘 다 성공한 연필 [A]
both_pass = k - any_fail

print(both_pass, both_fail, only_v_fail, only_p_fail)

####################################################################################


