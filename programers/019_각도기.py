def solution(angle):
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    else:  # angle == 180
        answer = 4
    return answer

####################################################################################

def solution(angle):
    # 각 조건이 참일 때마다 1씩 더해짐
    # 예각: [True, False, False, False] -> 1
    # 직각: [True, True, False, False] -> 2
    # 둔각: [True, True, True, False] -> 3
    # 평각: [True, True, True, True] -> 4
    conditions = [angle > 0, angle >= 90, angle > 90, angle >= 180]
    answer = sum(conditions)
    return answer

####################################################################################

def solution(angle):
    # 경계값들: 0보다 큰가, 90도인가, 90보다 큰가, 180도인가
    # 조건에 맞는 요소들만 남겨 리스트 길이를 반환
    answer = len([x for x in [0, 90, 91, 180] if angle >= x])
    return answer

####################################################################################

def solution(angle):
    # 특정 케이스를 우선 처리하고, 조건식을 키로 사용하는 매핑 방식
    mapping = {angle < 90: 1, angle == 90: 2, angle < 180: 3, angle == 180: 4}
    # 딕셔너리는 뒤에 오는 값이 덮어쓰므로 순서에 유의 (여기서는 순차 검색 활용)
    for condition, result in mapping.items():
        if condition:
            return result

####################################################################################

def solution(angle):
    # (angle // 90)과 (angle % 90 == 0)의 조합을 활용
    # angle=70 -> (0*2) + (0) + 1 = 1
    # angle=90 -> (1*2) + (1) - 1 = 2 (※90도는 특수 보정 필요)
    # 논리 연산의 결과를 정수형으로 변환하여 가중치를 줌
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1 + (angle == 180) * 1
    # 위 수식은 복잡하므로 아래와 같이 논리합으로 더 간단히 표현 가능
    answer = 1 + (angle >= 90) + (angle > 90) + (angle >= 180)
    return answer

####################################################################################



