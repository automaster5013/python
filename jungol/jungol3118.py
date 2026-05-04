import sys
import heapq

def solve():
    # 대량의 데이터를 빠르게 읽어오기 위한 설정
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # 인접 리스트 생성
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        
    # 최단 거리 테이블을 무한대로 초기화
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    
    # 우선순위 큐 (거리, 현재 노드)
    pq = [(0, 1)]
    
    while pq:
        d, curr = heapq.heappop(pq)
        
        # 이미 처리된 적 있는 노드라면 무시
        if dist[curr] < d:
            continue
            
        for neighbor, weight in adj[curr]:
            cost = d + weight
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor))
                
    # 1번에서 N번 정점까지의 최단 경로 값 출력
    print(dist[n])

if __name__ == "__main__":
    solve()

##############################################################################3



