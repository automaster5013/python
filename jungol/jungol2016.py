import sys

def solve():
    # 6x6 그리드 입력
    grid = []
    for _ in range(6):
        line = sys.stdin.readline().split()
        if not line: break
        grid.append(list(map(int, line)))

    # 전개도 내의 면 위치 찾기
    faces = {}
    start_pos = None
    for r in range(6):
        for c in range(6):
            if grid[r][c] != 0:
                faces[grid[r][c]] = (r, c)
                if start_pos is None:
                    start_pos = (r, c)

    if len(faces) != 6:
        print(0)
        return

    # 방향 벡터 정의 (x, y, z)
    # 초기값: 정면(Normal)=(0,0,1), 위(Up)=(0,1,0), 오른쪽(Right)=(1,0,0)
    # result[방향벡터] = 면의 숫자
    result = {}
    visited = [[False] * 6 for _ in range(6)]

    def neg(v):
        return (-v[0], -v[1], -v[2])

    def dfs(r, c, normal, up, right):
        num = grid[r][c]
        if normal in result: # 이미 해당 방향에 다른 면이 할당된 경우
            return False
        result[normal] = num
        visited[r][c] = True

        # 상, 하, 좌, 우 탐색
        directions = [
            (-1, 0, up, neg(normal), right),    # 위로 이동
            (1, 0, neg(up), normal, right),     # 아래로 이동
            (0, -1, neg(right), up, normal),    # 왼쪽으로 이동
            (0, 1, right, up, neg(normal))      # 오른쪽으로 이동
        ]

        for dr, dc, n_normal, n_up, n_right in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 6 and 0 <= nc < 6 and grid[nr][nc] != 0 and not visited[nr][nc]:
                if not dfs(nr, nc, n_normal, n_up, n_right):
                    return False
        return True

    # 탐색 시작 (첫 번째 발견된 면을 기준면으로 설정)
    sr, sc = start_pos
    if not dfs(sr, sc, (0, 0, 1), (0, 1, 0), (1, 0, 0)):
        print(0)
        return

    # 6개 면이 모두 채워졌는지 확인
    if len(result) != 6:
        print(0)
        return

    # 1번 면의 반대편 찾기
    # 1번 면의 벡터를 찾고 그 역벡터의 숫자를 출력
    vec1 = None
    for v, n in result.items():
        if n == 1:
            vec1 = v
            break
    
    opposite_vec = neg(vec1)
    if opposite_vec in result:
        print(result[opposite_vec])
    else:
        print(0)

if __name__ == "__main__":
    solve()

##########################################################



