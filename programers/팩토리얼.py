def solution(n):
    f = 1
    i = 1
    while f * (i + 1) <= n:
        i += 1
        f *= i
    return i

################################################

def solution(n):
    f = 1
    i = 1
    while True:
        f *= (i + 1)
        if f > n:
            break
        i += 1
    return i

################################################

def solution(n):
    f = 1
    for i in range(1, 12):
        f *= i
        if f > n:
            return i - 1
        if f == n:
            return i
    return 10 

################################################










































