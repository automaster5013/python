import sys

# 빠른 입출력
input = sys.stdin.readline

def solve():
    line = input().split()
    if not line: return
    n = int(line[0])

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, c = map(int, input().split())
        w = 1 if c == 1 else -1
        adj[u].append((v, w))
        adj[v].append((u, w))

    removed = [False] * (n + 1)
    sz = [0] * (n + 1)
    offset = n
    # cnt[거리][0:내부휴식지없음, 1:내부휴식지있음]
    cnt = [[0, 0] for _ in range(2 * n + 1)]
    ans = 0

    def get_sz(root):
        stack = [(root, -1)]
        order = []
        while stack:
            u, p = stack.pop()
            order.append((u, p))
            sz[u] = 1
            for v, w in adj[u]:
                if v != p and not removed[v]:
                    stack.append((v, u))
        for u, p in reversed(order):
            if p != -1: sz[p] += sz[u]
        return sz[root]

    def get_centroid(u, total):
        curr, p = u, -1
        while True:
            heavy = -1
            for v, w in adj[curr]:
                if v != p and not removed[v] and sz[v] > total // 2:
                    heavy = v
                    break
            if heavy == -1: return curr
            p, curr = curr, heavy

    # 현재 경로상에 나타난 거리들의 빈도 (내부 휴식지 체크용)
    # seen_dist[0]은 무게 중심 C를 의미하므로 1로 시작
    seen_dist = [0] * (2 * n + 1)

    def collect_paths(start_node, start_w):
        # (현재노드, 부모, 누적거리, 백트래킹여부)
        stack = [(start_node, -1, start_w, False)]
        res = []
        seen_dist[0 + offset] = 1 # Centroid(거리 0) 표시
        
        while stack:
            u, p, d, backtrack = stack.pop()
            if backtrack:
                seen_dist[d + offset] -= 1
                continue
            
            # 1. 무게 중심 C를 중간 발판으로 쓸 수 있는가? 
            # (즉, 나를 제외한 조상 중에 나와 같은 누적거리가 있는가?)
            f1 = (seen_dist[d + offset] > 0)
            
            # 2. C를 제외하고 내부에 합이 0인 지점이 있는가?
            # (즉, C를 제외한 조상 중 누적거리가 0인 지점이 있는가?)
            f2 = (seen_dist[0 + offset] > 1)
            
            res.append((d, f1, f2))
            
            stack.append((u, p, d, True))
            seen_dist[d + offset] += 1
            for v, w in adj[u]:
                if v != p and not removed[v]:
                    stack.append((v, u, d + w, False))
        
        seen_dist[0 + offset] = 0 # 초기화
        return res

    def decompose(u):
        nonlocal ans
        total = get_sz(u)
        if total < 2: return
        
        c = get_centroid(u, total)
        removed[c] = True
        
        active_indices = []
        # 무게 중심을 지나는 경로 조합
        for v, w in adj[c]:
            if not removed[v]:
                subtree = collect_paths(v, w)
                for d, f1, f2 in subtree:
                    target = -d + offset
                    # 매칭되는 상대편 노드 찾기
                    if f1:
                        # 내가 이미 휴식지가 있다면(f1), 상대는 합만 0이면 됨
                        ans += cnt[target][0] + cnt[target][1]
                    else:
                        # 내가 없다면, 상대가 휴식지(f1)를 가지고 있어야 함
                        ans += cnt[target][1]
                    
                    # 무게 중심 C를 시작점으로 하는 경로 (C-u)
                    if d == 0 and f2:
                        ans += 1
                
                # 현재 서브트리 데이터를 카운트 배열에 업데이트
                for d, f1, f2 in subtree:
                    cnt[d + offset][1 if f1 else 0] += 1
                    active_indices.append(d + offset)

        # 사용한 부분만 0으로 리셋
        for idx in active_indices:
            cnt[idx][0] = cnt[idx][1] = 0
        
        for v, w in adj[c]:
            if not removed[v]:
                decompose(v)

    decompose(1)
    print(ans)

solve()

