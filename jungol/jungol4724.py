def solve():
    # 1. 입력 받기 (N은 100 이하의 자연수)
    line = input().split()
    if not line:
        return
    n = int(line[0])
    
    # 2. 1부터 N까지의 수가 담긴 리스트 생성
    # 예: n=5 -> [1, 2, 3, 4, 5]
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
        
    # 3. 숫자가 하나만 남을 때까지 반복
    while len(numbers) > 1:
        next_numbers = []
        
        # 4. (A) 홀수번 칸의 수를 지우고, (B) 남은 수들을 모음
        # 파이썬의 인덱스는 0부터 시작하므로:
        # 1번 칸 -> 인덱스 0 (홀수번 칸)
        # 2번 칸 -> 인덱스 1 (짝수번 칸) -> 유지
        # 3번 칸 -> 인덱스 2 (홀수번 칸)
        # 즉, 인덱스가 '홀수'인 것들만 남겨야 합니다.
        for index in range(len(numbers)):
            # 칸 번호(index + 1)가 짝수인 경우만 새로운 리스트에 담음
            if (index + 1) % 2 == 0:
                next_numbers.append(numbers[index])
        
        # 남은 수들로 리스트를 교체
        numbers = next_numbers
        
    # 5. 마지막 남은 수 출력
    print(numbers[0])

# 함수 실행
solve()


