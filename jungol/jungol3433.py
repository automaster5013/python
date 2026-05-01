import sys

# 효율적인 처리를 위해 재귀 대신 반복문 사용
def process_comp(L, R, A, W_float):
    n = R - L + 1
    if n <= 0: return
    
    pref = [0] * n
    suff = [0] * n
    
    curr = A[L]
    for i in range(n):
        if A[L+i] < curr: curr = A[L+i]
        pref[i] = curr
        
    curr = A[R]
    for i in range(n-1, -1, -1):
        if A[L+i] < curr: curr = A[L+i]
        suff[i] = curr
        
    for i in range(n):
        W_float[L+i] = max(pref[i], suff[i])

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    A = [0] * (M + 1)
    B = [0] * (M + 1)
    h = [0] * (M + 1)
    
    idx = 2
    for j in range(1, M + 1):
        aj, bj = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        if aj == 0:
            A[j], B[j] = N + 1, N
        else:
            A[j], B[j] = aj, bj
            
        if B[j] == N: h[j] = A[j]
        else: h[j] = N + 1
            
    # 바닥 용기 수위 계산
    L_floor = [N + 1] * (M + 2)
    R_floor = [N + 1] * (M + 2)
    
    curr = N + 1
    for j in range(1, M + 1):
        if h[j] < curr: curr = h[j]
        L_floor[j] = curr
    curr = N + 1
    for j in range(M, 0, -1):
        if h[j] < curr: curr = h[j]
        R_floor[j] = curr
        
    W_floor = [max(L_floor[j], R_floor[j]) for j in range(M + 1)]
    
    # 공중에 뜬 용기 수위 계산
    W_float = [N + 1] * (M + 1)
    comp_start = -1
    for j in range(1, M + 1):
        is_float = (A[j] <= N and B[j] < N)
        if is_float:
            if comp_start == -1: comp_start = j
            elif not (max(A[j-1], A[j]) <= min(B[j-1], B[j])):
                process_comp(comp_start, j-1, A, W_float)
                comp_start = j
        else:
            if comp_start != -1:
                process_comp(comp_start, j-1, A, W_float)
                comp_start = -1
    if comp_start != -1: process_comp(comp_start, M, A, W_float)

    # 전체 고인 물 계산
    ans = 0
    for j in range(1, M + 1):
        # 덩어리 위쪽 고인 물
        trapped_top = min(W_floor[j], W_float[j])
        if trapped_top < A[j]:
            ans += (A[j] - trapped_top)
        # 덩어리 아래쪽 고인 물
        if B[j] < N:
            trapped_bottom_start = max(B[j] + 1, W_floor[j])
            if trapped_bottom_start <= N:
                ans += (N - trapped_bottom_start + 1)
                
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()

#######################################################################

