import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 지도를 2차원 리스트로 변환 (숫자형으로 저장)
    grid = [list(map(int, list(row))) for row in input_data[1:]]
    
    # 상하좌우 이동을 위한 방향 벡터
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    complex_sizes = [] # 각 단지의 크기를 저장할 리스트

    # 2. 지도를 순회하며 단지 찾기
    for r in range(n):
        for c in range(n):
            # 집이 있는 곳(1)을 발견하면 탐색 시작
            if grid[r][c] == 1:
                # 탐색 시작 (BFS)
                queue = deque([(r, c)])
                grid[r][c] = 0 # 방문 표시 (다시 방문하지 않게 0으로 변경)
                count = 1 # 현재 단지의 집 수
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    
                    for i in range(4):
                        nr, nc = curr_r + dr[i], curr_c + dc[i]
                        
                        # 지도의 범위 내에 있고, 아직 방문하지 않은 집이 있다면
                        if 0 <= nr < n and 0 <= nc < n:
                            if grid[nr][nc] == 1:
                                grid[nr][nc] = 0 # 방문 표시
                                count += 1
                                queue.append((nr, nc))
                
                # 하나의 단지 탐색 완료 후 크기 저장
                complex_sizes.append(count)

    # 3. 결과 출력
    # 단지 수 출력
    print(len(complex_sizes))
    
    # 각 단지의 크기를 오름차순으로 정렬하여 출력
    complex_sizes.sort()
    for size in complex_sizes:
        print(size)

if __name__ == "__main__":
    solve()

##################################################################################

