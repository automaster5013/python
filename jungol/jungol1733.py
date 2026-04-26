import sys

def solve_v1():
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
    
    # 우, 하, 우하향, 우상향 방향 벡터
    dr = [0, 1, 1, -1]
    dc = [1, 0, 1, 1]

    for r in range(19):
        for c in range(19):
            if board[r][c] != 0:
                color = board[r][c]
                
                for i in range(4):
                    cnt = 1
                    nr, nc = r + dr[i], c + dc[i]
                    
                    while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == color:
                        cnt += 1
                        if cnt == 5:
                            # 육목 체크: 시작점 이전 칸과 5번째 이후 칸 확인
                            prev_r, prev_c = r - dr[i], c - dc[i]
                            next_r, next_c = nr + dr[i], nc + dc[i]
                            
                            # 시작점 이전이 같은 색이 아니고, 5번째 다음도 같은 색이 아니어야 정답
                            if not (0 <= prev_r < 19 and 0 <= prev_c < 19 and board[prev_r][prev_c] == color):
                                if not (0 <= next_r < 19 and 0 <= next_c < 19 and board[next_r][next_c] == color):
                                    print(color)
                                    print(r + 1, c + 1)
                                    return
                            break
                        nr += dr[i]
                        nc += dc[i]
                        
    print(0)

solve_v1()

##########################################################################################################################

def is_winner(r, c, dr, dc, board):
    color = board[r][c]
    for i in range(1, 5):
        nr, nc = r + dr * i, c + dc * i
        if not (0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == color):
            return False
    # 육목 체크 (앞뒤)
    if 0 <= r - dr < 19 and 0 <= c - dc < 19 and board[r - dr][c - dc] == color:
        return False
    if 0 <= r + dr * 5 < 19 and 0 <= c + dc * 5 < 19 and board[r + dr * 5][c + dc * 5] == color:
        return False
    return True

def solve_v2():
    board = [list(map(int, input().split())) for _ in range(19)]
    dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    
    for r in range(19):
        for c in range(19):
            if board[r][c] != 0:
                for dr, dc in dirs:
                    if is_winner(r, c, dr, dc, board):
                        print(board[r][c])
                        print(r + 1, c + 1)
                        return
    print(0)

solve_v2()

##########################################################################################################################

def solve_v3():
    # 주변을 0으로 감싼 21x21 판 생성
    board = [[0]*21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0]*21]
    
    for r in range(1, 20):
        for c in range(1, 20):
            if board[r][c]:
                for dr, dc in [(0,1), (1,0), (1,1), (-1,1)]:
                    # 5알 연속 확인
                    if all(board[r + dr*i][c + dc*i] == board[r][c] for i in range(5)):
                        # 육목(6알) 방지: 앞뒤 칸이 현재 돌과 달라야 함
                        if board[r-dr][c-dc] != board[r][c] and board[r+dr*5][c+dc*5] != board[r][c]:
                            print(board[r][c])
                            print(r, c) # 패딩 때문에 1을 더할 필요 없음
                            return
    print(0)

solve_v3()

##########################################################################################################################

def solve_v4():
    stones = {1: set(), 2: set()}
    for r in range(19):
        row = list(map(int, input().split()))
        for c, val in enumerate(row):
            if val: stones[val].add((r, c))
            
    dirs = [(0,1), (1,0), (1,1), (-1,1)]
    # 좌표 정렬 (가장 왼쪽/위쪽 돌을 먼저 찾기 위함)
    for color in [1, 2]:
        for r, c in sorted(stones[color], key=lambda x: (x[1], x[0])):
            for dr, dc in dirs:
                if all((r + dr*i, c + dc*i) in stones[color] for i in range(5)):
                    if (r - dr, c - dc) not in stones[color] and (r + dr*5, c + dc*5) not in stones[color]:
                        print(color)
                        print(r + 1, c + 1)
                        return
    print(0)

solve_v4()

##########################################################################################################################

def solve_v5():
    b = [list(map(int, input().split())) for _ in range(19)]
    
    for r in range(19):
        for c in range(19):
            if b[r][c] == 0: continue
            
            for dr, dc in [(0,1), (1,0), (1,1), (-1,1)]:
                # 5개 연속성 확인
                try:
                    # 파이썬 특유의 음수 인덱스 방지
                    if r - dr < 0 or c - dc < 0:
                        if r - dr != -1 or c - dc != -1: # 경계선 밖으로 간주
                            pass 

                    # 정확히 5개인지 검사 (슬라이싱 개념 차용)
                    match = True
                    for i in range(5):
                        if not (0 <= r+dr*i < 19 and 0 <= c+dc*i < 19 and b[r+dr*i][c+dc*i] == b[r][c]):
                            match = False; break
                    
                    if match:
                        # 육목 체크
                        before = b[r-dr][c-dc] if 0<=r-dr<19 and 0<=c-dc<19 else -1
                        after = b[r+dr*5][c+dc*5] if 0<=r+dr*5<19 and 0<=c+dc*5<19 else -1
                        if before != b[r][c] and after != b[r][c]:
                            print(b[r][c])
                            print(r+1, c+1)
                            return
                except IndexError: continue
    print(0)

solve_v5()

##########################################################################################################################

