import sys
from collections import deque

def solve():
    # 1. 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, m = int(input_data[0]), int(input_data[1])
    # 1-based 좌표를 0-based로 변경 (r, c: 말 / s, k: 졸)
    r, c, s, k = map(lambda x: int(x) - 1, input_data[2:])

    # 2. 말의 이동 방향 (8방향)
    dr = [-2, -2, -1, -1, 1, 1, 2, 2]
    dc = [-1, 1, -2, 2, -2, 2, -1, 1]

    # 3. BFS 준비
    # visited 배열에 이동 횟수를 기록 (-1은 미방문)
    visited = [[-1] * m for _ in range(n)]
    queue = deque([(r, c)])
    visited[r][c] = 0

    # 4. 탐색 시작
    while queue:
        curr_r, curr_c = queue.popleft()

        # 졸의 위치에 도달했는지 확인
        if curr_r == s and curr_c == k:
            print(visited[curr_r][curr_c])
            return

        for i in range(8):
            nr, nc = curr_r + dr[i], curr_c + dc[i]

            # 장기판 범위 내에 있고 아직 방문하지 않은 경우만 탐색
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[curr_r][curr_c] + 1
                    queue.append((nr, nc))

if __name__ == "__main__":
    solve()

#####################################################################

