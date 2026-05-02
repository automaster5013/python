import sys

def solve():
    # 입력 처리
    input = sys.stdin.read().split()
    if not input:
        return
    
    N = int(input[0])
    grid = []
    idx = 1
    for _ in range(N):
        grid.append(list(map(int, input[idx:idx+N])))
        idx += N
        
    # 총 수확량 계산
    total_sum = sum(sum(row) for row in grid)
    
    # V[col][h]: col번째 열의 아래쪽 h개 칸의 수확량 합
    # col: 0 ~ N-1, h: 0 ~ N
    V = [[0] * (N + 1) for _ in range(N)]
    for j in range(N):
        current_col_sum = 0
        for h in range(1, N + 1):
            current_col_sum += grid[N - h][j]
            V[j][h] = current_col_sum
            
    # dp[col][h]: col번째 열까지의 높이가 h일 때 가능한 수확량 비트셋
    dp = [[0] * (N + 1) for _ in range(N)]
    
    # 첫 번째 열 초기화
    for h in range(N + 1):
        dp[0][h] = (1 << V[0][h])
        
    # DP 진행: 이전 열의 높이보다 현재 열의 높이가 크거나 같아야 함 (단조 증가)
    for j in range(1, N):
        for h in range(N + 1):
            for prev_h in range(h + 1):
                dp[j][h] |= (dp[j - 1][prev_h] << V[j][h])
                
    # 최적의 차이 계산
    min_diff = float('inf')
    best_b = -1
    last_h = -1
    
    for h in range(N + 1):
        for b in range(total_sum + 1):
            if (dp[N-1][h] >> b) & 1:
                diff = abs(2 * b - total_sum)
                if diff < min_diff:
                    min_diff = diff
                    best_b = b
                    last_h = h
                    
    # 경로 역추적
    ans_heights = [0] * N
    current_b = best_b
    current_h = last_h
    
    for j in range(N - 1, 0, -1):
        ans_heights[j] = current_h
        for prev_h in range(current_h + 1):
            prev_b = current_b - V[j][current_h]
            if prev_b >= 0 and (dp[j - 1][prev_h] >> prev_b) & 1:
                current_b = prev_b
                current_h = prev_h
                break
    ans_heights[0] = current_h
    
    # 결과 출력
    print(min_diff)
    print(*(ans_heights))

if __name__ == "__main__":
    solve()

#####################################################################



