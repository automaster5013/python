def solution(my_string):
    # 처음부터 끝까지 -1 간격으로(역순으로) 슬라이싱
    answer = my_string[::-1]
    return answer

#########################################################

def solution(my_string):
    # reversed로 생성된 역순 문자들을 빈 문자열("")을 기준으로 합침
    answer = "".join(reversed(my_string))
    return answer

#########################################################

def solution(my_string):
    # 문자열을 리스트로 변환
    str_list = list(my_string)
    # 리스트 순서를 뒤집음 (In-place)
    str_list.reverse()
    # 리스트를 다시 문자열로 결합
    answer = "".join(str_list)
    return answer

#########################################################

import sys
sys.setrecursionlimit(2000) # 문자열 길이 제한에 따른 재귀 깊이 설정

def solution(my_string):
    # 문자열이 빈 값이나 하나라면 그대로 반환 (기본 조건)
    if len(my_string) <= 1:
        return my_string
    # 마지막 문자를 맨 앞으로 가져오고 나머지를 재귀 호출
    return my_string[-1] + solution(my_string[:-1])

#########################################################

def solution(my_string):
    answer = ""
    for char in my_string:
        # 문자를 현재까지 만든 문자열의 '앞'에 더해줌으로써 순서를 뒤집음
        answer = char + answer
    return answer

#########################################################



