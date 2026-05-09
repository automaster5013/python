import sys

def solve():
    # 빠른 입출력 처리를 위해 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    idx = 1
    
    # 미로 벽 정보 1차원 리스트로 저장 (인덱스 접근 속도 최적화)
    grid = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    M = int(input_data[idx])
    idx += 1
    
    # LED 타일 정보 매핑
    leds = []
    indices_of_val = {}
    for i in range(M):
        r = int(input_data[idx]) - 1
        c = int(input_data[idx+1]) - 1
        val = int(input_data[idx+2])
        idx += 3
        
        u = r * N + c # 1차원 인덱스 변환
        leds.append((u, val))
        
        if val not in indices_of_val:
            indices_of_val[val] = []
        indices_of_val[val].append(i)
        
    T = int(input_data[idx])
    idx += 1
    
    # 찾아야 하는 수열 입력
    S = []
    for _ in range(T):
        S.append(int(input_data[idx]))
        idx += 1
        
    # 1. 빠른 탐색을 위해 1차원 배열 형태의 인접 리스트 생성
    adj = [[] for _ in range(N * N)]
    for r in range(N):
        for c in range(N):
            u = r * N + c
            w = grid[r][c]
            
            # 북쪽(1), 동쪽(2), 남쪽(4), 서쪽(8) 양방향 뚫림 확인
            if r > 0 and not (w & 1) and not (grid[r-1][c] & 4):
                adj[u].append(u - N)
            if c < N - 1 and not (w & 2) and not (grid[r][c+1] & 8):
                adj[u].append(u + 1)
            if r < N - 1 and not (w & 4) and not (grid[r+1][c] & 1):
                adj[u].append(u + N)
            if c > 0 and not (w & 8) and not (grid[r][c-1] & 2):
                adj[u].append(u - 1)
                
    # 2. 극한으로 속도를 높인 배열 기반 BFS (deque 오버헤드 제거)
    def bfs(start_u):
        dist = [-1] * (N * N)
        dist[start_u] = 0
        q = [0] * (N * N) # 고정 크기 배열로 큐 구현
        q[0] = start_u
        head = 0
        tail = 1
        
        while head < tail:
            u = q[head]
            head += 1
            d = dist[u] + 1
            
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = d
                    q[tail] = v
                    tail += 1
        return dist

    # 3. 모든 주요 거점 간 최단 거리 (All-Pairs Shortest Path) 계산
    dist_start_array = bfs(0)  # 시작점 (0,0)에서 출발
    dist_start = [dist_start_array[u] for u, _ in leds]
    
    dist_matrix = [[-1] * M for _ in range(M)]
    dist_exit = [-1] * M
    end_u = (N - 1) * N + (N - 1)  # 출구 위치
    
    # 각 LED 간의 거리 및 LED에서 출구까지의 거리
    for i in range(M):
        u, _ = leds[i]
        dist_from_led = bfs(u)
        for j in range(M):
            v, _ = leds[j]
            dist_matrix[i][j] = dist_from_led[v]
        dist_exit[i] = dist_from_led[end_u]
        
    # 4. 메모리를 줄인 1차원 동적 계획법 (Dynamic Programming)
    INF = float('inf')
    prev_dp = [INF] * M
    
    # 초기 시작 타겟 갱신 (입구로 진입하는 시간 1 추가)
    target_val = S[0]
    if target_val in indices_of_val:
        for i in indices_of_val[target_val]:
            if dist_start[i] != -1:
                prev_dp[i] = 1 + dist_start[i]
                
    # 수열 순서대로 탐색하며 최단 시간 누적
    for t in range(1, T):
        curr_dp = [INF] * M
        prev_val = S[t-1]
        curr_val = S[t]
        
        if curr_val not in indices_of_val or prev_val not in indices_of_val:
            prev_dp = curr_dp
            continue
            
        for i in indices_of_val[curr_val]:
            best = INF
            for j in indices_of_val[prev_val]:
                if prev_dp[j] != INF and dist_matrix[j][i] != -1:
                    if prev_dp[j] + dist_matrix[j][i] < best:
                        best = prev_dp[j] + dist_matrix[j][i]
            curr_dp[i] = best
        prev_dp = curr_dp
        
    # 5. 최종 위치에서 출구로 빠져나가는 최소 시간 도출 (출구 탈출 시간 1 추가)
    ans = INF
    final_val = S[-1]
    
    if final_val in indices_of_val:
        for i in indices_of_val[final_val]:
            if prev_dp[i] != INF and dist_exit[i] != -1:
                if prev_dp[i] + dist_exit[i] + 1 < ans:
                    ans = prev_dp[i] + dist_exit[i] + 1
                    
    print(ans)

if __name__ == '__main__':
    solve()

################################################################################



