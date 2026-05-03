import sys
from collections import deque

def solve():
    # 대량의 데이터를 한 번에 읽어 처리 속도를 높입니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    if n == 1:
        print(0)
        return
        
    # 인접 리스트 생성 (부모-자식 관계는 무방향 간선으로 처리)
    adj = [[] for _ in range(n + 1)]
    for i in range(1, n):
        # 입력 데이터에서 a, b 쌍을 읽어옵니다.
        u = int(input_data[2*i - 1])
        v = int(input_data[2*i])
        adj[u].append(v)
        adj[v].append(u)

    def bfs(start_node):
        # 거리 배열을 -1로 초기화하여 방문 여부를 동시에 확인합니다.
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = deque([start_node])
        
        farthest_node = start_node
        max_dist = 0
        
        while queue:
            curr = queue.popleft()
            
            # 현재까지 발견된 가장 먼 노드와 거리 정보 갱신
            if distances[curr] > max_dist:
                max_dist = distances[curr]
                farthest_node = curr
                
            for nxt in adj[curr]:
                if distances[nxt] == -1: # 방문하지 않은 노드인 경우
                    distances[nxt] = distances[curr] + 1
                    queue.append(nxt)
                    
        return farthest_node, max_dist

    # 1. 임의의 노드(1번)에서 가장 먼 노드 u를 찾습니다.
    node_u, _ = bfs(1)
    
    # 2. 노드 u에서 다시 가장 먼 노드 v를 찾고 그 거리를 구합니다.
    node_v, diameter = bfs(node_u)
    
    # 최종 지름 출력
    print(diameter)

if __name__ == "__main__":
    # N=100,000이므로 RecursionError 위험이 있는 DFS보다 
    # 반복문 기반의 BFS를 사용하는 것이 안전합니다.
    solve()

#########################################################################



