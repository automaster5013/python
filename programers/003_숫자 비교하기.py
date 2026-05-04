def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer

#################################################
def solution(num1, num2):
    # (참일 때 값) if (조건) else (거짓일 때 값)
    answer = 1 if num1 == num2 else -1
    return answer

#################################################

def solution(num1, num2):
    # num1 == num2가 참(1)이면: 1 * 2 - 1 = 1
    # num1 == num2가 거짓(0)이면: 0 * 2 - 1 = -1
    answer = (num1 == num2) * 2 - 1
    return answer

#################################################

def solution(num1, num2):
    # 인덱스 0(False)에는 -1, 인덱스 1(True)에는 1을 배치
    mapping = [-1, 1]
    answer = mapping[num1 == num2]
    return answer

#################################################

def solution(num1, num2):
    # 두 수를 set에 넣으면 중복이 제거됨
    unique_count = len({num1, num2})
    
    # 원소가 1개면 두 수는 같음(1), 2개면 다름(-1)
    answer = 1 if unique_count == 1 else -1
    return answer

#################################################



