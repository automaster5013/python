import sys
from collections import deque

def solve():
    # 1. 빠른 입력 및 초기화
    input_data = sys.stdin.read().split()
    if not input_data: return
    m, n = int(input_data[0]), int(input_data[1])
    grid = [list(map(int, input_data[i*n + 2 : (i+1)*n + 2])) for i in range(m)]

    # 2. 연결 성분 라벨링
    visited_comp = [[False] * n for _ in range(m)]
    comp_map = [[-1] * n for _ in range(m)]
    comp_id = 0
    for r in range(m):
        for c in range(n):
            if not visited_comp[r][c]:
                color, q = grid[r][c], deque([(r, c)])
                visited_comp[r][c] = True
                while q:
                    curr_r, curr_c = q.popleft()
                    comp_map[curr_r][curr_c] = comp_id
                    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < m and 0 <= nc < n and not visited_comp[nr][nc] and grid[nr][nc] == color:
                            visited_comp[nr][nc] = True
                            q.append((nr, nc))
                comp_id += 1

    if comp_id <= 1: print(0); return

    # 3. 인접 리스트 생성
    adj = [set() for _ in range(comp_id)]
    for r in range(m):
        for c in range(n):
            u = comp_map[r][c]
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    v = comp_map[nr][nc]
                    if u != v:
                        adj[u].add(v); adj[v].add(u)
    adj = [list(s) for s in adj]

    # 4. 지름 양 끝점 A, B 찾기 (2-BFS)
    def get_dists(start_node):
        dists = [-1] * comp_id
        dists[start_node], q = 0, deque([start_node])
        farthest_node, max_d = start_node, 0
        while q:
            u = q.popleft()
            if dists[u] > max_d: max_d, farthest_node = dists[u], u
            for v in adj[u]:
                if dists[v] == -1:
                    dists[v] = dists[u] + 1
                    q.append(v)
        return farthest_node, dists

    node_a, _ = get_dists(0)
    node_b, dists_a = get_dists(node_a)
    _, dists_b = get_dists(node_b)

    # 5. 전략적 BFS 및 강력한 가지치기
    # 하한선(max(dist_a, dist_b))이 낮은 순서대로 정렬하여 좋은 후보부터 탐색
    candidates = sorted(range(comp_id), key=lambda x: max(dists_a[x], dists_b[x]))
    
    min_radius = float('inf')
    visited = [-1] * comp_id
    
    for i in candidates:
        # 하한선 가지치기: 현재 노드의 최소 가능 이심률이 이미 찾은 반지름보다 크면 스킵
        if max(dists_a[i], dists_b[i]) >= min_radius:
            continue
            
        # 최적화된 BFS (레벨 단위)
        curr_q = [i]
        visited[i] = i
        dist = 0
        while curr_q:
            if dist >= min_radius: break
            next_q = []
            for u in curr_q:
                for v in adj[u]:
                    if visited[v] != i:
                        visited[v] = i
                        next_q.append(v)
            if not next_q: break
            curr_q = next_q
            dist += 1
            
        if dist < min_radius:
            min_radius = dist
            
    print(min_radius)

solve()

###########################################################################################3


