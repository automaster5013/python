def solution(n):
    # 2부터 n까지(n 포함) 2씩 건너뛰며 짝수만 생성하여 합산
    answer = sum(range(2, n + 1, 2))
    return answer

#################################################################

def solution(n):
    # n 이하의 짝수 개수 k를 구함
    k = n // 2
    # 등차수열의 합 공식: k * (첫 항 + 끝 항) / 2 => k * (2 + 2k) / 2 = k(k+1)
    answer = k * (k + 1)
    return answer

#################################################################

def solution(n):
    # 1부터 n까지 순회하며 짝수(i % 2 == 0)인 경우만 리스트에 담아 합산
    answer = sum([i for i in range(1, n + 1) if i % 2 == 0])
    return answer

#################################################################

def solution(n):
    # 1~n 범위에서 짝수만 걸러내는 필터 적용
    even_filter = filter(lambda x: x % 2 == 0, range(1, n + 1))
    answer = sum(even_filter)
    return answer

#################################################################

def solution(n):
    answer = 0
    current = 2
    # current가 n 이하일 때까지 2씩 더하며 누적
    while current <= n:
        answer += current
        current += 2
    return answer

#################################################################

