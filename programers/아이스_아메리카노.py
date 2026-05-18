def solution(money):
    cups = money // 5500
    change = money % 5500
    
    return [cups, change]

n1 = 5500
n2 = 15000

print(solution(n1))
print(solution(n2))

#########################################

def solution(money):
    return list(divmod(money, 5500))

n1 = 5500
n2 = 15000

print(solution(n1))
print(solution(n2))

#########################################

def solution(money):
    cups = 0
    while money >= 5500:
        money -= 5500
        cups += 1
    return [cups, money]

n1 = 5500
n2 = 15000

print(solution(n1))
print(solution(n2))

#########################################

def solution(money):
    cups = money // 5500
    change = money - (cups * 5500)

    return [cups, change]

n1 = 5500
n2 = 15000

print(solution(n1))
print(solution(n2))

########################################

def solution(money):
    if money < 5500:
        return [0, money]

    result = solution(money - 5500)
    return [result[0] + 1, result[1]]

n1 = 5500
n2 = 15000

print(solution(n1))
print(solution(n2))

########################################














