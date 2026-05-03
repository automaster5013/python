import sys
from collections import deque

def solve():
    # 입력 처리 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))  # 가수 수
    m = int(next(it))  # 보조 PD 수
    
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    # 그래프 구축
    for _ in range(m):
        count = int(next(it))
        path = [int(next(it)) for _ in range(count)]
        for i in range(count - 1):
            u, v = path[i], path[i+1]
            adj[u].append(v)
            in_degree[v] += 1
            
    # 위상 정렬 시작 (진입 차수가 0인 가수들 큐에 삽입)
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    result = []
    
    while queue:
        curr = queue.popleft()
        result.append(curr)
        
        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    # 모든 가수가 포함되었는지 확인하여 사이클 유무 판별
    if len(result) == n:
        for singer in result:
            print(singer)
    else:
        print(0)

if __name__ == "__main__":
    solve()

##############################################################################


