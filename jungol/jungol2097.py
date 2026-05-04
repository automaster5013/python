import sys

def solve():
    # 데이터 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 지하철역의 수
    m = int(input_data[1]) # 목적역 번호
    
    # 인접 행렬 입력 받기
    adj = []
    idx = 2
    for i in range(n):
        adj.append(list(map(int, input_data[idx : idx + n])))
        idx += n
        
    # 다익스트라 초기화
    dist = [float('inf')] * (n + 1)
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    dist[1] = 0 # 출발역(1번) 거리 0
    
    for _ in range(n):
        # 1. 방문하지 않은 역 중 거리가 가장 짧은 역 선택
        min_val = float('inf')
        curr = -1
        for i in range(1, n + 1):
            if not visited[i] and dist[i] < min_val:
                min_val = dist[i]
                curr = i
        
        if curr == -1: # 더 이상 갈 수 있는 역이 없음
            break
            
        visited[curr] = True
        
        # 목적지에 도달했더라도 다른 경로가 더 짧을 수 있으므로 전체 갱신
        # 2. 선택된 역을 거쳐가는 것이 더 빠른 경우 거리 갱신
        for next_node in range(1, n + 1):
            weight = adj[curr - 1][next_node - 1]
            if dist[curr] + weight < dist[next_node]:
                dist[next_node] = dist[curr] + weight
                parent[next_node] = curr # 경로 기록
                
    # 결과 출력 1: 목적지까지의 최소 시간
    print(dist[m])
    
    # 결과 출력 2: 경로 역추적
    path = []
    temp = m
    while temp != 0:
        path.append(temp)
        temp = parent[temp]
        
    print(*(path[::-1])) # 역순으로 출력하여 출발지부터 표시

if __name__ == "__main__":
    solve()

#############################################################################3



