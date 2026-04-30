import sys

# 세그먼트 트리 탐색을 위한 재귀 깊이 제한 확장
sys.setrecursionlimit(1000000)

def solve():
    # 표준 입력으로부터 데이터를 읽어옵니다.
    try:
        input_data = sys.stdin.read().split()
    except EOFError:
        return
        
    if not input_data:
        return
    
    # 장애물 개수 N, 출발지점 y, 결승선 x 좌표
    N = int(input_data[0])
    Y_start = int(input_data[1])
    X_finish = int(input_data[2])
    
    obstacles = []
    for i in range(N):
        x = int(input_data[3 + 3*i])
        yl = int(input_data[4 + 3*i])
        yh = int(input_data[5 + 3*i])
        obstacles.append((x, yl, yh))
        
    # 장애물을 x 좌표 순으로 정렬하여 동쪽으로 이동하며 처리합니다.
    obstacles.sort()
    
    # 좌표 압축: 유의미한 모든 y 좌표를 수집하여 정렬합니다.
    all_y = {Y_start}
    for _, yl, yh in obstacles:
        all_y.add(yl)
        all_y.add(yh)
        
    coords = sorted(list(all_y))
    M = len(coords)
    idx_map = {y: i for i, y in enumerate(coords)}
    
    # 세그먼트 트리 크기 설정 (2의 거듭제곱)
    size = 1 << (M - 1).bit_length()
    tree_count = [0] * (2 * size) # 활성화된 경로의 개수를 저장하는 트리
    
    INF = float('inf')
    f_values = [INF] * M # 각 y 좌표에서의 최소 수직 이동 거리
    
    # 세그먼트 트리의 특정 점을 활성화하거나 거리 값을 갱신하는 함수
    def update_st(i, dist):
        if dist < f_values[i]:
            f_values[i] = dist
            idx = i + size
            if tree_count[idx] == 0:
                tree_count[idx] = 1
                while idx > 1:
                    idx >>= 1
                    tree_count[idx] = tree_count[idx << 1] + tree_count[(idx << 1) | 1]

    # 세그먼트 트리의 특정 점을 비활성화하는 함수 (장애물에 막힌 경로 제거)
    def clear_st(i):
        f_values[i] = INF
        idx = i + size
        if tree_count[idx] == 1:
            tree_count[idx] = 0
            while idx > 1:
                idx >>= 1
                tree_count[idx] = tree_count[idx << 1] + tree_count[(idx << 1) | 1]

    # 장애물 범위 내에 있는 활성화된 모든 인덱스를 찾는 함수
    def get_active(v, tl, tr, l, r, found):
        if l > r or tree_count[v] == 0:
            return
        if tl == tr:
            found.append(tl)
            return
        tm = (tl + tr) >> 1
        if l <= tm:
            get_active(v << 1, tl, tm, l, min(r, tm), found)
        if r > tm:
            get_active((v << 1) | 1, tm + 1, tr, max(l, tm + 1), r, found)

    # 초기 상태 설정: 출발지점 y좌표에서의 수직 거리는 0입니다.
    update_st(idx_map[Y_start], 0)
    
    for _, yl, yh in obstacles:
        idx_l = idx_map[yl]
        idx_h = idx_map[yh]
        
        # 현재 장애물 구간 (yl, yh)에 걸리는 모든 경로를 찾습니다.
        found = []
        get_active(1, 0, size - 1, idx_l + 1, idx_h - 1, found)
        
        if not found:
            continue
        
        # 장애물 끝 점(yl 또는 yh)으로 우회하는 최적의 경로를 계산합니다.
        min_plus = INF  # f(y) + y 의 최솟값
        min_minus = INF # f(y) - y 의 최솟값
        for i in found:
            val_f = f_values[i]
            y_val = coords[i]
            if val_f + y_val < min_plus:
                min_plus = val_f + y_val
            if val_f - y_val < min_minus:
                min_minus = val_f - y_val
            # 장애물에 막힌 기존의 점은 제거합니다.
            clear_st(i)
            
        # 장애물 양 끝점으로 우회한 경로들을 업데이트합니다.
        update_st(idx_l, min_plus - yl)
        update_st(idx_h, yh + min_minus)
        
    # 모든 장애물을 통과한 후, 수직 이동 거리의 최솟값을 찾습니다.
    min_v_dist = min(f_values)
    
    # 최단 경로의 전체 길이 출력
    sys.stdout.write(f"{X_finish + min_v_dist}\n")
    
    # 최소 수직 거리를 갖는 서로 다른 도착 지점들의 y 좌표 수집
    res_y = [coords[i] for i in range(M) if f_values[i] == min_v_dist]
    sys.stdout.write(f"{len(res_y)} {' '.join(map(str, res_y))}\n")

if __name__ == "__main__":
    solve()

#############################################################################


