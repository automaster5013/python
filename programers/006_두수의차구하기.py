def solution(num1, num2):
    # 가장 기본이 되는 산술 연산자 활용
    answer = num1 - num2
    return answer

###############################################

def solution(num1, num2):
    # num2의 부호를 반전시켜 num1과 합산
    numbers = [num1, -num2]
    answer = sum(numbers)
    return answer

###############################################

import operator

def solution(num1, num2):
    # operator.sub(a, b) 함수는 a - b를 수행함
    answer = operator.sub(num1, num2)
    return answer

###############################################

def solution(num1, num2):
    # 비트 반전(NOT) 후 1을 더해 음수를 만들고 num1과 더함
    # 뺄셈 기호 없이 뺄셈을 구현하는 창의적 방식
    answer = num1 + (~num2 + 1)
    return answer

###############################################

def solution(num1, num2):
    # 정수 클래스 내부에 정의된 뺄셈 메서드를 직접 호출
    answer = num1.__sub__(num2)
    return answer

###############################################



