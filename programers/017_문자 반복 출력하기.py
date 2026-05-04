def solution(my_string, n):
    answer = ''
    for char in my_string:
        # 각 문자에 n을 곱하여 반복된 문자열을 생성 후 합산
        answer += char * n
    return answer

###############################################################

def solution(my_string, n):
    # 각 문자를 n번 반복한 리스트 생성 후 빈 문자열로 연결
    answer = "".join([char * n for char in my_string])
    return answer

###############################################################

def solution(my_string, n):
    # 모든 요소에 n을 곱하는 익명 함수(lambda) 적용
    answer = "".join(map(lambda x: x * n, my_string))
    return answer

###############################################################

def solution(my_string, n):
    answer = ''
    for char in my_string:
        # 내측 반복문에서 n번만큼 문자를 추가
        for _ in range(n):
            answer += char
    return answer

###############################################################

def solution(my_string, n):
    # 기저 조건: 문자열이 비어있으면 빈 문자열 반환
    if not my_string:
        return ""
    
    # 첫 번째 문자 반복 + 나머지 문자열에 대한 재귀 호출
    answer = (my_string[0] * n) + solution(my_string[1:], n)
    return answer

###############################################################



