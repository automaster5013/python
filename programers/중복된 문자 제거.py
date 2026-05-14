def solution(my_string):
    answer = ''
    for char in my_string:
        if char not in answer:
            answer += char
    return answer

###################################################

def solution(my_string):
    char_dict = {}
    for char in my_string:
        char_dict[char] = 0
    
    return "".join(char_dict.keys())

###################################################























































def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string.find(my_string[i]) == i:
            answer += my_string[i]
    return answer

###################################################

