import sys

# 빠른 입출력을 위해 sys.stdin.read 사용
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    
    N = int(next(it))
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        
    # BFS를 이용한 부모 노드 찾기
    parent = [0] * (N + 1)
    bfs_q = [1]
    parent[1] = -1  # 루트 표시
    idx = 0
    while idx < len(bfs_q):
        u = bfs_q[idx]
        idx += 1
        for v in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                bfs_q.append(v)
    
    is_in_S = [False] * (N + 1)
    dsu_parent = list(range(N + 1))
    dsu_sz = [1] * (N + 1)
    
    # DSU find 함수 (경로 압축)
    def find(i):
        root = i
        while dsu_parent[root] != root:
            root = dsu_parent[root]
        while dsu_parent[i] != root:
            new_i = dsu_parent[i]
            dsu_parent[i] = root
            i = new_i
        return root

    # DSU union 함수 (크기 기반 합치기)
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if dsu_sz[root_i] < dsu_sz[root_j]:
                root_i, root_j = root_j, root_i
            dsu_parent[root_j] = root_i
            dsu_sz[root_i] += dsu_sz[root_j]

    Q_count = int(next(it))
    results = []
    for _ in range(Q_count):
        K = int(next(it))
        S = [int(next(it)) for _ in range(K)]
        
        for s in S:
            is_in_S[s] = True
        
        # 부모가 S에 속해 있으면 연결
        for s in S:
            p = parent[s]
            if p != -1 and is_in_S[p]:
                union(s, p)
        
        # 연결 요소의 크기를 이용한 강도 계산
        ans = 0
        for s in S:
            if dsu_parent[s] == s:
                c = dsu_sz[s]
                ans += c * (c - 1) // 2
        results.append(str(ans))
        
        # 다음 질의를 위한 효율적인 초기화
        for s in S:
            is_in_S[s] = False
            dsu_parent[s] = s
            dsu_sz[s] = 1
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

##########################################################

