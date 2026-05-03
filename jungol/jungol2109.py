import sys
import heapq

def dijkstra(n, start_node, adj):
    # 최단 거리를 무한대로 초기화
    distances = [float('inf')] * (n + 1)
    distances[start_node] = 0
    pq = [(0, start_node)]
    
    while pq:
        dist, curr = heapq.heappop(pq)
        
        if distances[curr] < dist:
            continue
            
        for neighbor, weight in adj[curr]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                
    return distances

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 마을 수
    m = int(input_data[1]) # 도로 수
    x = int(input_data[2]) # 파티 장소
    
    # 정방향 그래프와 역방향 그래프 구성
    adj_original = [[] for _ in range(n + 1)]
    adj_reversed = [[] for _ in range(n + 1)]
    
    ptr = 3
    for _ in range(m):
        u, v, t = int(input_data[ptr]), int(input_data[ptr+1]), int(input_data[ptr+2])
        adj_original[u].append((v, t))
        adj_reversed[v].append((u, t))
        ptr += 3
        
    # 2. 다익스트라 실행
    # dist_return: X에서 각 마을로 돌아오는 최단 시간 (X -> i)
    dist_return = dijkstra(n, x, adj_original)
    
    # dist_go: 각 마을에서 X로 가는 최단 시간 (i -> X)
    # 역방향 그래프에서 X를 시작점으로 돌리면 원래 그래프의 i -> X와 같음
    dist_go = dijkstra(n, x, adj_reversed)
    
    # 3. 최댓값 찾기
    max_total_time = 0
    for i in range(1, n + 1):
        if dist_go[i] != float('inf') and dist_return[i] != float('inf'):
            max_total_time = max(max_total_time, dist_go[i] + dist_return[i])
            
    print(max_total_time)

if __name__ == "__main__":
    solve()

##########################################################################################



