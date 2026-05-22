def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer += char * n
        
    return answer

print(solution("hello", 3))

#############################################################

def solution(my_string, n):
    if not my_string:
        return ""
    
    return (my_string[0] * n) + solution(my_string[1:], n)

print(solution("hello", 3))

#############################################################











































