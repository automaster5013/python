def solve():
    # 1. 첫 번째 줄 입력 (N과 X)
    # input().split()은 공백을 기준으로 문자열을 나누어 리스트로 만듭니다.
    line1 = input().split()
    if not line1:
        return
    
    n = int(line1[0]) # 버스의 개수
    x = int(line1[1]) # 제한 시간
    
    # 지각하지 않는 버스 중 가장 늦은 출발 시간(S)을 저장
    # 초기값 -1은 조건을 만족하는 버스가 없을 때를 대비한 것입니다.
    latest_s = -1
    
    # 2. N개의 버스 정보를 하나씩 확인
    for _ in range(n):
        bus_info = input().split()
        if not bus_info:
            continue
            
        s = int(bus_info[0]) # 출발 대기 시간
        t = int(bus_info[1]) # 학교까지 가는 시간
        
        # 3. 도착 시각(s + t)이 제한 시간(x) 이내인지 확인
        if s + t <= x:
            # 4. 조건을 만족하는 버스 중 가장 큰 s값을 찾음
            if s > latest_s:
                latest_s = s
                
    # 5. 최종 결과 출력
    print(latest_s)

# 함수 실행
solve()


