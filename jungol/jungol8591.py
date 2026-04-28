import sys
import numpy as np

def solve():
    data = sys.stdin.buffer.read().split()
    N, M = int(data[0]), int(data[1])
    
    grid = np.array(data[2:], dtype=np.int64).reshape(N, M)
    row_prefix = np.cumsum(grid, axis=0)  # (N, M)
    
    ans = -10**18

    for r1 in range(N):
        # col[r2][j] = r1~r2행, j열 합 → 한 번에 (N-r1, M) 행렬로 처리
        if r1 == 0:
            cols = row_prefix  # (N, M)
        else:
            cols = row_prefix[r1:] - row_prefix[r1 - 1]  # (N-r1, M)
        
        # cols의 각 행에 대해 Kadane 적용
        # 열 방향 prefix sum 후 min prefix를 빼는 방법
        # prefix[j] - min(prefix[0..j-1]) 의 최대 = 최대 구간합
        col_prefix = np.cumsum(cols, axis=1)  # (rows, M)
        
        # 각 행에서 "현재까지의 최소 prefix" 계산
        # min_prefix[j] = min(0, prefix[0], ..., prefix[j-1])
        # 0을 앞에 붙여서 처리
        shifted = np.hstack([np.zeros((col_prefix.shape[0], 1), dtype=np.int64), col_prefix[:, :-1]])
        running_min = np.minimum.accumulate(shifted, axis=1)
        running_min = np.minimum(running_min, 0)  # 빈 구간(prefix 0) 포함
        
        row_max = (col_prefix - running_min).max(axis=1)  # 각 r2에 대한 최대 구간합
        ans = max(ans, row_max.max())
    
    print(ans)

solve()

###########################################################################################################