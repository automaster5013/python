def solution(num1, num2):
    # 실수 나눗셈 후 1000을 곱하고 정수로 변환
    answer = int((num1 / num2) * 1000)
    return answer

#####################################################

def solution(num1, num2):
    # 미리 1000을 곱한 뒤 정수 나눗셈(//)으로 소수점 버림 처리
    answer = (num1 * 1000) // num2
    return answer

#####################################################

import math

def solution(num1, num2):
    # math.trunc를 사용하여 소수점 자리를 강제로 잘라냄
    answer = math.trunc((num1 / num2) * 1000)
    return answer

#####################################################

def solution(num1, num2):
    # 몫(quotient)과 나머지(remainder) 중 몫만 사용
    answer, _ = divmod(num1 * 1000, num2)
    return answer

#####################################################

def solution(num1, num2):
    # 비트 OR 연산자(|)를 0과 함께 쓰면 소수점 이하가 버려짐
    # (주의: 큰 수에서는 동작이 다를 수 있으나 본 문제 범위에선 유효함)
    answer = ((num1 / num2) * 1000) // 1
    # 또는 아래와 같이 표현 가능
    answer = int((num1 / num2) * 1000 // 1)
    return answer

#####################################################



