def solution(num1, num2):
    # 가장 표준적이고 직관적인 곱셈 연산
    answer = num1 * num2
    return answer

######################################################

def solution(num1, num2):
    answer = 0
    # num1을 num2번만큼 반복해서 더함
    for _ in range(num2):
        answer += num1
    return answer

######################################################

import operator

def solution(num1, num2):
    # operator.mul(a, b)는 a * b를 수행하는 표준 함수
    answer = operator.mul(num1, num2)
    return answer

######################################################

import math

def solution(num1, num2):
    # 0인 경우 로그를 취할 수 없으므로 예외 처리
    if num1 == 0 or num2 == 0:
        return 0
    
    # log(num1 * num2) = log(num1) + log(num2) 원리 이용
    # exp(log(num1) + log(num2))는 num1 * num2가 됨
    answer = round(math.exp(math.log(num1) + math.log(num2)))
    return answer

######################################################

def solution(num1, num2):
    # 기저 조건: 하나라도 0이면 곱은 0
    if num1 == 0 or num2 == 0:
        return 0
    # num2가 1이 될 때까지 num1을 더하며 재귀 호출
    if num2 == 1:
        return num1
    
    answer = num1 + solution(num1, num2 - 1)
    return answer

######################################################


