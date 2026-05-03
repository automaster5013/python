import sys
from collections import deque

def solve():
    # 빠른 입력을 위한 설정
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 무방향 그래프 (전체 거리용)
    adj = [[] for _ in range(n + 1)]
    # 방향 그래프 (자손용: 부모 -> 자식)
    children = [[] for _ in range(n + 1)]
    
    idx = 1
    for _ in range(n - 1):
        c, p = int(input_data[idx]), int(input_data[idx + 1])
        adj[p].append(c)
        adj[c].append(p)
        children[p].append(c)
        idx += 2
        
    x = int(input_data[idx])

    # 1. 루트(1)와의 거리 계산
    def get_dist_to_root(target):
        q = deque([(1, 0)]) # (현재노드, 거리)
        visited = [False] * (n + 1)
        visited[1] = True
        while q:
            curr, dist = q.popleft()
            if curr == target:
                return dist
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, dist + 1))
        return 0

    # 2 & 3. 자손 노드 개수 및 가장 먼 자손 거리
    # 자손 노드만 탐색하므로 children 리스트 사용
    descendant_count = 0
    max_descendant_dist = 0
    
    q = deque([(x, 0)])
    while q:
        curr, dist = q.popleft()
        descendant_count += 1
        max_descendant_dist = max(max_descendant_dist, dist)
        for nxt in children[curr]:
            q.append((nxt, dist + 1))

    # 4. 전체 노드 중 가장 먼 노드와의 거리
    # 부모 노드로도 올라갈 수 있어야 하므로 무방향 adj 사용
    def get_farthest_dist(start_node):
        q = deque([(start_node, 0)])
        visited = [False] * (n + 1)
        visited[start_node] = True
        max_d = 0
        while q:
            curr, dist = q.popleft()
            max_d = max(max_d, dist)
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, dist + 1))
        return max_d

    # 결과 출력
    print(get_dist_to_root(x))
    print(descendant_count)
    print(max_descendant_dist)
    print(get_farthest_dist(x))

if __name__ == "__main__":
    solve()

#################################################################


