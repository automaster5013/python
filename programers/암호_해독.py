def solution(cipher, code):
    return cipher[code - 1 : : code]
    
a1, b1 = "dfjardstddetckdaccccdegk", 4
a2, b2 = "pfqallllabwaoclk", 2

print(solution(a1, b1))
print(solution(a2, b2))

########################################

def solution(cipher, code):
    answer = ''
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
        
    return answer

a1, b1 = "dfjardstddetckdaccccdegk", 4
a2, b2 = "pfqallllabwaoclk", 2

print(solution(a1, b1))
print(solution(a2, b2))

########################################

def solution(cipher, code):
    answer = []
    for idx, char in enumerate(cipher):
        if (idx + 1) % code == 0:
            answer.append(char)
            
    return "".join(answer)


a1, b1 = "dfjardstddetckdaccccdegk", 4
a2, b2 = "pfqallllabwaoclk", 2

print(solution(a1, b1))
print(solution(a2, b2))

########################################

def solution(cipher, code):
    answer = ''
    i = code - 1
    while i < len(cipher):
        answer += cipher[i]
        i += code 
        
    return answer

a1, b1 = "dfjardstddetckdaccccdegk", 4
a2, b2 = "pfqallllabwaoclk", 2

print(solution(a1, b1))
print(solution(a2, b2))

########################################

def solution(cipher, code):
    return "".join([cipher[i] for i in range(code - 1, len(cipher), code)])

a1, b1 = "dfjardstddetckdaccccdegk", 4
a2, b2 = "pfqallllabwaoclk", 2

print(solution(a1, b1))
print(solution(a2, b2))

########################################


































