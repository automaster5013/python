import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    N = int(next(it))
    M = int(next(it))
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        t = int(next(it))
        adj[u].append((v, t))
        
    c = [int(next(it)) for _ in range(N)]
    c = [0] + c # 1-indexed
    
    A = int(next(it))
    B = int(next(it))
    
    # 1. 안전한 건물들 간의 슈퍼 에지 생성
    safe_indices = [i for i in range(1, N + 1) if c[i] == 0]
    super_edges = [[] for _ in range(N + 1)]
    
    # 다익스트라용 거리 배열 재사용
    dist_pre = [A + 1] * (N + 1)
    
    for start_node in safe_indices:
        if start_node == N: continue
        
        pq = [(0, start_node)]
        dist_pre[start_node] = 0
        visited = [start_node]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist_pre[u]: continue
            
            # 출발점을 제외한 안전한 건물에 도착하면 슈퍼 에지 추가 후 탐색 중단
            if c[u] == 0 and u != start_node:
                super_edges[start_node].append((u, d))
                continue
            
            for v, t in adj[u]:
                nd = d + t
                if nd <= A and nd < dist_pre[v]:
                    dist_pre[v] = nd
                    heapq.heappush(pq, (nd, v))
                    visited.append(v)
        
        for v in visited: dist_pre[v] = A + 1 # 초기화
    
    # 2. 안전한 건물 그래프에서 최종 다익스트라 실행
    dist_s = [float('inf')] * (N + 1)
    dist_s[1] = 0
    pq_s = [(0, 1)]
    cycle_len = A + B
    
    while pq_s:
        curr_time, u = heapq.heappop(pq_s)
        if curr_time > dist_s[u]: continue
        if u == N:
            print(curr_time)
            return
        
        for v, w in super_edges[u]:
            rem = curr_time % cycle_len
            # 현재 눈을 감은 구간 내에 이동 가능한지 확인
            if rem + w <= A:
                arrival = curr_time + w
            else:
                # 다음 주기가 시작될 때까지 대기 후 이동
                arrival = (curr_time // cycle_len + 1) * cycle_len + w
            
            if arrival < dist_s[v]:
                dist_s[v] = arrival
                heapq.heappush(pq_s, (arrival, v))
                
    print("-1")

if __name__ == "__main__":
    solve()

##########################################################################

