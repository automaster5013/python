def solve():
    # 1. N 입력 받기
    line1 = input().split()
    if not line1:
        return
    n = int(line1[0])
    
    # 2. 2N개의 카드 정보 입력 받기
    cards = input().split()
    
    # 각 숫자가 처음 나타난 위치를 저장할 리스트 (N은 최대 2000)
    # 1부터 N까지 사용하므로 크기를 N+1로 설정하고 -1로 초기화
    first_positions = [-1] * (n + 1)
    
    max_distance = 0
    
    # 3. 카드 리스트를 순회하며 거리 계산
    for i in range(2 * n):
        num = int(cards[i])
        
        # 이 숫자가 처음 나온 경우
        if first_positions[num] == -1:
            first_positions[num] = i
        # 이 숫자가 두 번째로 나온 경우
        else:
            # 사이 카드 수 = (현재 인덱스) - (처음 인덱스) - 1
            distance = i - first_positions[num] - 1
            
            # 최댓값 갱신
            if distance > max_distance:
                max_distance = distance
                
    # 4. 결과 출력
    print(max_distance)

# 함수 실행
solve()


