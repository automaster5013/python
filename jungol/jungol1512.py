import sys

# 재귀 한도 설정
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n, m = int(input_data[0]), int(input_data[1])
    k = int(input_data[2])
    grid = []
    all_values = []
    idx = 3
    for i in range(n):
        row = list(map(int, input_data[idx:idx+m]))
        grid.append(row)
        all_values.extend(row)
        idx += m
    
    # 이진 탐색을 위한 값 정렬 및 중복 제거
    sorted_vals = sorted(list(set(all_values)))
    
    def get_min_vertex_cover(limit_val):
        adj = [[] for _ in range(n)]
        edges = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] > limit_val:
                    adj[i].append(j)
                    edges.append((i, j))
        
        if not edges: return 0, [], []
        
        # 이분 매칭 (Hopcroft-Karp 대신 간단한 DFS 사용)
        match_l = [-1] * n
        match_r = [-1] * m
        
        def dfs(u, visited):
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if match_r[v] == -1 or dfs(match_r[v], visited):
                        match_r[v] = u
                        match_l[u] = v
                        return True
            return False

        matching_count = 0
        for i in range(n):
            visited = [False] * m
            if dfs(i, visited):
                matching_count += 1
        
        if matching_count > k:
            return matching_count, [], []
            
        # 최소 정점 커버 추출 (Konig's Theorem Constructive Proof)
        visited_l = [False] * n
        visited_r = [False] * m
        
        def mark_dfs(u):
            visited_l[u] = True
            for v in adj[u]:
                if not visited_r[v] and match_l[u] != v:
                    visited_r[v] = True
                    if match_r[v] != -1:
                        mark_dfs(match_r[v])
        
        # 매칭되지 않은 왼쪽 정점에서 시작
        for i in range(n):
            if match_l[i] == -1:
                mark_dfs(i)
        
        # 최소 정점 커버: (방문하지 않은 왼쪽 정점) + (방문한 오른쪽 정점)
        rows = [i + 1 for i in range(n) if not visited_l[i]]
        cols = [j + 1 for j in range(m) if visited_r[j]]
        
        return len(rows) + len(cols), rows, cols

    # 매개 변수 이진 탐색
    low = 0
    high = len(sorted_vals) - 1
    best_x = sorted_vals[-1]
    final_rows, final_cols = [], []
    
    while low <= high:
        mid = (low + high) // 2
        count, rows, cols = get_min_vertex_cover(sorted_vals[mid])
        
        if count <= k:
            best_x = sorted_vals[mid]
            final_rows, final_cols = rows, cols
            high = mid - 1
        else:
            low = mid + 1
            
    # 출력 요구사항: R + C = K를 맞춰야 하므로 부족한 개수만큼 임의의 행/열 추가
    # (이미 선택되지 않은 번호 중에서 추가)
    while len(final_rows) + len(final_cols) < k:
        added = False
        for i in range(1, n + 1):
            if i not in final_rows:
                final_rows.append(i)
                added = True
                break
            if len(final_rows) + len(final_cols) == k: break
        if added and len(final_rows) + len(final_cols) == k: break
        for j in range(1, m + 1):
            if j not in final_cols:
                final_cols.append(j)
                added = True
                break
            if len(final_rows) + len(final_cols) == k: break

    print(best_x)
    print(len(final_rows), *sorted(final_rows))
    print(len(final_cols), *sorted(final_cols))

solve()

################################################################################

