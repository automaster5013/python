def solution(dots):
    # 점들을 변수로 할당 (가독성 향상)
    [a, b, c, d] = dots
    
    # 기울기를 구하는 중복 로직을 함수로 정의
    def get_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    # 케이스 1: (A, B)와 (C, D)
    if get_slope(a, b) == get_slope(c, d): return 1
    # 케이스 2: (A, C)와 (B, D)
    if get_slope(a, c) == get_slope(b, d): return 1
    # 케이스 3: (A, D)와 (B, C)
    if get_slope(a, d) == get_slope(b, c): return 1
    
    return 0

#######################################################(방법01)

def solution(dots):
    # 3가지 조합에 대해 (y차이1 * x차이2) == (y차이2 * x차이1) 확인
    cases = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]
    
    for p1, p2, p3, p4 in cases:
        dy1 = dots[p1][1] - dots[p2][1]
        dx1 = dots[p1][0] - dots[p2][0]
        dy2 = dots[p3][1] - dots[p4][1]
        dx2 = dots[p3][0] - dots[p4][0]
        
        # 분수 비교 대신 곱셈으로 평행 여부 확인
        if dy1 * dx2 == dy2 * dx1:
            return 1
            
    return 0

#######################################################(방법02)

def solution(dots):
    answer = 0
    # 첫 번째 점(dots[0])을 기준으로 다른 점 하나를 선택
    for i in range(1, 4):
        # 선택된 두 점의 인덱스
        p1, p2 = 0, i
        # 남은 두 점의 인덱스 찾기
        others = [idx for idx in range(1, 4) if idx != i]
        p3, p4 = others[0], others[1]
        
        # 기울기 계산
        slope1 = (dots[p1][1] - dots[p2][1]) / (p1_x := dots[p1][0] - dots[p2][0])
        slope2 = (dots[p3][1] - dots[p4][1]) / (p2_x := dots[p3][0] - dots[p4][0])
        
        if slope1 == slope2:
            return 1
            
    return 0

#######################################################(방법03)

def solution(dots):
    slopes = []
    # 모든 가능한 두 점의 조합(6가지)에서 기울기 추출
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            slope = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
            slopes.append(slope)
    
    # 중복을 제거한 기울기 리스트 생성 (기본 문법 활용)
    unique_slopes = []
    for s in slopes:
        if s not in unique_slopes:
            unique_slopes.append(s)
            
    # 전체 6개 조합 중 중복이 발생했다면 평행이 존재할 가능성 높음
    # (단, 이 문제의 제한사항인 '4개의 점'에 특화된 논리)
    return 1 if len(slopes) != len(unique_slopes) else 0

#######################################################(방법04)

def solution(dots):
    # 두 선분이 평행하려면 x변화량:y변화량의 비율이 같아야 함
    def get_vector(idx1, idx2):
        return (dots[idx1][0] - dots[idx2][0], dots[idx1][1] - dots[idx2][1])

    # 케이스 검증 (AB vs CD)
    v1 = get_vector(0, 1)
    v2 = get_vector(2, 3)
    if v1[1]/v1[0] == v2[1]/v2[0]: return 1
    
    # 케이스 검증 (AC vs BD)
    v1 = get_vector(0, 2)
    v2 = get_vector(1, 3)
    if v1[1]/v1[0] == v2[1]/v2[0]: return 1
    
    # 케이스 검증 (AD vs BC)
    v1 = get_vector(0, 3)
    v2 = get_vector(1, 2)
    if v1[1]/v1[0] == v2[1]/v2[0]: return 1
    
    return 0

#######################################################(방법05)

