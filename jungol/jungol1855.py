import sys
import heapq

def solve():
    # 모든 입력을 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))  # 학생 수
    p = int(next(it))  # 장소 수
    c = int(next(it))  # 경로 수
    
    adj = [[] for _ in range(p + 1)]
    for _ in range(c):
        u, v, cost = int(next(it)), int(next(it)), int(next(it))
        adj[u].append((v, cost))
        adj[v].append((u, cost))
        
    student_pos = [int(next(it)) for _ in range(n)]
    
    # 각 장소에서 다른 장소까지의 최단 거리를 미리 계산하지 않고,
    # 각 장소를 '모임 장소'로 가정하고 다익스트라를 수행합니다.
    def get_total_dist(start_node):
        distances = [float('inf')] * (p + 1)
        distances[start_node] = 0
        pq = [(0, start_node)]
        
        while pq:
            d, curr = heapq.heappop(pq)
            
            if distances[curr] < d:
                continue
                
            for neighbor, weight in adj[curr]:
                if d + weight < distances[neighbor]:
                    distances[neighbor] = d + weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))
        
        # 해당 모임 장소에서 모든 학생의 위치까지 거리 합산
        res = 0
        for pos in student_pos:
            res += distances[pos]
        return res

    min_total_sum = float('inf')
    
    # 모든 장소를 후보지로 검사
    for i in range(1, p + 1):
        current_sum = get_total_dist(i)
        if current_sum < min_total_sum:
            min_total_sum = current_sum
            
    print(min_total_sum)

if __name__ == "__main__":
    solve()

###########################################################################



