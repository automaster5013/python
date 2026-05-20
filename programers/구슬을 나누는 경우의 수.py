def solution(balls, share):
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    return factorial(balls) // (factorial(share) * factorial(balls - share))


a1, b1 = 3, 2
a2, b2 = 5, 3

print(solution(a1, b1))
print(solution(a2, b2))

#############################################################

def solution(balls, share):
    numerator = 1   
    denominator = 1 
    
    for i in range(share):
        numerator *= (balls - i)
        denominator *= (i + 1)
        
    return numerator // denominator

a1, b1 = 3, 2
a2, b2 = 5, 3

print(solution(a1, b1))
print(solution(a2, b2))

#############################################################















