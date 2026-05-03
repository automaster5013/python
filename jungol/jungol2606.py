import sys
from collections import deque

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # M: 가로, N: 세로, H: 높이
    m = int(input_data[0])
    n = int(input_data[1])
    h = int(input_data[2])
    
    # 3차원 창고 데이터 구성 [h][n][m]
    warehouse = []
    queue = deque()
    unripe_count = 0
    
    ptr = 3
    for z in range(h):
        layer = []
        for y in range(n):
            row = list(map(int, input_data[ptr : ptr + m]))
            for x in range(m):
                if row[x] == 1:
                    # 익은 토마토의 좌표(z, y, x)와 경과 일수(0)를 큐에 추가
                    queue.append((z, y, x, 0))
                elif row[x] == 0:
                    unripe_count += 1
            layer.append(row)
            ptr += m
        warehouse.append(layer)
        
    # 저장될 때부터 모든 토마토가 익어있는 경우
    if unripe_count == 0:
        print(0)
        return

    # 6방향 이동 좌표 (위, 아래, 상, 하, 좌, 우)
    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]
    
    max_days = 0
    
    # BFS 탐색 시작
    while queue:
        curr_z, curr_y, curr_x, days = queue.popleft()
        max_days = days
        
        for i in range(6):
            nz, ny, nx = curr_z + dz[i], curr_y + dy[i], curr_x + dx[i]
            
            # 창고 범위 내에 있고, 아직 익지 않은 토마토(0)인 경우
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if warehouse[nz][ny][nx] == 0:
                    warehouse[nz][ny][nx] = 1 # 토마토 익음 처리
                    unripe_count -= 1
                    queue.append((nz, ny, nx, days + 1))
                    
    # 모든 토마토가 익었는지 확인
    if unripe_count == 0:
        print(max_days)
    else:
        print(-1)

if __name__ == "__main__":
    solve()

#############################################################################



