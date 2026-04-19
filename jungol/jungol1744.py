def solve():
    # 총 3번의 윷 던지기 결과가 주어지므로 3번 반복
    for _ in range(3):
        try:
            # 한 줄에 4개의 윷짝 상태(0 또는 1)를 입력
            data = input().split()
            if not data:
                break
                
            # 배(0)의 개수를 저장할 변수
            zero_count = 0
            
            # 입력받은 4개의 윷짝을 하나씩 확인하며 '0'의 개수를 셈
            for yut in data:
                if yut == '0':
                    zero_count += 1
            
            # 0의 개수에 따라 도, 개, 걸, 윷, 모 판별
            if zero_count == 1:
                print('A') # 도
            elif zero_count == 2:
                print('B') # 개
            elif zero_count == 3:
                print('C') # 걸
            elif zero_count == 4:
                print('D') # 윷
            elif zero_count == 0:
                print('E') # 모
                
        except EOFError:
            break

# 함수 실행
solve()

