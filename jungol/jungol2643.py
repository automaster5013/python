def solve():
    # 1. 꼭짓점 입력 받기
    try:
        line1 = input().split()
        if not line1: return
        n = int(line1[0])
    except EOFError:
        return

    vertices = []
    for _ in range(n):
        vertices.append(list(map(int, input().split())))

    # 2. 수평 선분(바닥) 정보만 추출
    # 시작(0,0) -> 수직 -> 수평 -> 수직 -> 수평 ... 순서이므로
    # 인덱스 1-2, 3-4, 5-6 ... 가 수평 선분입니다.
    segs = []
    for i in range(1, n - 1, 2):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i+1]
        # [x1, x2, 깊이y, 구멍여부]
        segs.append([x1, x2, y1, False])

    # 3. 구멍 정보 입력 및 매핑
    k = int(input())
    for _ in range(k):
        h_info = list(map(int, input().split()))
        hx1, hy = h_info[0], h_info[1]
        # 해당 구멍이 어느 수평 선분에 있는지 찾아서 표시
        for s in segs:
            if s[0] == hx1 and s[2] == hy:
                s[3] = True
                break

    num_segs = len(segs)
    
    # 4. 왼쪽에서 오른쪽으로 흐르는 물의 높이 계산 (L_drain)
    l_drain = [0] * num_segs
    curr_max_y = 0 # 현재까지 도달 가능한 가장 깊은 구멍의 y값
    for i in range(num_segs):
        # 경로 상의 가장 얕은 턱(y가 작은 값)에 의해 배수 높이가 제한됨
        curr_max_y = min(curr_max_y, segs[i][2])
        # 만약 현재 선분에 구멍이 있다면, 그 선분의 깊이가 새로운 배수 기준이 됨
        if segs[i][3]:
            curr_max_y = max(curr_max_y, segs[i][2])
        l_drain[i] = curr_max_y

    # 5. 오른쪽에서 왼쪽으로 흐르는 물의 높이 계산 (R_drain)
    r_drain = [0] * num_segs
    curr_max_y = 0
    for i in range(num_segs - 1, -1, -1):
        curr_max_y = min(curr_max_y, segs[i][2])
        if segs[i][3]:
            curr_max_y = max(curr_max_y, segs[i][2])
        r_drain[i] = curr_max_y

    # 6. 남은 물의 양 계산
    total_remaining = 0
    for i in range(num_segs):
        width = segs[i][1] - segs[i][0]
        original_depth = segs[i][2]
        # 왼쪽/오른쪽 중 더 많이 빠지는(y값이 더 큰) 쪽이 최종 수위
        final_water_y = max(l_drain[i], r_drain[i])
        
        # 남은 물의 높이는 (원래 깊이 - 빠진 높이). 단, 음수가 될 수 없으므로 max(0, ...)
        remaining_depth = max(0, original_depth - final_water_y)
        total_remaining += width * remaining_depth

    print(total_remaining)

solve()

############################################################################################



