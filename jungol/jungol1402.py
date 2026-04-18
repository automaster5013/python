def solve():
    # 1. N과 K 입력 받기
    try:
        data = input().split()
        if not data:
            return
        
        n = int(data[0]) # 약수를 구할 대상 숫자
        k = int(data[1]) # 몇 번째 약수를 찾을 것인지
    except EOFError:
        return

    # 2. 약수들을 담을 리스트 생성
    divisors = []
    
    # 3. 1부터 N까지 모든 숫자로 나누어보며 약수 찾기
    for i in range(1, n + 1):
        # N을 i로 나누었을 때 나머지가 0이면 i는 N의 약수
        if n % i == 0:
            divisors.append(i)
            
    # 4. 결과 출력
    # 약수의 개수가 K개보다 작으면 0을 출력
    if len(divisors) < k:
        print(0)
    else:
        # K번째 약수 출력 (인덱스는 0부터 시작하므로 K-1 사용)
        print(divisors[k - 1])

# 함수 실행
solve()

