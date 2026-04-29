import sys
from collections import deque

def solve():
    # 1. 입력 처리 및 0-based 변환
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    m, n = int(input_data[0]), int(input_data[1])
    grid = []
    idx = 2
    for _ in range(m):
        grid.append(list(map(int, input_data[idx:idx+n])))
        idx += n
    
    # 출발지(sr, sc, sd), 도착지(er, ec, ed)
    sr, sc, sd = map(int, input_data[idx:idx+3])
    er, ec, ed = map(int, input_data[idx+3:idx+6])
    
    # 좌표만 0-based로 변경 (방향은 1~4 그대로 사용)
    sr -= 1; sc -= 1; er -= 1; ec -= 1
    
    # 2. 방향 벡터 설정 (1:동, 2:서, 3:남, 4:북)
    # 인덱스 0은 더미값
    dr = [0, 0, 0, 1, -1]
    dc = [0, 1, -1, 0, 0]
    
    # visited[row][col][dir]
    visited = [[[False] * 5 for _ in range(n)] for _ in range(m)]
    
    # 3. BFS 탐색
    queue = deque([(sr, sc, sd, 0)])
    visited[sr][sc][sd] = True
    
    while queue:
        r, c, d, dist = queue.popleft()
        
        # 목표 지점 및 방향 도달 시 즉시 종료
        if r == er and c == ec and d == ed:
            print(dist)
            return
            
        # 명령 1: Go k (1, 2, 3)
        for k in range(1, 4):
            nr, nc = r + dr[d] * k, c + dc[d] * k
            
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == 0:
                    if not visited[nr][nc][d]:
                        visited[nr][nc][d] = True
                        queue.append((nr, nc, d, dist + 1))
                else:
                    # 중간에 벽이 있으면 더 멀리 갈 수 없음
                    break
            else:
                break
                
        # 명령 2: Turn Left/Right (90도 회전)
        # 동(1)/서(2)에서는 남(3)/북(4)으로, 남(3)/북(4)에서는 동(1)/서(2)로 회전 가능
        def get_next_dirs(curr_d):
            if curr_d <= 2: return [3, 4]
            else: return [1, 2]
            
        for nd in get_next_dirs(d):
            if not visited[r][c][nd]:
                visited[r][c][nd] = True
                queue.append((r, c, nd, dist + 1))

if __name__ == "__main__":
    solve()

#######################################################################################

