import sys

# 재귀 한도 설정
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    # 5개의 데이터 세트 처리
    for _ in range(5):
        try:
            n = int(next(it))
            m = int(next(it))
        except StopIteration:
            break
            
        parent = list(range(n + 1))
        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY: parent[rootX] = rootY

        relations = []
        for _ in range(m):
            rel, u, v = int(next(it)), int(next(it)), int(next(it))
            if rel == 1:
                union(u, v)
            else:
                relations.append((u, v))

        # 그룹 인원수 계산
        group_size = {}
        for i in range(1, n + 1):
            root = find(i)
            group_size[root] = group_size.get(root, 0) + 1

        # 그룹 간 경쟁 그래프 생성
        adj = {root: [] for root in group_size}
        possible = True
        for u, v in relations:
            rootU = find(u)
            rootV = find(v)
            if rootU == rootV: # 같은 그룹 내 경쟁 관계 존재 시 불가
                possible = False
                break
            adj[rootU].append(rootV)
            adj[rootV].append(rootU)
        
        if not possible:
            print("-1")
            continue

        # 이분 그래프 체크 및 성분별 인원 합 쌍 추출
        visited = {}
        pairs = []
        for root in group_size:
            if root not in visited:
                # BFS/DFS로 2-coloring
                stack = [(root, 0)]
                visited[root] = 0
                comp = [0, 0] # [color 0 인원합, color 1 인원합]
                
                comp_possible = True
                q = [(root, 0)]
                idx = 0
                while idx < len(q):
                    u, color = q[idx]; idx += 1
                    comp[color] += group_size[u]
                    for v in adj[u]:
                        if v not in visited:
                            visited[v] = 1 - color
                            q.append((v, 1 - color))
                        elif visited[v] == color:
                            comp_possible = False
                            break
                    if not comp_possible: break
                
                if not comp_possible:
                    possible = False
                    break
                pairs.append(comp)
        
        if not possible:
            print("-1")
            continue

        # DP (Bitset 최적화)
        # 가능한 총 인원 합의 조합을 비트마스크로 표현
        dp = 1
        for a, b in pairs:
            dp = (dp << a) | (dp << b)
        
        min_diff = n
        # 가능한 모든 인원 합 w에 대해 |2w - n|의 최솟값 탐색
        for w in range(n + 1):
            if (dp >> w) & 1:
                min_diff = min(min_diff, abs(2 * w - n))
        
        print(min_diff)

if __name__ == "__main__":
    solve()

###########################################################################


