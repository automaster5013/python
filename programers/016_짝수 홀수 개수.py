def solution(num_list):
    even_count = 0
    odd_count = 0
    for n in num_list:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    answer = [even_count, odd_count]
    return answer

########################################################

def solution(num_list):
    # 짝수 리스트와 홀수 리스트를 각각 생성하여 길이를 구함
    even_count = len([n for n in num_list if n % 2 == 0])
    odd_count = len([n for n in num_list if n % 2 != 0])
    answer = [even_count, odd_count]
    return answer

########################################################

def solution(num_list):
    # [짝수 개수, 홀수 개수]를 담을 공간 준비
    answer = [0, 0]
    for n in num_list:
        # n % 2가 0이면 answer[0] 증가, 1이면 answer[1] 증가
        answer[n % 2] += 1
    return answer

########################################################

def solution(num_list):
    # n & 1은 홀수일 때 1, 짝수일 때 0을 반환함
    odd_count = sum(n & 1 for n in num_list)
    even_count = len(num_list) - odd_count
    answer = [even_count, odd_count]
    return answer

########################################################

def solution(num_list):
    # filter를 사용하여 짝수 요소들만 걸러냄
    evens = list(filter(lambda x: x % 2 == 0, num_list))
    even_count = len(evens)
    # 전체 개수에서 짝수 개수를 빼서 홀수 개수 산출
    odd_count = len(num_list) - even_count
    
    answer = [even_count, odd_count]
    return answer

########################################################



