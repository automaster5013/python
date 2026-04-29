import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m, n = int(input_data[0]), int(input_data[1]) # m: 열, n: 행
    
    grid = []
    total_zerglings = 0
    idx = 2
    for r in range(n):
        row_str = input_data[idx]
        row = [int(char) for char in row_str]
        grid.append(row)
        total_zerglings += row.count(1) # 전체 저글링 수 카운트
        idx += 1
        
    start_x = int(input_data[idx]) # 열(col)
    start_y = int(input_data[idx+1]) # 행(row)
    
    # 2. BFS 준비
    # 시작 위치가 저글링이 없는 곳일 경우 예외 처리 (문제 조건상 대개 1임)
    if grid[start_y-1][start_x-1] == 0:
        print(0)
        print(total_zerglings)
        return

    queue = deque([(start_y-1, start_x-1, 3)]) # (r, c, death_time) 시작 저글링은 3초 뒤에 죽음
    visited = [[False] * m for _ in range(n)]
    visited[start_y-1][start_x-1] = True
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    max_death_time = 3
    polluted_count = 0
    
    # 3. BFS 탐색
    while queue:
        curr_r, curr_c, curr_time = queue.popleft()
        polluted_count += 1
        max_death_time = max(max_death_time, curr_time)
        
        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # 다음 저글링은 1초 뒤에 오염되므로 현재 죽는 시간 + 1
                    queue.append((nr, nc, curr_time + 1))

    # 4. 결과 출력
    print(max_death_time)
    print(total_zerglings - polluted_count)

if __name__ == "__main__":
    solve()

###############################################################################3

