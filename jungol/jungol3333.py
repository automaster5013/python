def solve():
    # 1. 막대기의 개수 N 입력 받기
    try:
        line = input().split()
        if not line:
            return
        n = int(line[0])
    except EOFError:
        return
    
    # 2. 막대기들의 높이를 리스트에 저장
    # N이 최대 100,000이므로 하나씩 입력받아 리스트에 담습니다.
    heights = []
    for _ in range(n):
        heights.append(int(input()))
        
    # 3. 오른쪽에서 보았을 때 보이는 막대기 수 세기
    # 맨 오른쪽에 있는 막대기는 무조건 보입니다.
    count = 1
    # 현재까지 오른쪽에서 보았던 막대기 중 가장 높은 높이를 저장
    # 초기값은 맨 오른쪽 막대기의 높이입니다.
    max_height = heights[n - 1]
    
    # 4. 오른쪽에서 두 번째 막대기부터 왼쪽 방향으로 탐색 (역순 순회)
    # 인덱스 n-2부터 0까지 -1씩 감소하며 확인
    for i in range(n - 2, -1, -1):
        # 현재 막대기가 지금까지의 최댓값보다 크면 보입니다.
        if heights[i] > max_height:
            count += 1
            # 새로운 최댓값으로 갱신
            max_height = heights[i]
            
    # 5. 결과 출력
    print(count)

# 함수 실행
solve()


