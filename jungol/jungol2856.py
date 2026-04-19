def solve():
    # 1. 날짜의 일의 자리 숫자 입력 받기
    # input()은 문자열로 들어오므로 정수(int)로 변환
    try:
        day_digit = int(input())
    except EOFError:
        return

    # 2. 자동차 5대의 번호 일의 자리 숫자들 입력 받기
    # split()을 통해 공백으로 구분된 문자열들을 리스트로 만듬
    car_digits = input().split()
    
    # 위반 차량의 수를 저장할 변수
    violation_count = 0
    
    # 3. 5대의 자동차 번호를 하나씩 확인
    for car in car_digits:
        # 문자열 상태인 car를 정수로 변환하여 날짜 숫자와 비교
        if int(car) == day_digit:
            # 숫자가 일치하면 위반 차량이므로 개수를 1 증가
            violation_count += 1
            
    # 4. 최종 위반 차량 수 출력
    print(violation_count)

# 함수 실행
solve()


