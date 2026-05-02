import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(300000)

def solve():
    # 빠른 입력을 위해 전체를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    M = int(input_data[ptr]); ptr += 1
    
    # 1. DSU를 활용한 MST 구축
    parent = list(range(N + 1))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    adj = [[] for _ in range(N + 1)]
    for x in range(1, M + 1):
        u = int(input_data[ptr]); ptr += 1
        v = int(input_data[ptr]); ptr += 1
        # 가중치 2^x 순서대로(입력 순서대로) MST 구성
        if union(u, v):
            adj[u].append(v)
            adj[v].append(u)

    # 2. LCA 및 깊이(Depth) 계산을 위한 준비
    LOG = 18
    depth = [-1] * (N + 1)
    up = [[0] * (N + 1) for _ in range(LOG + 1)]

    # 비재귀 BFS로 트리 순회 및 깊이 설정
    queue = [1]
    depth[1] = 0
    while queue:
        u = queue.pop()
        for v in adj[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                up[0][v] = u
                queue.append(v)

    # LCA Sparse Table 구축
    for i in range(1, LOG + 1):
        for v in range(1, N + 1):
            up[i][v] = up[i-1][up[i-1][v]]

    def get_lca(u, v):
        if depth[u] < depth[v]: u, v = v, u
        for i in range(LOG, -1, -1):
            if depth[u] - (1 << i) >= depth[v]:
                u = up[i][u]
        if u == v: return u
        for i in range(LOG, -1, -1):
            if up[i][u] != up[i][v]:
                u = up[i][u]
                v = up[i][v]
        return up[0][u]

    # 3. 질의 처리
    Q = int(input_data[ptr]); ptr += 1
    results = []
    for _ in range(Q):
        s = int(input_data[ptr]); ptr += 1
        e = int(input_data[ptr]); ptr += 1
        
        lca = get_lca(s, e)
        # 트리 상의 거리: depth(s) + depth(e) - 2 * depth(lca)
        dist = depth[s] + depth[e] - 2 * depth[lca]
        # 중간 노드 수: 거리 - 1
        results.append(str(dist - 1))

    # 결과 일괄 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

###################################################################



