def solution(numbers, num1, num2):
    # num2 인덱스까지 포함하기 위해 num2 + 1을 끝점으로 설정
    answer = numbers[num1:num2 + 1]
    return answer

#################################################################

def solution(numbers, num1, num2):
    answer = []
    # num1부터 num2까지의 인덱스를 직접 순회
    for i in range(num1, num2 + 1):
        answer.append(numbers[i])
    return answer

#################################################################

def solution(numbers, num1, num2):
    # 인덱스 i가 num1과 num2 사이에 있는 요소들로 리스트 생성
    answer = [numbers[i] for i in range(num1, num2 + 1)]
    return answer

#################################################################

def solution(numbers, num1, num2):
    # 인덱스(i)가 num1 이상 num2 이하인 값(v)만 필터링
    answer = [v for i, v in enumerate(numbers) if num1 <= i <= num2]
    return answer

#################################################################

def solution(numbers, num1, num2):
    # 원본 보호를 위해 복사본 생성
    answer = numbers[:]
    
    # 뒷부분 먼저 삭제 (인덱스 밀림 방지)
    del answer[num2 + 1:]
    # 앞부분 삭제
    del answer[:num1]
    
    return answer

#################################################################



