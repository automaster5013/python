def solution(order):
    answer = 0
    while order > 0:
        digit = order % 10
        if digit == 3 or digit == 6 or digit == 9:
            answer += 1
        order //= 10
        
    return answer

order1 = 3
order2 = 29423
order3 = 0

print(solution(order1))
print(solution(order2))
print(solution(order3))

###########################################################

def solution(order):
    s = str(order)
    return s.count('3') + s.count('6') + s.count('9')

order1 = 3
order2 = 29423
order3 = 0

print(solution(order1))
print(solution(order2))
print(solution(order3))

###########################################################

def solution(order):
    return sum(1 for char in str(order) if char in '369')

order1 = 3
order2 = 29423
order3 = 0

print(solution(order1))
print(solution(order2))
print(solution(order3))












