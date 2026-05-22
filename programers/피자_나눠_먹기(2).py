def solution(n):
    pizza = 1
    while (pizza * 6) % n != 0:
        pizza += 1
        
    return pizza

n1 = 6
n2 = 10
n3 = 4

print(solution(n1))
print(solution(n2))
print(solution(n3))

################################################################

def solution(n):
    pizza = [i for i in range(1, n + 1) if (i * 6) % n == 0]
    return min(pizza)

n1 = 6
n2 = 10
n3 = 4

print(solution(n1))
print(solution(n2))
print(solution(n3))

################################################################

def solution(n):
    def find_pizza(pieces):
        if pieces % n == 0:
            return pieces // 6
        return find_pizza(pieces + 6)
        
    return find_pizza(6)

n1 = 6
n2 = 10
n3 = 4

print(solution(n1))
print(solution(n2))
print(solution(n3))

################################################################

def solution(n):
    # 6과 n의 최대공약수(GCD) 구하기 (유클리드 호제법)
    a, b = 6, n
    while b != 0:
        a, b = b, a % b
    gcd = a
    
    # 최소공배수(LCM) = (6 * n) // gcd
    # 구하고자 하는 피자 판 수 = 최소공배수 // 6
    # 결국 (6 * n) // gcd // 6 이므로 'n // gcd'
    return n // gcd

n1 = 6
n2 = 10
n3 = 4

print(solution(n1))
print(solution(n2))
print(solution(n3))

################################################################
















































