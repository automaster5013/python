def solution(n):
    # 7로 나누어 떨어지면 몫만큼, 나머지가 있으면 한 판 더 추가
    if n % 7 == 0:
        answer = n // 7
    else:
        answer = (n // 7) + 1
    return answer

################################################################

def solution(n):
    # (n-1)을 7로 나눈 몫에 1을 더해 올림 처리를 구현
    answer = (n - 1) // 7 + 1
    return answer

################################################################

import math

def solution(n):
    # n을 7로 나눈 뒤 math.ceil을 사용하여 소수점 올림 처리
    answer = math.ceil(n / 7)
    return answer

################################################################

def solution(n):
    # 음수로 나눈 몫을 구하면 내림 효과로 인해 절대값이 커짐 (올림 효과)
    # -(-15 // 7) => -(-3) => 3
    answer = -(-n // 7)
    return answer

################################################################

def solution(n):
    # quotient(몫)와 remainder(나머지)를 한 번에 계산
    quotient, remainder = divmod(n, 7)
    
    # 나머지가 0보다 크면 True(1), 아니면 False(0)가 되어 몫에 더해짐
    answer = quotient + (remainder > 0)
    return answer

################################################################





