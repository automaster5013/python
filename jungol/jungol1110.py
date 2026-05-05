import sys
from collections import deque

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0]) # 파이프 수
    N = int(input_data[1]) # 마을 수
    
    # 인접 행렬로 용량 관리 (마을 번호가 1~N이므로 N+1 크기)
    # 마을 사이에 여러 개의 파이프가 있을 수 있으므로 누적합으로 저장
    capacity = [[0] * (N + 1) for _ in range(N + 1)]
    adj = [[] for _ in range(N + 1)]
    
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        
        # 유량 네트워크 구성을 위해 인접 리스트와 용량 설정
        if capacity[u][v] == 0:
            adj[u].append(v)
            adj[v].append(u) # 역방향 간선 추가
        capacity[u][v] += w
    
    total_flow = 0
    source = 1
    sink = N
    
    while True:
        # BFS를 위한 부모 노드 기록 배열
        parent = [-1] * (N + 1)
        queue = deque([source])
        parent[source] = source
        
        while queue:
            curr = queue.popleft()
            for next_node in adj[curr]:
                # 방문하지 않았고 잔여 용량이 남아있는 경우
                if parent[next_node] == -1 and capacity[curr][next_node] > 0:
                    parent[next_node] = curr
                    queue.append(next_node)
                    if next_node == sink:
                        break
            if parent[sink] != -1:
                break
        
        # 더 이상 증가 경로가 없으면 종료
        if parent[sink] == -1:
            break
            
        # 경로 상의 최소 잔여 용량 찾기
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
            
        # 잔여 용량 업데이트
        s = sink
        while s != source:
            p = parent[s]
            capacity[p][s] -= path_flow
            capacity[s][p] += path_flow # 역방향 유량 추가
            s = p
            
        total_flow += path_flow
        
    print(total_flow)

if __name__ == "__main__":
    solve()

#####################################################################################

