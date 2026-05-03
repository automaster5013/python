def solution(numbers):
    # 합계를 개수로 나누는 가장 직관적인 방식
    answer = sum(numbers) / len(numbers)
    return answer

##################################################

import statistics

def solution(numbers):
    # 통계 전문 라이브러리의 평균 함수를 호출
    answer = statistics.mean(numbers)
    return answer

##################################################

def solution(numbers):
    total = 0
    # 배열을 직접 순회하며 하나씩 더함
    for num in numbers:
        total += num
    
    answer = total / len(numbers)
    return answer

##################################################

from functools import reduce

def solution(numbers):
    # reduce를 사용하여 모든 원소를 더한 뒤 길이로 나눔
    # lambda x, y: x + y 는 누적 합을 계산하는 익명 함수
    total = reduce(lambda x, y: x + y, numbers)
    answer = total / len(numbers)
    return answer

##################################################

import numpy as np

def solution(numbers):
    # 넘파이 배열로 변환 후 mean 메서드 활용
    # 대용량 데이터 처리 시 가장 빠른 속도를 보임
    answer = np.array(numbers).mean()
    return answer

##################################################


