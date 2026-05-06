def solution(num_list, n):
    answer = 0
    answer = 1 if num_list.count(n) > 0 else 0
    return answer

#################################################(방법01)

def solution(num_list, n):
    return int(n in num_list)

#################################################(방법02)


def solution(num_list, n):
    if n in num_list: return 1
    return 0

#################################################(방법03)

def solution(num_list, n):
    answer = 0
    if n in num_list:
        answer = 1
    else:
        answer = 0
    return answer

#################################################(방법04)

def solution(num_list, n):
    return [0,1][n in num_list]

#################################################(방법05)

def solution(num_list, n):
    answer = 0
    for i in num_list:
        if n == int(i):
            answer = 1
    return answer

#################################################(방법06)


