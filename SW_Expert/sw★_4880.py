def get_winner(p1, p2, cards):
    c1 = cards[p1 - 1]
    c2 = cards[p2 - 1]
    
    win_cases = {1: 3, 2: 1, 3: 2}
    
    if c1 == c2:
        return p1 if p1 < p2 else p2
    elif win_cases[c1] == c2:
        return p1
    else:
        return p2

def divide(i, j, cards):
    if i == j:
        return i
    
    mid = (i + j) // 2
    
    left_winner = divide(i, mid, cards)
    right_winner = divide(mid + 1, j, cards)
    
    return get_winner(left_winner, right_winner, cards)

T_str = input()
if T_str:
    T = int(T_str)
    for tc in range(1, T + 1):
        N = int(input())
        cards = list(map(int, input().split()))
        
        result = divide(1, N, cards)
        
        print(f"#{tc} {result}")

#################################################################





















































# 가위바위보 승자를 가리는 함수
def get_winner(p1, p2, cards):
    # cards는 0번 인덱스부터 시작하므로 학생 번호에서 1을 뺌
    c1 = cards[p1 - 1]
    c2 = cards[p2 - 1]
    
    # 1:가위, 2:바위, 3:보
    # 승리 규칙 정의 (key가 이기는 패, value가 지는 패)
    win_cases = {1: 3, 2: 1, 3: 2}
    
    # 비긴 경우 번호가 작은 사람 승리
    if c1 == c2:
        return p1 if p1 < p2 else p2
    # p1이 이기는 경우
    elif win_cases[c1] == c2:
        return p1
    # 그 외에는 p2 승리
    else:
        return p2

# 재귀적으로 그룹을 나누는 함수
def divide(i, j, cards):
    # 한 명만 남으면 그 학생 번호 반환 (기저 조건)
    if i == j:
        return i
    
    # 문제의 공식 (i+j)//2 를 사용하여 그룹 분할
    mid = (i + j) // 2
    
    # 왼쪽 그룹 승자와 오른쪽 그룹 승자를 각각 구함
    left_winner = divide(i, mid, cards)
    right_winner = divide(mid + 1, j, cards)
    
    # 두 승자끼리 대결하여 최종 승자 반환
    return get_winner(left_winner, right_winner, cards)

# 메인 실행부
T_str = input()
if T_str:
    T = int(T_str)
    for tc in range(1, T + 1):
        N = int(input())
        # 카드 정보를 리스트로 변환
        cards = list(map(int, input().split()))
        
        # 1번부터 N번 학생까지 토너먼트 시작
        result = divide(1, N, cards)
        
        print(f"#{tc} {result}")








    