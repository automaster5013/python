def solution(num_list):

    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1

    return answer

##########################################################

def solution(num_list):
    even_num = len([n for n in num_list if n % 2 == 0])
    odd_num = len([n for n in num_list if n % 2 != 0])
    answer = [even_num, odd_num]
    return answer

##########################################################

def solution(num_list):
    even_num = 0
    odd_num = 0
    for n in num_list:
        if n % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
    answer = [even_num, odd_num]
    return answer

##########################################################











