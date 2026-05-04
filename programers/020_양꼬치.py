def solution(n, k):
    # 양꼬치 가격 + 음료수 가격 - (서비스 음료수 개수 * 음료수 가격)
    service_drink = n // 10
    answer = (n * 12000) + (k * 2000) - (service_drink * 2000)
    return answer

###########################################################################

def solution(n, k):
    # k개 중에서 서비스(n // 10)를 제외한 실제 유료 음료 개수 계산
    paid_drinks = k - (n // 10)
    answer = (n * 12000) + (paid_drinks * 2000)
    return answer

###########################################################################

def solution(n, k):
    # 몫(service)만 필요하지만 divmod의 활용법을 익히기에 좋은 예제
    service, _ = divmod(n, 10)
    answer = (n * 12000) + (k - service) * 2000
    return answer

###########################################################################

def solution(n, k):
    # 한 줄로 요약된 수식 계산
    # 서비스 음료만큼 k에서 미리 뺀 값을 사용
    answer = (lambda n, k: n * 12000 + (k - n // 10) * 2000)(n, k)
    return answer

###########################################################################

def solution(n, k):
    LAMB_PRICE = 12000
    DRINK_PRICE = 2000
    SERVICE_THRESHOLD = 10
    
    # 서비스로 감면받을 음료 수 계산
    discount_drinks = n // SERVICE_THRESHOLD
    
    # 각 항목별 합계 산출
    total_lamb = n * LAMB_PRICE
    total_drinks = (k - discount_drinks) * DRINK_PRICE
    
    answer = total_lamb + total_drinks
    return answer

###########################################################################





