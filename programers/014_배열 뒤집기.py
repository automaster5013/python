def solution(num_list):
    # 슬라이싱 [start:stop:step]에서 step을 -1로 설정하여 뒤집기
    answer = num_list[::-1]
    return answer

################################################################

def solution(num_list):
    # 원본 리스트의 순서를 직접 바꾼 뒤 반환
    num_list.reverse()
    answer = num_list
    return answer

################################################################

def solution(num_list):
    # 역순 이터레이터를 생성하고 다시 리스트로 변환
    answer = list(reversed(num_list))
    return answer

################################################################

def solution(num_list):
    answer = []
    # 원본 리스트 복사본에서 뒤에서부터 하나씩 꺼내어 추가
    temp = num_list[:]
    while temp:
        answer.append(temp.pop())
    return answer

################################################################

def solution(num_list):
    answer = []
    # 리스트의 길이(n)를 구한 뒤 n-1 인덱스부터 0까지 역순 순회
    n = len(num_list)
    for i in range(n - 1, -1, -1):
        answer.append(num_list[i])
    return answer

################################################################



