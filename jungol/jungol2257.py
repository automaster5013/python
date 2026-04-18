def solve():
    # 1. 5개의 고유번호 숫자 입력 받기
    # input().split()을 사용하여 공백으로 구분된 5개의 숫자를 리스트로 가져옵니다.
    try:
        data = input().split()
        if not data:
            return
    except EOFError:
        return

    # 각 숫자의 제곱의 합을 저장할 변수
    total_sum = 0
    
    # 2. 리스트에 들어있는 5개의 숫자를 하나씩 확인
    for s in data:
        num = int(s) # 문자열을 정수로 변환
        
        # 3. 숫자를 제곱하여 합계에 누적
        # num ** 2 또는 num * num을 사용합니다.
        total_sum += (num * num)
        
    # 4. 검증수 계산: 제곱의 합을 10으로 나눈 나머지
    verification_number = total_sum % 10
    
    # 5. 결과 출력
    print(verification_number)

# 함수 실행
solve()

