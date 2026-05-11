def solution(num_str):
    answer = 0
    for char in num_str:
        answer += int(char)
    return answer

##################################(방법01)

def solution(num_str):
    answer = 0
    for char in num_str:
        answer += ord(char) - ord('0')
    return answer

##################################(방법02)

def solution(num_str):
    if not num_str:
        return 0
    return int(num_str[0]) + solution(num_str[1:])

##################################(방법03)

def solution(num_str):
    answer = sum([int(char) for char in num_str])
    return answer

##################################(방법04)

def solution(num_str):
    answer = 0
    stack = [int(char) for char in num_str]
    
    while stack:
        answer += stack.pop()
        
    return answer

##################################(방법05)

def solution(num_str):
    answer = 0
    for char in num_str:
        answer += int(char)
    return answer

##################################(방법06)

def solution(num_str):
    answer = 0
    for char in num_str:
        # '1'의 아스키 값에서 '0'의 아스키 값을 빼면 숫자 1이 됩니다.
        answer += ord(char) - ord('0')
    return answer

##################################(방법07)

def solution(num_str):
    # 더 이상 더할 숫자가 없으면 0을 반환 (종료 조건)
    if not num_str:
        return 0
    # 첫 번째 숫자 + (나머지 문자열을 다시 함수에 넣은 결과)
    return int(num_str[0]) + solution(num_str[1:])

##################################(방법08)

def solution(num_str):
    # 문자열의 각 문자를 정수로 바꾼 리스트를 생성 후 sum으로 합산
    answer = sum([int(char) for char in num_str])
    return answer

##################################(방법09)

def solution(num_str):
    answer = 0
    # 문자열을 각 글자가 담긴 리스트로 변환
    stack = [int(char) for char in num_str]
    
    while stack:
        # 리스트의 마지막 요소를 꺼내어 합산
        answer += stack.pop()
        
    return answer

##################################(방법10)


