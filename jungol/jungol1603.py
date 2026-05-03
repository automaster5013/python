import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 비행장 수
    k = int(input_data[1]) # 최대 급유 횟수
    
    # 지점들: S(0,0), 비행장들, T(10000, 10000)
    points = [(0, 0)]
    for i in range(n):
        x = int(input_data[2 + 2*i])
        y = int(input_data[3 + 2*i])
        points.append((x, y))
    points.append((10000, 10000))
    
    total_nodes = len(points)
    
    # 2. BFS 검증 함수
    def can_reach(capacity):
        max_dist_sq = (capacity * 10) ** 2
        queue = deque([(0, 0)]) # (현재 노드 인덱스, 현재까지의 점프 횟수)
        visited = [False] * total_nodes
        visited[0] = True
        
        while queue:
            curr, jumps = queue.popleft()
            
            # 급유 횟수 = 점프 횟수 - 1
            # 만약 점프 횟수가 k + 1을 넘어가면 더 이상 탐색할 필요 없음
            if jumps > k:
                continue
            
            for nxt in range(1, total_nodes):
                if not visited[nxt]:
                    # 두 지점 사이의 거리가 용량 이내인지 확인 (제곱 비교로 속도 향상)
                    dx = points[curr][0] - points[nxt][0]
                    dy = points[curr][1] - points[nxt][1]
                    dist_sq = dx*dx + dy*dy
                    
                    if dist_sq <= max_dist_sq:
                        if nxt == total_nodes - 1: # 목적지 도착
                            return True
                        visited[nxt] = True
                        queue.append((nxt, jumps + 1))
        return False

    # 3. 이분 탐색
    low = 1
    high = 1415 # 루트(10000^2 + 10000^2) / 10 의 올림값
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if can_reach(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == "__main__":
    solve()

#########################################################################################

