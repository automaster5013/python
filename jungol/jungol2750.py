def solve():
    # 1. 과자 가격 K, 개수 N, 현재 돈 M 입력 받기
    # input().split()을 통해 공백으로 구분된 값을 리스트로 가져옵니다.
    try:
        data = input().split()
        if not data:
            return
        
        k = int(data[0]) # 과자 한 개의 가격
        n = int(data[1]) # 사려고 하는 과자의 개수
        m = int(data[2]) # 현재 동수가 가진 돈
    except EOFError:
        return

    # 2. 전체 과자 가격 계산
    total_price = k * n
    
    # 3. 모자란 돈 계산 (전체 가격 - 가진 돈)
    needed_money = total_price - m
    
    # 4. 결과 출력
    # 계산된 값이 0보다 작거나 같다면 돈이 충분하다는 뜻이므로 0을 출력합니다.
    if needed_money <= 0:
        print(0)
    else:
        print(needed_money)

# 함수 실행
solve()


