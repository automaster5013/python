def solution(array, height):
    answer = 0
    for h in array:
        if h > height:
            answer += 1
    return answer

############################################################

def solution(array, height):
    # height보다 큰 값들만 리스트로 필터링하여 길이를 반환
    answer = len([h for h in array if h > height])
    return answer

############################################################

def solution(array, height):
    # 각 요소가 height보다 큰지 확인(True/False)하고 이들의 합을 구함
    answer = sum(1 for h in array if h > height)
    # 또는 더 간결하게: sum(h > height for h in array)
    return answer

############################################################

def solution(array, height):
    # lambda 식을 사용하여 기준보다 큰 요소만 추출한 뒤 리스트화하여 개수를 셈
    filtered_list = list(filter(lambda x: x > height, array))
    answer = len(filtered_list)
    return answer

############################################################

def solution(array, height):
    # 머쓱이의 키를 배열에 추가하고 오름차순 정렬
    # [120, 140, 180, 190] 형태에서 190의 위치를 찾는 방식
    temp_array = array + [height]
    temp_array.sort()
    
    # 정렬된 배열에서 height가 마지막으로 나타나는 인덱스를 활용
    # 전체 길이에서 (height의 위치 + 1)을 빼면 더 큰 사람의 수가 나옴
    # 중복값이 있을 수 있으므로 뒤에서부터 찾는 로직이 안전함
    temp_array.sort(reverse=True)
    answer = temp_array.index(height)
    return answer

############################################################





