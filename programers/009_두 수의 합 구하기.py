def solution(num1, num2):
    # 가장 표준적이고 명확한 산술 연산
    answer = num1 + num2
    return answer

##############################################################

def solution(num1, num2):
    # 두 수를 리스트로 묶어 내장 함수 sum으로 합산
    answer = sum([num1, num2])
    return answer

##############################################################

import operator

def solution(num1, num2):
    # 더하기 연산을 수행하는 add 함수를 직접 호출
    answer = operator.add(num1, num2)
    return answer

##############################################################

def solution(num1, num2):
    # 비트 연산을 통한 가산기 로직 구현
    while num2 != 0:
        # 올림수 계산 (공통 비트 찾기)
        carry = num1 & num2
        # 올림수 제외한 합 계산
        num1 = num1 ^ num2
        # 올림수를 한 칸 왼쪽으로 이동하여 num2에 할당
        num2 = carry << 1
    
    answer = num1
    return answer

##############################################################

def solution(num1, num2):
    # 정수 객체의 내장 메서드인 __add__를 활용
    # num1 + num2의 실제 내부 동작 방식임
    answer = num1.__add__(num2)
    return answer

##############################################################






