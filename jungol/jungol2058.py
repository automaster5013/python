import sys
from collections import deque

def solve():
    # 모든 입력 데이터를 한 번에 읽어 처리 속도를 높입니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    try:
        n = int(next(it))
        # 고돌이와 고소미의 시작 및 집 위치 (0-indexed로 변환)
        r1, c1, hr1, hc1 = [int(next(it)) - 1 for _ in range(4)]
        r2, c2, hr2, hc2 = [int(next(it)) - 1 for _ in range(4)]
        
        # 격자 정보 (0: 이동 가능, 1: 웅덩이)
        grid = []
        for _ in range(n):
            grid.append([int(next(it)) for _ in range(n)])
    except (StopIteration, ValueError):
        return

    n_sq = n * n
    
    # 1차원 좌표로 변환 (r, c) -> r * n + c
    start1, home1 = r1 * n + c1, hr1 * n + hc1
    start2, home2 = r2 * n + c2, hr2 * n + hc2

    # 1. 각 칸에서 가능한 이동 경로(8방향 + 제자리) 미리 계산
    moves_diff = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]
    adj = [[] for _ in range(n_sq)]
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1: continue
            p = r * n + c
            for dr, dc in moves_diff:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    adj[p].append(nr * n + nc)

    # 2. 가시 영역(Thorn constraint) 체크 매트릭스 미리 계산
    # is_safe[p1][p2]가 1이면 두 고슴도치가 서로의 가시 범위 밖에 있는 안전한 상태입니다.
    is_safe = [bytearray(n_sq) for _ in range(n_sq)]
    for p1 in range(n_sq):
        r1_c, c1_c = divmod(p1, n)
        for p2 in range(n_sq):
            r2_c, c2_c = divmod(p2, n)
            if abs(r1_c - r2_c) > 1 or abs(c1_c - c2_c) > 1:
                is_safe[p1][p2] = 1

    # 3. BFS 탐색
    if start1 == home1 and start2 == home2:
        print(0)
        return

    q = deque([(start1, start2, 0)])
    visited = bytearray(n_sq * n_sq)
    visited[start1 * n_sq + start2] = 1
    
    popleft = q.popleft
    append = q.append
    
    while q:
        p1, p2, dist = popleft()
        d_next = dist + 1
        
        # 고돌이의 다음 이동 후보
        for np1 in adj[p1]:
            v_idx_offset = np1 * n_sq
            safe_row = is_safe[np1]
            # 고소미의 다음 이동 후보
            for np2 in adj[p2]:
                # 가시 제약 조건 확인
                if safe_row[np2]:
                    v_idx = v_idx_offset + np2
                    if not visited[v_idx]:
                        # 두 고슴도치가 모두 집에 도착했는지 확인
                        if np1 == home1 and np2 == home2:
                            print(d_next)
                            return
                        visited[v_idx] = 1
                        append((np1, np2, d_next))

if __name__ == '__main__':
    solve()

##########################################################################



