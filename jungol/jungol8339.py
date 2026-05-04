import heapq
import sys

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))  # 목초지 수
    m = int(next(it))  # 길의 수
    k = int(next(it))  # 정비 가능한 최대 길의 수
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        t = int(next(it))
        # 양방향 도로 설정
        adj[u].append((v, t))
        adj[v].append((u, t))
        
    # dist[used_k][node]: 사용한 k번의 정비 횟수와 현재 노드에 따른 최단 거리
    dist = [[float('inf')] * (n + 1) for _ in range(k + 1)]
    
    # 시작점 설정: 0번 정비, 1번 목초지
    dist[0][1] = 0
    pq = [(0, 0, 1)] # (비용, 사용한 k, 현재 노드)
    
    while pq:
        curr_w, used_k, curr_n = heapq.heappop(pq)
        
        # 이미 처리된 최단 거리라면 무시
        if curr_w > dist[used_k][curr_n]:
            continue
            
        for next_n, weight in adj[curr_n]:
            # 1. 정비를 사용하지 않고 이동하는 경우 (동일 층 이동)
            if dist[used_k][next_n] > curr_w + weight:
                dist[used_k][next_n] = curr_w + weight
                heapq.heappush(pq, (dist[used_k][next_n], used_k, next_n))
            
            # 2. 정비를 사용하여 이동하는 경우 (다음 층으로 이동)
            if used_k < k:
                if dist[used_k + 1][next_n] > curr_w:
                    dist[used_k + 1][next_n] = curr_w
                    heapq.heappush(pq, (dist[used_k + 1][next_n], used_k + 1, next_n))
                    
    # N번 목초지에 도달하는 모든 경우(0~k번 정비) 중 최솟값 출력
    ans = float('inf')
    for i in range(k + 1):
        ans = min(ans, dist[i][n])
    print(ans)

if __name__ == "__main__":
    solve()

##############################################################################################



