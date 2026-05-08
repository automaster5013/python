import sys
import heapq

def solve():
    # 빠른 입출력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    P = int(input_data[0])
    
    # 알파벳을 0~51 사이의 정수 인덱스로 변환하는 함수
    def char_to_idx(c):
        if 'A' <= c <= 'Z':
            return ord(c) - ord('A')
        else:
            return ord(c) - ord('a') + 26
            
    # 정수 인덱스를 다시 알파벳으로 변환하는 함수
    def idx_to_char(idx):
        if idx <= 25:
            return chr(idx + ord('A'))
        else:
            return chr(idx - 26 + ord('a'))

    # 그래프 인접 리스트 초기화 (총 52개 노드)
    graph = [{} for _ in range(52)]
    
    idx = 1
    for _ in range(P):
        u_char = input_data[idx]
        v_char = input_data[idx+1]
        w = int(input_data[idx+2])
        idx += 3
        
        u = char_to_idx(u_char)
        v = char_to_idx(v_char)
        
        # 중복된 경로가 들어올 경우 가장 짧은 거리만 유지
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], w)
        else:
            graph[u][v] = w
            graph[v][u] = w
            
    # 헛간 'Z'에서 시작하는 다익스트라 알고리즘 설정
    start = char_to_idx('Z')
    dist = [float('inf')] * 52
    dist[start] = 0
    
    # 우선순위 큐 초기화: (거리, 노드)
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # 이미 처리된 노드라면 무시
        if d > dist[u]:
            continue
            
        # 인접한 목장 탐색
        for v, weight in graph[u].items():
            cost = dist[u] + weight
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(pq, (cost, v))
                
    # 'A'부터 'Y'까지 (인덱스 0 ~ 24) 중 가장 거리가 짧은 소 찾기
    min_dist = float('inf')
    best_cow = -1
    
    for i in range(25):
        if dist[i] < min_dist:
            min_dist = dist[i]
            best_cow = i
            
    # 정답 출력
    print(f"{idx_to_char(best_cow)} {min_dist}")

if __name__ == '__main__':
    solve()

#####################################################################


