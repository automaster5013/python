def solution(n):
    answer = 0
    # 1부터 n까지 모든 숫자를 확인
    for i in range(1, n + 1):
        if n % i == 0:
            answer += 1
    return answer

###############################################################

def solution(n):
    # n의 약수들만 리스트로 생성하여 길이를 반환
    answer = len([i for i in range(1, n + 1) if n % i == 0])
    return answer

###############################################################

def solution(n):
    answer = 0
    # 1부터 n의 제곱근까지만 확인
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # 제곱근인 경우 (예: 10*10=100) 한 번만 카운트
            if i * i == n:
                answer += 1
            # 그 외의 경우 (예: 1*20, 2*10) 쌍으로 존재하므로 2개 카운트
            else:
                answer += 2
    return answer

###############################################################

def solution(n):
    # 1~n 범위에서 약수 조건(n % x == 0)을 만족하는 요소만 필터링
    divisors = filter(lambda x: n % x == 0, range(1, n + 1))
    # 이터레이터의 요소 개수를 세기 위해 sum 활용
    answer = sum(1 for _ in divisors)
    return answer

###############################################################

def solution(n):
    answer = 1
    d = 2
    temp = n
    # 소인수분해 수행
    while d * d <= temp:
        count = 0
        while temp % d == 0:
            count += 1
            temp //= d
        # 약수의 개수 공식: (지수 + 1)들의 곱
        answer *= (count + 1)
        d += 1
    if temp > 1:
        answer *= 2
    return answer

###############################################################



