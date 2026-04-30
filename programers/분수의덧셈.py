def solution(denum1, num1, denum2, num2):
    answer = []    
    a = 0
    b = 0

    a = (denum1 * num2) + (denum2 * num1)
    b = num2 * num1
    for j in range(1, 1000):
        for i in range(1, 1000):
            if (a % i) == 0 and (b % i) == 0:
                a = a / i
                b = b / i

        answer = [a, b]

    return answer

    # 더 이상 약분할 수 없는 ‘단순한’ 분수(기약분수)
    # 분자와 분모가 서로소인 분수(기약분수)
#################################################(방법01)

def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    denum0 = (denum1 * num2) + (denum2 * num1)
    num0 = num1 * num2
    for i in range(min(denum0, num0), 0, -1):
        if denum0 % i == 0 and num0 % i == 0:
            s = i
            break

    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer

#################################################(방법02)

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    def get_gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    gcd = get_gcd(numer, denom)
    return [numer // gcd, denom // gcd]

#################################################(방법03)


