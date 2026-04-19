def solve():
    # 1. 현재 시각 (시 A, 분 B) 입력 받기
    try:
        current_time = input().split()
        if not current_time:
            return
        a = int(current_time[0]) # 시
        b = int(current_time[1]) # 분
        
        # 2. 요리 시간 (분 C) 입력 받기
        c = int(input())
    except EOFError:
        return

    # 3. 모든 시간을 '분' 단위로 환산하여 합치기
    # 1시간은 60분이므로 (시 * 60 + 분)에 요리 시간을 더함
    total_minutes = a * 60 + b + c
    
    # 4. 합쳐진 분을 다시 시와 분으로 분리하기
    # 전체 분을 60으로 나눈 몫이 '시', 나머지가 '분'
    final_hour = (total_minutes // 60) % 24 # 24시가 넘어가면 0시부터 다시 시작
    final_minute = total_minutes % 60
    
    # 5. 결과 출력
    print(final_hour, final_minute)

# 함수 실행
solve()


