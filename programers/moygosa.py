def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    points = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        if answer == p1[i % len(p1)]:
            points[0] += 1
        if answer == p2[i % len(p2)]:
            points[1] += 1
        if answer == p3[i % len(p3)]:
            points[2] += 1
            
    max_score = max(points)
    
    result = []
    for idx, score in enumerate(points):
        if score == max_score:
            result.append(idx + 1)
            
    return result

###############################################################(방법01)

def solution(answers):
    m = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [[b[i % len(b)] - a for i, a in enumerate(answers)].count(0) for j, b in enumerate(m)]
    return [i + 1 for i, a in enumerate(s) if a >= max(s)]

###############################################################(방법02)

def solution(answers):
    # 1. 수포자들의 반복되는 패턴 정의
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 2. 각 수포자의 맞힌 개수를 저장할 리스트
    scores = [0, 0, 0]
    
    # 3. 정답과 비교하여 점수 산출
    for i, answer in enumerate(answers):
        if answer == p1[i % len(p1)]:
            scores[0] += 1
        if answer == p2[i % len(p2)]:
            scores[1] += 1
        if answer == p3[i % len(p3)]:
            scores[2] += 1
            
    # 4. 가장 높은 점수 확인
    max_score = max(scores)
    
    # 5. 최다 득점자들(여럿일 수 있음)을 결과에 담기
    result = []
    for idx, score in enumerate(scores):
        if score == max_score:
            result.append(idx + 1) # 인덱스는 0부터 시작하므로 +1
            
    return result