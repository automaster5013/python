import sys
from collections import deque

def solve():
    # 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 정방향(큰 학생 찾기)과 역방향(작은 학생 찾기) 인접 리스트
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        adj[u].append(v)
        rev_adj[v].append(u)
        ptr += 2

    # 특정 그래프에서 start 노드로부터 도달 가능한 노드 수를 세는 함수
    def count_reachable(start, graph):
        q = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        count = 0
        
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += 1
                    q.append(neighbor)
        return count

    answer = 0
    # 모든 학생에 대해 전수 조사
    for i in range(1, n + 1):
        taller_count = count_reachable(i, adj)      # 나보다 큰 사람
        shorter_count = count_reachable(i, rev_adj) # 나보다 작은 사람
        
        # 합이 N-1이면 내 위치가 고정됨
        if taller_count + shorter_count == n - 1:
            answer += 1
            
    print(answer)

if __name__ == "__main__":
    solve()

###########################################################################

