def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            if i not in answer:
                answer.append(i)
            n //= i 
        else:
            i += 1 
            
    return answer

n1 = 12
n2 = 17
n3 = 420

print(solution(n1))
print(solution(n2))
print(solution(n3))

###########################################

def solution(n):
    answer = []
    i = 2
    while i <= n:
        while n % i == 0:
            answer.append(i) 
            n //= i
        i += 1
        
    return sorted(list(set(answer)))

n1 = 12
n2 = 17
n3 = 420

print(solution(n1))
print(solution(n2))
print(solution(n3))

###########################################




















