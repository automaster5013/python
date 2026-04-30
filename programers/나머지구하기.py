
def solution(num1, num2):
    # answer = -1
    return num1 % num2

#####################################(방법01)

def solution(num1, num2):
    while num1 >= num2:
        num1 -= num2
    return num1

#####################################(방법02)

def solution(num1, num2):
    return divmod(num1, num2)[1]

#####################################(방법03)

def solution(num1, num2):
    answer = num1 % num2
    return answer

#####################################(방법04)

