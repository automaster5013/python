def solution(money):
    # 몫(잔 수)과 나머지(잔돈)를 각각 계산하여 리스트로 반환
    cups = money // 5500
    change = money % 5500
    answer = [cups, change]
    return answer

###########################################################

def solution(money):
    # divmod는 (money // 5500, money % 5500)을 한 번에 반환함
    # 반환된 튜플을 리스트로 변환하여 정답 포맷 생성
    answer = list(divmod(money, 5500))
    return answer

###########################################################

def solution(money):
    # 리스트 내부에서 필요한 연산을 직접 수행
    # [몫, 나머지] 순서대로 리스트 생성
    answer = [money // 5500, money % 5500]
    return answer

###########################################################

def solution(money):
    cups = 0
    # 가진 돈이 커피 값보다 많다면 계속해서 한 잔씩 구매
    while money >= 5500:
        money -= 5500
        cups += 1
    
    # 구매한 잔 수와 남은 돈(잔돈)을 리스트에 담음
    answer = [cups, money]
    return answer

###########################################################

def solution(money):
    # 몫과 나머지를 각각 cups와 change라는 변수에 할당
    cups, change = divmod(money, 5500)
    
    # 할당된 변수들을 리스트로 묶어서 반환
    answer = [cups, change]
    return answer

###########################################################


