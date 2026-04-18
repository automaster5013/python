def solve():
    # 1. 가게의 수 N 입력 받기
    try:
        line1 = input().split()
        if not line1:
            return
        n = int(line1[0])
    except EOFError:
        return
    
    # 가장 빨리 구할 수 있는 시간을 저장할 변수
    # 초기값으로 문제에서 나올 수 있는 최대 시간(1000)보다 큰 값을 설정하거나
    # 살 수 있는 경우를 체크하기 위해 -1 등으로 설정해
    min_time = 1001 
    
    # 2. N개의 가게 정보 입력 받기
    for _ in range(n):
        store_info = input().split()
        if not store_info:
            continue
            
        a = int(store_info[0]) # 가게까지 가는 시간
        b = int(store_info[1]) # 빵이 들어오는 시간
        
        # 3. 빵을 살 수 있는지 확인 (도착 시간 A <= 빵 들어오는 시간 B)
        if a <= b:
            # 4. 살 수 있는 경우 중 가장 빠른 시간(B의 최솟값) 갱신
            if b < min_time:
                min_time = b
                
    # 5. 결과 출력
    # min_time이 초기값 그대로라면 살 수 있는 가게가 없었다는 뜻
    if min_time == 1001:
        print(-1)
    else:
        print(min_time)

# 함수 실행
solve()


