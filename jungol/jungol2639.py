import sys

# 대규모 데이터 처리를 위해 재귀 한도를 높임
sys.setrecursionlimit(10**6)

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽음
    try:
        raw_input = sys.stdin.read().split()
    except EOFError:
        return
    if not raw_input:
        return
    
    N = int(raw_input[0])
    ptr = 1
    
    # 꼭짓점 정보 읽기
    v_x = [0] * N
    v_y = [0] * N
    for i in range(N):
        v_x[i] = int(raw_input[ptr])
        v_y[i] = int(raw_input[ptr+1])
        ptr += 2
        
    segs_y = []
    segs_w = []
    segs_x1 = []
    
    # 수평 선분 추출 (v[1]-v[2], v[3]-v[4], ...)
    for i in range(1, N - 1, 2):
        x1, y = v_x[i], v_y[i]
        x2 = v_x[i+1]
        segs_y.append(y)
        segs_w.append(x2 - x1)
        segs_x1.append(x1)
        
    M = len(segs_y)
    if M == 0:
        print("0.00")
        print("0")
        return

    K_holes = int(raw_input[ptr])
    ptr += 1
    
    hole_set = set()
    for _ in range(K_holes):
        hx1 = int(raw_input[ptr])
        hy1 = int(raw_input[ptr+1])
        ptr += 4
        hole_set.add((hx1, hy1))
        
    has_hole = [0] * M
    total_initial_area = 0
    for i in range(M):
        if (segs_x1[i], segs_y[i]) in hole_set:
            has_hole[i] = 1
        total_initial_area += segs_w[i] * segs_y[i]
        
    # RMQ를 위한 Sparse Table 빌드 (가장 얕은 y의 인덱스 찾기)
    log_table = [0] * (M + 1)
    for i in range(2, M + 1):
        log_table[i] = log_table[i >> 1] + 1
        
    st_depth = log_table[M] + 1
    st = [None] * st_depth
    st[0] = list(range(M))
    for k in range(1, st_depth):
        prev_st = st[k-1]
        curr_st = [0] * (M - (1 << k) + 1)
        offset = 1 << (k-1)
        for i in range(M - (1 << k) + 1):
            idx1 = prev_st[i]
            idx2 = prev_st[i + offset]
            # 더 작은 y를 우선, 같으면 앞쪽 인덱스 선택
            curr_st[i] = idx1 if segs_y[idx1] <= segs_y[idx2] else idx2
        st[k] = curr_st
                
    def query(l, r):
        d = r - l + 1
        k = log_table[d]
        idx1 = st[k][l]
        idx2 = st[k][r - (1 << k) + 1]
        return idx1 if segs_y[idx1] <= segs_y[idx2] else idx2
            
    total_drained = [0] # nonlocal 변수 대체용

    # 분지 트리 탐색 (Bottom-up)
    def process(l, r, upper_y):
        if l > r:
            return 0, 0, 0.0 # 너비, 구멍 수, 누적 시간
        
        # 현재 범위 내에서 가장 얕은(y가 작은) 선분이 이 분지의 "턱(lip)"이 됨
        k = query(l, r)
        curr_y = segs_y[k]
        
        # 좌우 하위 분지 탐색
        w_l, h_l, t_l = process(l, k - 1, curr_y)
        w_r, h_r, t_r = process(k + 1, r, curr_y)
        
        my_width = w_l + w_r + segs_w[k]
        my_holes = h_l + h_r + has_hole[k]
        
        my_time = 0.0
        if my_holes > 0:
            # 하위 분지 중 가장 오래 걸린 시간부터 시작하여 턱까지 배수
            branch_time = t_l if t_l > t_r else t_r
            # 시간 = 부피 / 구멍 수
            my_time = branch_time + (float(my_width) * (curr_y - upper_y)) / my_holes
            total_drained[0] += my_width * (curr_y - upper_y)
        
        return my_width, my_holes, my_time
        
    _, _, final_time = process(0, M - 1, 0)
    
    # 결과 출력
    sys.stdout.write("{:.2f}\n".format(final_time))
    sys.stdout.write("{}\n".format(int(total_initial_area - total_drained[0])))

if __name__ == "__main__":
    solve()

########################################################################################

