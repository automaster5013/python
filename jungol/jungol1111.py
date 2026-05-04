import heapq
import sys

def solve():
    # 데이터 읽기 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 정상 좌표 (1-based -> 0-based 변환)
    target_r, target_c = int(input_data[1]) - 1, int(input_data[2]) - 1
    
    # 지형 높이 행렬 구성
    mountain = []
    idx = 3
    for i in range(n):
        mountain.append(list(map(int, input_data[idx : idx + n])))
        idx += n
        
    # 최단 거리(힘) 배열 초기화
    dist = [[float('inf')] * n for _ in range(n)]
    pq = [] # (비용, 행, 열)
    
    # 1. 시작점 처리: 모든 테두리 노드를 시작 후보로 등록
    # 바깥(높이 0)에서 테두리로 들어오는 비용은 (높이)^2
    for r in range(n):
        for c in range(n):
            if r == 0 or r == n - 1 or c == 0 or c == n - 1:
                cost = mountain[r][c] ** 2
                dist[r][c] = cost
                heapq.heappush(pq, (cost, r, c))
                
    # 2. 다익스트라 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while pq:
        curr_d, r, c = heapq.heappop(pq)
        
        # 이미 처리된 경로는 무시
        if curr_d > dist[r][c]:
            continue
            
        # 정상에 도달한 경우 (다익스트라 특성상 가장 먼저 도착한 것이 최단 거리)
        if r == target_r and c == target_c:
            print(curr_d)
            return
            
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n:
                h1 = mountain[r][c]
                h2 = mountain[nr][nc]
                
                # 비용 계산 규칙 적용
                if h1 == h2:
                    move_cost = 0
                elif h1 > h2:
                    move_cost = h1 - h2
                else: # h1 < h2
                    move_cost = (h2 - h1) ** 2
                
                if dist[r][c] + move_cost < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + move_cost
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))

if __name__ == "__main__":
    solve()

##################################################################################3



