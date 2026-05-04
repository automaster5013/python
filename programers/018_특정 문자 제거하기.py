def solution(my_string, letter):
    # 특정 문자를 모두 찾아 빈 문자열로 교체(제거)
    answer = my_string.replace(letter, '')
    return answer

######################################################

def solution(my_string, letter):
    # letter와 일치하지 않는 문자들만 모아서 다시 결합
    answer = "".join([char for char in my_string if char != letter])
    return answer

######################################################

def solution(my_string, letter):
    # letter를 기준으로 나누면 letter가 사라진 리스트가 생성됨
    parts = my_string.split(letter)
    # 쪼개진 부분들을 공백 없이 다시 붙임
    answer = "".join(parts)
    return answer

######################################################

def solution(my_string, letter):
    # lambda를 사용하여 letter와 다른 문자만 걸러내도록 필터링
    filtered_chars = filter(lambda x: x != letter, my_string)
    answer = "".join(filtered_chars)
    return answer

######################################################

def solution(my_string, letter):
    answer = ''
    for char in my_string:
        # 현재 문자가 제거할 문자가 아닐 때만 결과에 추가
        if char != letter:
            answer += char
    return answer

######################################################



