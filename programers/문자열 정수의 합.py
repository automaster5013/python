def solution(num_str):
    answer = 0
    for char in num_str:
        answer += int(char)
    return answer

##################################(방법01)

def solution(num_str):
    answer = 0
    for char in num_str:
        answer += ord(char) - ord('0')
    return answer

##################################(방법02)

def solution(num_str):
    if not num_str:
        return 0
    return int(num_str[0]) + solution(num_str[1:])

##################################(방법03)

def solution(num_str):
    answer = sum([int(char) for char in num_str])
    return answer

##################################(방법04)

def solution(num_str):
    answer = 0
    stack = [int(char) for char in num_str]
    
    while stack:
        answer += stack.pop()
        
    return answer

##################################(방법05)





