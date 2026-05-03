def solution(slice, n):
    # 나머지가 있으면 한 판을 더하고, 없으면 몫만 반환
    if n % slice == 0:
        answer = n // slice
    else:
        answer = (n // slice) + 1
    return answer

########################################################

def solution(slice, n):
    # (n - 1) // slice + 1 공식은 정수 나눗셈에서 올림(ceil)과 동일함
    answer = (n - 1) // slice + 1
    return answer

########################################################

import math

def solution(slice, n):
    # n을 slice로 나눈 실수 값을 올림 처리
    answer = math.ceil(n / slice)
    return answer

########################################################

def solution(slice, n):
    # 음수 나눗셈 결과를 다시 양수로 바꾸어 올림 효과를 얻음
    # 예: -(-10 // 7) -> -(-2) -> 2
    answer = -(-n // slice)
    return answer

########################################################

def solution(slice, n):
    answer = 1
    # 총 조각 수(slice * answer)가 사람 수(n)보다 작을 때까지 판 수를 늘림
    while (slice * answer) < n:
        answer += 1
    return answer

########################################################





