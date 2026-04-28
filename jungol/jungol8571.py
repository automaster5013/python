import sys

# 1. 고속 입출력 및 로컬 변수 활용을 위한 함수화
def main():
    input = sys.stdin.read().split()
    if not input: return
    
    ptr = 0
    n = int(input[ptr]); ptr += 1
    q = int(input[ptr]); ptr += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(input[ptr]); ptr += 1
        v = int(input[ptr]); ptr += 1
        w = int(input[ptr]); ptr += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # 2. BFS로 트리 정보 전처리 (메모리 절약형)
    depth = [-1] * (n + 1)
    dist_1 = [0] * (n + 1)
    parent = [[0] * 18 for _ in range(n + 1)]
    
    queue = [1]
    depth[1] = 0
    for u in queue:
        for v, w in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                dist_1[v] = dist_1[u] + w
                parent[v][0] = u
                queue.append(v)
    
    # Sparse Table (Binary Lifting)
    for j in range(1, 18):
        for i in range(1, n + 1):
            p = parent[i][j-1]
            if p: parent[i][j] = parent[p][j-1]

    def get_lca(u, v):
        if depth[u] < depth[v]: u, v = v, u
        diff = depth[u] - depth[v]
        for j in range(18):
            if (diff >> j) & 1: u = parent[u][j]
        if u == v: return u
        for j in range(17, -1, -1):
            if parent[u][j] != parent[v][j]:
                u = parent[u][j]
                v = parent[v][j]
        return parent[u][0]

    # 3. 구간 계산 및 좌표 압축
    target_dist = dist_1[n]
    scenario_intervals = []
    robots_log = {}
    coords = {0, target_dist}
    
    query_ptr = ptr
    for i in range(1, q + 1):
        type = int(input[query_ptr]); query_ptr += 1
        if type == 1:
            aj = int(input[query_ptr]); query_ptr += 1
            bj = int(input[query_ptr]); query_ptr += 1
            pr = get_lca(aj, n)
            dist_to_path = dist_1[aj] - dist_1[pr]
            radius = bj - dist_to_path
            if radius >= 0:
                l_val = max(0, dist_1[pr] - radius)
                r_val = min(target_dist, dist_1[pr] + radius)
                if l_val < r_val:
                    scenario_intervals.append((1, l_val, r_val))
                    robots_log[i] = (l_val, r_val)
                    coords.add(l_val); coords.add(r_val)
                    continue
            scenario_intervals.append((1, None, None))
            robots_log[i] = None
        else:
            cj = int(input[query_ptr]); query_ptr += 1
            interval = robots_log[cj]
            scenario_intervals.append((2, interval[0] if interval else None, interval[1] if interval else None))

    # 좌표 압축 완료
    sorted_coords = sorted(list(coords))
    coord_map = {val: idx for idx, val in enumerate(sorted_coords)}
    m = len(sorted_coords)
    
    # 4. 세그먼트 트리 최적화 (배열만 사용)
    num_nodes = 1
    while num_nodes < m: num_nodes *= 2
    
    tree_cnt = [0] * (2 * num_nodes)
    tree_len = [0] * (2 * num_nodes)
    # 각 노드가 담당하는 실제 길이 미리 계산 (속도 향상 핵심)
    node_full_len = [0] * (2 * num_nodes)
    for i in range(m - 1):
        node_full_len[num_nodes + i] = sorted_coords[i+1] - sorted_coords[i]
    for i in range(num_nodes - 1, 0, -1):
        node_full_len[i] = node_full_len[2*i] + node_full_len[2*i+1]

    # 하향식 업데이트 (재귀를 쓰되 최소한으로)
    def update(node, start, end, l, r, val):
        if l <= start and end <= r:
            tree_cnt[node] += val
        else:
            mid = (start + end) // 2
            if l <= mid: update(node * 2, start, mid, l, r, val)
            if r > mid: update(node * 2 + 1, mid + 1, end, l, r, val)
            
        if tree_cnt[node] > 0:
            tree_len[node] = node_full_len[node]
        else:
            if node < num_nodes:
                tree_len[node] = tree_len[2*node] + tree_len[2*node+1]
            else:
                tree_len[node] = 0

    # 5. 최종 시뮬레이션
    results = []
    for t, l, r in scenario_intervals:
        if l is not None:
            update(1, 0, num_nodes - 1, coord_map[l], coord_map[r] - 1, 1 if t == 1 else -1)
        results.append("YES" if tree_len[1] == target_dist else "NO")
    
    sys.stdout.write("\n".join(results) + "\n")

main()

####################################################################################################


