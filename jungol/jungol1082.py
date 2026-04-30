import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    r, c = int(input_data[0]), int(input_data[1])
    grid = [list(row) for row in input_data[2:]]
    
    # 시간 정보를 저장할 배열 (무한대로 초기화)
    fire_time = [[float('inf')] * c for _ in range(r)]
    visited = [[False] * c for _ in range(r)]
    
    fire_q = deque()
    start_pos = None
    target_pos = None
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '*':
                fire_time[i][j] = 0
                fire_q.append((i, j))
            elif grid[i][j] == 'S':
                start_pos = (i, j)
            elif grid[i][j] == 'D':
                target_pos = (i, j)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 2. 불의 BFS: 각 칸에 불이 도달하는 시간 계산
    while fire_q:
        curr_r, curr_c = fire_q.popleft()
        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]
            if 0 <= nr < r and 0 <= nc < c:
                # 불은 빈칸이나 재우의 시작 위치로만 퍼짐 (바위나 집으로는 안 감)
                if grid[nr][nc] in ('.', 'S') and fire_time[nr][nc] == float('inf'):
                    fire_time[nr][nc] = fire_time[curr_r][curr_c] + 1
                    fire_q.append((nr, nc))

    # 3. 재우의 BFS: 탈출 가능한 최단 시간 계산
    q = deque([(start_pos[0], start_pos[1], 0)])
    visited[start_pos[0]][start_pos[1]] = True
    
    while q:
        curr_r, curr_c, time = q.popleft()
        
        if (curr_r, curr_c) == target_pos:
            print(time)
            return
            
        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]
            if 0 <= nr < r and 0 <= nc < c:
                if not visited[nr][nc] and grid[nr][nc] != 'X':
                    # 재우가 다음 칸에 도착할 시간(time + 1)이 불이 도달할 시간보다 빨라야 함
                    if time + 1 < fire_time[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc, time + 1))
    
    print("impossible")

if __name__ == "__main__":
    solve()

###########################################################################################

