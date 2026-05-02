import sys
from bisect import bisect_right
import array

def solve():
    # 전체 데이터를 읽어와 이터레이터로 변환 (I/O 최적화)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    tokens = iter(input_data)
    
    N = int(next(tokens))
    X = array.array('q', [0] * N)
    P_init = array.array('q', [0] * N)
    for i in range(N):
        X[i] = int(next(tokens))
        P_init[i] = int(next(tokens))
        
    # 각 점프대에서 제자리 점프를 할 수 있는 최대 횟수 (다음 점프대에 닿기 전까지)
    c_limit = array.array('i', [0] * N)
    for i in range(N - 1):
        diff = X[i+1] - X[i]
        if diff > P_init[i]:
            # p * 2^(c-1) < diff 를 만족하는 최대 c
            c_limit[i] = ((diff - 1) // P_init[i]).bit_length()
        else:
            c_limit[i] = 0

    Q = int(next(tokens))
    
    LOG = 20
    # array.array('q')는 요소당 8바이트를 사용하여 메모리를 절약합니다.
    nxt = [array.array('i', [-1] * N) for _ in range(LOG)]
    cost = [array.array('q', [0] * N) for _ in range(LOG)]
    INF = 2 * 10**18 
    
    # 희소 테이블 기저 조건 (2^0 단계)
    for i in range(N - 1):
        diff = X[i+1] - X[i]
        c = c_limit[i] # 다음 점프대를 넘어가기 위해 필요한 '실패 점프' 횟수
        
        p_escape = P_init[i] * (1 << c)
        landing_pos = X[i] + p_escape
        j = bisect_right(X, landing_pos) - 1
        
        # 소요 시간 = 제자리 점프 시간 + 통과 점프(1) + 왼쪽 이동 거리
        total_t = P_init[i] * ((1 << c) - 1) + c + 1 + (landing_pos - X[j])
        
        nxt[0][i] = j
        cost[0][i] = total_t
    
    # 희소 테이블 빌드 (Binary Lifting)
    for k in range(1, LOG):
        nk_prev = nxt[k-1]
        ck_prev = cost[k-1]
        nk_curr = nxt[k]
        ck_curr = cost[k]
        for i in range(N):
            mid = nk_prev[i]
            if mid != -1:
                nk_curr[i] = nk_prev[mid]
                cv = ck_prev[i] + ck_prev[mid]
                ck_curr[i] = cv if cv < INF else INF
            else:
                ck_curr[i] = INF

    results = []
    for _ in range(Q):
        S = int(next(tokens))
        T = int(next(tokens))
        
        idx = bisect_right(X, S) - 1
        if idx < 0:
            results.append(str(S - T))
            continue
            
        dt = S - X[idx]
        if T < dt:
            results.append(str(S - T))
            continue
            
        T -= dt
        curr_i = idx
        
        # 1. 희소 테이블을 타고 점프대 사이를 고속 이동
        for k in range(LOG - 1, -1, -1):
            nk = nxt[k]
            ck = cost[k]
            if nk[curr_i] != -1 and ck[curr_i] <= T:
                T -= ck[curr_i]
                curr_i = nk[curr_i]
        
        # 2. 현재 점프대에서 남은 시간 동안 뛸 수 있는 횟수 계산
        p = P_init[curr_i]
        # p * (2^c - 1) + c <= T 를 만족하는 최대 c 계산
        if T > 0:
            target_c = (T // p + 1).bit_length() - 1
            if p * ((1 << target_c) - 1) + target_c > T:
                target_c -= 1
            
            # 다음 점프대에 닿지 않는 선에서만 뜀
            best_c = target_c
            if curr_i < N - 1 and best_c > c_limit[curr_i]:
                best_c = c_limit[curr_i]
                
            T -= p * ((1 << best_c) - 1) + best_c
            p <<= best_c
        
        # 3. 마지막 상태 결정
        if T == 0:
            results.append(str(X[curr_i]))
        else:
            # 마지막 점프 후 남은 시간만큼 왼쪽으로 이동
            results.append(str(X[curr_i] + p - (T - 1)))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

###################################################################

