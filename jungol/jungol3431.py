import sys

# 재귀 깊이 제한 설정 (DSU 및 세그먼트 트리용)
sys.setrecursionlimit(300000)

def solve():
    # 전체 입력을 한 번에 읽어와 속도 향상
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    logs = []
    x_coords = []
    curr = 2
    for i in range(N):
        x1 = int(input_data[curr])
        x2 = int(input_data[curr+1])
        y = int(input_data[curr+2])
        logs.append([x1, x2, y, i + 1])
        x_coords.append(x1)
        x_coords.append(x2)
        curr += 3
        
    # 좌표 압축 (x 좌표 범위가 10^9이므로)
    unique_x = sorted(list(set(x_coords)))
    x_map = {x: i for i, x in enumerate(unique_x)}
    M = len(unique_x)
    
    # y 좌표 순으로 정렬
    logs.sort(key=lambda x: x[2])
    
    # DSU (Disjoint Set Union) 초기화
    parent = list(range(N + 1))
    def find(i):
        root = i
        while parent[root] != root:
            root = parent[root]
        while parent[i] != root:
            nxt = parent[i]
            parent[i] = root
            i = nxt
        return root

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    # 세그먼트 트리: 특정 구간의 로그 번호를 관리
    # tree[v] > 0: 구간 전체가 해당 로그 번호로 덮임
    # tree[v] == 0: 로그 없음
    # tree[v] == -1: 하위 노드에 서로 다른 로그들이 섞여 있음
    tree = [0] * (4 * M)

    def query_and_union(v, tl, tr, l, r, log_id):
        if l > r: return
        if tree[v] != -1:
            if tree[v] != 0:
                union(tree[v], log_id)
            return
        if tl == tr: return
        tm = (tl + tr) // 2
        query_and_union(2*v, tl, tm, l, min(r, tm), log_id)
        query_and_union(2*v+1, tm+1, tr, max(l, tm+1), r, log_id)

    def update(v, tl, tr, l, r, log_id):
        if l > r: return
        if l == tl and r == tr:
            tree[v] = log_id
            return
        if tree[v] != -1:
            tree[2*v] = tree[2*v+1] = tree[v]
            tree[v] = -1
        tm = (tl + tr) // 2
        update(2*v, tl, tm, l, min(r, tm), log_id)
        update(2*v+1, tm+1, tr, max(l, tm+1), r, log_id)
        if tree[2*v] == tree[2*v+1] and tree[2*v] != -1:
            tree[v] = tree[2*v]
        else:
            tree[v] = -1

    # 스위핑 수행
    for x1, x2, y, log_id in logs:
        idx1, idx2 = x_map[x1], x_map[x2]
        query_and_union(1, 0, M - 1, idx1, idx2, log_id)
        update(1, 0, M - 1, idx1, idx2, log_id)
    
    # 쿼리 처리
    results = []
    for _ in range(Q):
        u = int(input_data[curr])
        v = int(input_data[curr+1])
        curr += 2
        if find(u) == find(v):
            results.append("1")
        else:
            results.append("0")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

##############################################################

