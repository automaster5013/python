import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    m = int(input_data[0]) # 세로 (행)
    n = int(input_data[1]) # 가로 (열)
    k = int(input_data[2]) # 직사각형 개수
    
    # 2. 격자 초기화 (0: 빈 칸, 1: 직사각형)
    grid = [[0] * n for _ in range(m)]
    
    idx = 3
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input_data[idx:idx+4])
        idx += 4
        # 직사각형 영역을 1로 채우기
        # 주의: 좌표 (x1, y1) -> (x2, y2)는 인덱스상 y1~y2-1, x1~x2-1임
        for y in range(y1, y2):
            for x in range(x1, x2):
                grid[y][x] = 1
                
    # 3. BFS 탐색을 통한 영역 구하기
    areas = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for r in range(m):
        for c in range(n):
            # 아직 방문하지 않은 빈 칸(0) 발견 시 탐색 시작
            if grid[r][c] == 0:
                grid[r][c] = 1 # 방문 표시
                queue = deque([(r, c)])
                count = 1 # 현재 영역의 넓이
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    
                    for i in range(4):
                        nr, nc = curr_r + dr[i], curr_c + dc[i]
                        
                        if 0 <= nr < m and 0 <= nc < n:
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = 1 # 방문 표시
                                count += 1
                                queue.append((nr, nc))
                
                areas.append(count)
                
    # 4. 결과 출력
    areas.sort() # 오름차순 정렬
    print(len(areas)) # 영역 개수
    print(*(areas)) # 각 영역의 넓이

if __name__ == "__main__":
    solve()

#######################################################################


