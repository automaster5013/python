import heapq
import sys

def solve():
    # 표준 입력으로부터 데이터를 읽어옴
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1 # 도시의 수
    M = int(input_data[ptr]); ptr += 1 # 도로의 수
    
    # 각 도시의 리터당 기름 가격
    prices = []
    for _ in range(N):
        prices.append(int(input_data[ptr]))
        ptr += 1
        
    # 인접 리스트 형식으로 도로 정보 저장
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(input_data[ptr]); ptr += 1
        v = int(input_data[ptr]); ptr += 1
        d = int(input_data[ptr]); ptr += 1
        adj[u].append((v, d))
        adj[v].append((u, d))
        
    # min_p_at[city]: 해당 도시에 도달했을 때의 최소 기름 가격 기록 (가지치기용)
    inf = float('inf')
    min_p_at = [inf] * (N + 1)
    
    # 다익스트라 우선순위 큐: (현재까지의 총 비용, 현재 도시, 현재까지의 최소 기름 가격)
    # 1번 도시에서 비용 0으로 시작, 초기 최소 가격은 1번 도시의 가격
    pq = [(0, 1, prices[0])]
    
    while pq:
        cost, u, p = heapq.heappop(pq)
        
        # 현재 도달한 기름 가격이 이전에 이 도시에 도달했을 때보다 비싸면 무시
        if p >= min_p_at[u]:
            continue
        min_p_at[u] = p
        
        # 목표 도시 N에 도달하면 비용 출력 후 종료
        if u == N:
            print(cost)
            return
        
        for v, d in adj[u]:
            # 다음 도시로 이동하는 비용 계산
            new_cost = cost + d * p
            # 다음 도시의 가격을 고려하여 최소 가격 갱신
            new_p = min(p, prices[v-1])
            
            # 다음 도시에 대해 더 저렴한 가격으로 도달 가능성이 있을 때만 큐에 삽입
            if new_p < min_p_at[v]:
                heapq.heappush(pq, (new_cost, v, new_p))

if __name__ == "__main__":
    solve()

#################################################################################

