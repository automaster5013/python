import sys

# 재귀 깊이 제한 해제 (500x500 격자 탐색 대비)
sys.setrecursionlimit(10**6)

def solve():
    # 빠른 입력 처리
    input = sys.stdin.read().split()
    if not input:
        return
    
    M = int(input[0])  # 세로 크기
    N = int(input[1])  # 가로 크기
    
    # 격자 높이 정보 저장
    grid = []
    idx = 2
    for _ in range(M):
        grid.append(list(map(int, input[idx : idx + N])))
        idx += N
        
    # DP 테이블 초기화 (-1: 미방문 상태)
    dp = [[-1] * N for _ in range(M)]
    
    # 이동 방향 (상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def dfs(r, c):
        # 목적지에 도달한 경우 경로 1개 반환
        if r == M - 1 and c == N - 1:
            return 1
        
        # 이미 계산된 결과가 있다면 해당 값 반환 (메모이제이션)
        if dp[r][c] != -1:
            return dp[r][c]
        
        # 현재 위치에서 경로 찾기 시작 (0으로 초기화)
        dp[r][c] = 0
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            # 격자 범위 내에 있고, 내리막길인 경우에만 이동
            if 0 <= nr < M and 0 <= nc < N:
                if grid[nr][nc] < grid[r][c]:
                    dp[r][c] += dfs(nr, nc)
                    
        return dp[r][c]

    # 시작점 (0, 0)에서 목적지까지의 경로 수 출력
    print(dfs(0, 0))

if __name__ == "__main__":
    solve()

####################################################################

