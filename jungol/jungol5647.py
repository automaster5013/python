def solve():
    # 1. 첫 번째 줄 입력 (N: 묶음 수, K: 한 묶음당 빵 개수, P: 판매 불가 기준)
    line1 = input().split()
    if not line1:
        return
    
    n = int(line1[0])
    k = int(line1[1])
    p = int(line1[2])
    
    # 2. 두 번째 줄 입력 (전체 빵의 크림 정보)
    # 총 N * K 개의 빵 정보가 들어옴
    breads = input().split()
    
    sellable_count = 0  # 팔 수 있는 묶음의 수를 저장할 변수
    
    # 3. N개의 묶음을 하나씩 순회
    for i in range(n):
        # 현재 묶음에서 크림이 없는 빵(0)의 개수를 셀 변수
        no_cream_count = 0
        
        # 4. i번째 묶음에 해당하는 빵들을 확인 (인덱스: i*k 부터 (i+1)*k - 1 까지)
        for j in range(k):
            # 현재 확인 중인 빵의 인덱스 계산
            current_index = i * k + j
            
            # 크림이 없는 빵(문자열 "0")이라면 개수 증가
            if breads[current_index] == "0":
                no_cream_count += 1
        
        # 5. 판매 가능 조건 확인: 크림 없는 빵이 P개 미만이어야 함
        if no_cream_count < p:
            sellable_count += 1
            
    # 6. 결과 출력
    print(sellable_count)

# 함수 실행
solve()


