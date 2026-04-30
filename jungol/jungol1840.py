import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input = sys.stdin.read().split()
    if not input: return
    n, m = int(input[0]), int(input[1])
    grid = []
    ptr = 2
    for i in range(n):
        grid.append(list(map(int, input[ptr:ptr+m])))
        ptr += m

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def get_melting_cheese():
        # 외부 공기(0,0)에서 시작하는 BFS
        q = deque([(0, 0)])
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True
        melting = []
        
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                    visited[ny][nx] = True
                    if grid[ny][nx] == 0:
                        q.append((ny, nx))
                    else:
                        # 공기와 맞닿은 치즈 발견
                        melting.append((ny, nx))
        return melting

    time = 0
    last_cheese_count = 0

    while True:
        # 현재 남은 치즈 개수 파악
        current_cheese = sum(row.count(1) for row in grid)
        if current_cheese == 0:
            break
            
        last_cheese_count = current_cheese # 녹기 전 개수 저장
        
        # 이번 시간에 녹을 치즈들 찾기
        targets = get_melting_cheese()
        
        # 치즈 녹이기
        for ry, rx in targets:
            grid[ry][rx] = 0
            
        time += 1

    print(time)
    print(last_cheese_count)

if __name__ == "__main__":
    solve()

###############################################################################


