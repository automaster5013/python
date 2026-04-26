def check_bingo(board):
    count = 0
    # 1. 가로 확인
    for row in board:
        if sum(row) == 0: count += 1
    # 2. 세로 확인
    for c in range(5):
        if sum(board[r][c] for r in range(5)) == 0: count += 1
    # 3. 대각선 확인 (좌상 -> 우하)
    if sum(board[i][i] for i in range(5)) == 0: count += 1
    # 4. 대각선 확인 (우상 -> 좌하)
    if sum(board[i][4-i] for i in range(5)) == 0: count += 1
    
    return count >= 3

def solve_v1():
    board = [list(map(int, input().split())) for _ in range(5)]
    calls = []
    for _ in range(5):
        calls.extend(list(map(int, input().split())))

    for i, num in enumerate(calls):
        # 숫자 위치 찾아서 0으로 마킹
        for r in range(5):
            for c in range(5):
                if board[r][c] == num:
                    board[r][c] = 0
                    break
        
        # 12번째 수 전에는 절대 3빙고가 나올 수 없으므로 최적화 (선택 사항)
        if i >= 11:
            if check_bingo(board):
                print(i + 1)
                return

solve_v1()

##############################################################################

def solve_v2():
    pos = {}
    for r in range(5):
        row = list(map(int, input().split()))
        for c, val in enumerate(row):
            pos[val] = (r, c)
            
    calls = []
    for _ in range(5): calls.extend(map(int, input().split()))
    
    marked = [[False] * 5 for _ in range(5)]
    
    for turn, num in enumerate(calls):
        r, c = pos[num]
        marked[r][c] = True
        
        # 빙고 개수 계산
        line_cnt = 0
        # 가로/세로
        for i in range(5):
            if all(marked[i][j] for j in range(5)): line_cnt += 1
            if all(marked[j][i] for j in range(5)): line_cnt += 1
        # 대각선
        if all(marked[i][i] for i in range(5)): line_cnt += 1
        if all(marked[i][4-i] for i in range(5)): line_cnt += 1
        
        if line_cnt >= 3:
            print(turn + 1)
            return

solve_v2()

##############################################################################

def solve_v3():
    board_pos = {}
    for r in range(5):
        for c, val in enumerate(map(int, input().split())):
            board_pos[val] = (r, c)
            
    row_cnt, col_cnt = [0]*5, [0]*5
    diag1, diag2 = 0, 0
    bingo_lines = 0
    
    calls = []
    for _ in range(5): calls.extend(map(int, input().split()))
    
    # 이미 빙고가 된 라인을 다시 세지 않기 위해 set 사용
    bingo_set = set()

    for i, num in enumerate(calls):
        r, c = board_pos[num]
        row_cnt[r] += 1
        if row_cnt[r] == 5: bingo_set.add(f"r{r}")
        
        col_cnt[c] += 1
        if col_cnt[c] == 5: bingo_set.add(f"c{c}")
        
        if r == c:
            diag1 += 1
            if diag1 == 5: bingo_set.add("d1")
        if r + c == 4:
            diag2 += 1
            if diag2 == 5: bingo_set.add("d2")
            
        if len(bingo_set) >= 3:
            print(i + 1)
            return

solve_v3()

##############################################################################

def solve_v4():
    # 1~25 숫자가 빙고판의 몇 번 인덱스(0~24)에 있는지 저장
    pos = [0] * 26
    for r in range(5):
        for c, v in enumerate(map(int, input().split())):
            pos[v] = r * 5 + c
            
    marked = [0] * 25
    calls = []
    for _ in range(5): calls.extend(map(int, input().split()))
    
    for turn, num in enumerate(calls):
        marked[pos[num]] = 1
        
        # 빙고 체크 로직
        count = 0
        # 가로
        for i in range(0, 25, 5):
            if sum(marked[i:i+5]) == 5: count += 1
        # 세로
        for i in range(5):
            if sum(marked[i::5]) == 5: count += 1
        # 대각선
        if sum(marked[0:25:6]) == 5: count += 1 # 0, 6, 12, 18, 24
        if sum(marked[4:21:4]) == 5: count += 1 # 4, 8, 12, 16, 20
        
        if count >= 3:
            print(turn + 1)
            return

solve_v4()

##############################################################################

def solve_v5():
    board_map = {}
    for r in range(5):
        for c, v in enumerate(map(int, input().split())):
            board_map[v] = (r, c)
            
    # 가능한 모든 빙고 라인 (좌표의 집합)
    lines = []
    for i in range(5):
        lines.append({(i, j) for j in range(5)}) # 행
        lines.append({(j, i) for j in range(5)}) # 열
    lines.append({(i, i) for i in range(5)})     # 대각선1
    lines.append({(i, 4-i) for i in range(5)})   # 대각선2
    
    called_pos = set()
    calls = []
    for _ in range(5): calls.extend(map(int, input().split()))
    
    for turn, num in enumerate(calls):
        called_pos.add(board_map[num])
        
        bingo_count = 0
        for line in lines:
            if line.issubset(called_pos):
                bingo_count += 1
                
        if bingo_count >= 3:
            print(turn + 1)
            return

solve_v5()

##############################################################################


