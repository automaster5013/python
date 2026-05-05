import sys

# 재귀 한도 설정
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0]) # 행
    N = int(input_data[1]) # 열
    grid = input_data[2:]
    
    # 1. 좌석 좌표를 기반으로 노드 번호 부여
    total_seats = 0
    seat_id = [[-1] * N for _ in range(M)]
    for r in range(M):
        for c in range(N):
            if grid[r][c] == '.':
                seat_id[r][c] = total_seats
                total_seats += 1
                
    # 2. 이분 그래프 인접 리스트 생성 (짝수 열 -> 홀수 열로만 간선 연결)
    adj = [[] for _ in range(total_seats)]
    
    # 시험지를 볼 수 있는 상대 경로 (A, C, D, E 방향)
    # A(-1, -1), C(-1, 1), D(0, -1), E(0, 1)
    # 무향 그래프 관계이므로 반대 방향인 (1, -1), (1, 1)도 고려되어야 함
    directions = [(-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1)]
    
    for r in range(M):
        for c in range(0, N, 2): # 짝수 열(0, 2, 4...) 기준
            u = seat_id[r][c]
            if u == -1: continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < M and 0 <= nc < N:
                    v = seat_id[nr][nc]
                    if v != -1:
                        adj[u].append(v)
                        
    # 3. 이분 매칭 수행 (Maximum Matching)
    # match[v]는 홀수 열 노드 v에 매칭된 짝수 열 노드 번호
    match = [-1] * total_seats
    
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] == -1 or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False
    
    max_matching = 0
    for r in range(M):
        for c in range(0, N, 2): # 오직 짝수 열 노드에서만 시작
            u = seat_id[r][c]
            if u != -1:
                visited = [False] * total_seats
                if dfs(u, visited):
                    max_matching += 1
                    
    # 최대 독립 집합 = 전체 정점 - 최대 매칭
    print(total_seats - max_matching)

if __name__ == "__main__":
    solve()

#####################################################################

