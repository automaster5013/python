import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    r, c = int(input_data[0]), int(input_data[1])
    grid = [list(row) for row in input_data[2:]]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs(start_r, start_c):
        # BFS를 위한 큐와 방문 및 거리 측정 배열
        q = deque([(start_r, start_c, 0)])
        visited = [[False] * c for _ in range(r)]
        visited[start_r][start_c] = True
        
        max_d = 0
        while q:
            curr_r, curr_c, dist = q.popleft()
            # 현재까지의 최단 거리 중 최댓값 갱신
            if dist > max_d:
                max_d = dist
            
            for i in range(4):
                nr, nc = curr_r + dr[i], curr_c + dc[i]
                
                if 0 <= nr < r and 0 <= nc < c:
                    if grid[nr][nc] == 'L' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc, dist + 1))
        return max_d

    # 2. 모든 육지 칸에 대해 BFS 수행
    total_max_dist = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'L':
                # 육지인 경우에만 탐색 시작
                result = bfs(i, j)
                if result > total_max_dist:
                    total_max_dist = result
                    
    # 3. 결과 출력
    print(total_max_dist)

if __name__ == "__main__":
    solve()

######################################################################

