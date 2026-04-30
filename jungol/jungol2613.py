import sys
from collections import deque

def solve():
    # 1. 입력 처리 (가로 M, 세로 N)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    m = int(input_data[0])
    n = int(input_data[1])
    
    grid = []
    queue = deque()
    unripe_count = 0
    
    idx = 2
    for r in range(n):
        row = list(map(int, input_data[idx : idx + m]))
        grid.append(row)
        for c in range(m):
            if row[c] == 1:
                # 익은 토마토의 위치를 큐에 추가 (r, c, day)
                queue.append((r, c, 0))
            elif row[c] == 0:
                unripe_count += 1
        idx += m

    # 처음부터 모든 토마토가 익어있는 경우
    if unripe_count == 0:
        print(0)
        return

    # 2. BFS 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_days = 0
    
    while queue:
        curr_r, curr_c, curr_day = queue.popleft()
        max_days = curr_day
        
        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 1 # 토마토 익힘
                    unripe_count -= 1
                    queue.append((nr, nc, curr_day + 1))

    # 3. 결과 출력
    # 탐색 후에도 익지 않은 토마토가 남아있으면 -1
    if unripe_count > 0:
        print(-1)
    else:
        print(max_days)

if __name__ == "__main__":
    solve()

#################################################################

