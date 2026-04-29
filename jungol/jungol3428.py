import sys
from collections import deque

def solve():
    # 고속 입력
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    m = int(input[1])
    x = int(input[2])
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    
    ptr = 3
    for _ in range(m):
        u = int(input[ptr])
        v = int(input[ptr+1])
        # u가 v보다 잘함: u -> v
        adj[u].append(v)
        # 역방향: v -> u (나보다 잘한 사람 찾기용)
        rev_adj[v].append(u)
        ptr += 2

    def count_reachable(start_node, graph):
        q = deque([start_node])
        visited = [False] * (n + 1)
        visited[start_node] = True
        count = 0
        
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += 1
                    q.append(neighbor)
        return count

    # 나보다 확실히 잘한 사람 수
    better_than_x = count_reachable(x, rev_adj)
    # 나보다 확실히 못한 사람 수
    worse_than_x = count_reachable(x, adj)
    
    # 최상 등수: 나보다 잘한 사람 수 + 1
    # 최하 등수: 전체 인원 - 나보다 못한 사람 수
    print(1 + better_than_x, n - worse_than_x)

if __name__ == "__main__":
    solve()

######################################################


