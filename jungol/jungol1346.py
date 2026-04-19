def solve():
    numbers = []
    total_sum = 0
    
    # 1. 다섯 개의 숫자를 입력받아 리스트에 저장하고 합계 구하기
    for _ in range(5):
        try:
            num = int(input())
            numbers.append(num)
            total_sum += num
        except EOFError:
            break
            
    # 2. 평균 계산
    # 수의 합을 개수(5)로 나눈다. 결과가 자연수라고 명시되어 있으므로 // 연산자 사용 가능
    average = total_sum // 5
    
    # 3. 중앙값 계산을 위한 정렬
    # 버블 정렬(Bubble Sort)을 사용하여 라이브러리 없이 직접 정렬
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                # 두 수의 자리를 바꿈 (Swap)
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    # 4. 중앙값 추출
    # 정렬된 리스트 [0, 1, 2, 3, 4]에서 가장 중앙은 인덱스 2번
    median = numbers[2]
    
    # 5. 결과 출력
    print(average)
    print(median)

# 함수 실행
solve()

