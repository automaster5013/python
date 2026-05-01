import sys

# 대용량 처리를 위해 재귀 제한 및 입력 방식 최적화
sys.setrecursionlimit(2000000)

def solve():
    # 표준 입력을 통해 모든 데이터를 한 번에 읽음
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        it = iter(input_data)
        N = int(next(it))
    except (EOFError, StopIteration):
        return

    X = [0] * N
    Y = [0] * N
    
    start_idx = -1
    for i in range(N):
        x_val = int(next(it))
        y_val = int(next(it))
        X[i] = x_val
        Y[i] = y_val
        # x축 아래에 있는 꼭짓점을 시작점으로 선택 (봉우리 도중 끊김 방지)
        if start_idx == -1 and y_val < 0:
            start_idx = i

    intervals = []
    in_peak = False
    peak_start_x = 0
    
    # 다각형의 모든 변을 순회하며 x축 교차점(봉우리 경계) 확인
    for k in range(N):
        prev_idx = (start_idx + k) % N
        curr_idx = (start_idx + k + 1) % N
        
        y_prev = Y[prev_idx]
        y_curr = Y[curr_idx]
        
        # x축 아래에서 위로 진입: 봉우리 시작
        if y_prev < 0 and y_curr > 0:
            in_peak = True
            peak_start_x = X[curr_idx]
        # x축 위에서 아래로 탈출: 봉우리 종료
        elif in_peak and y_prev > 0 and y_curr < 0:
            in_peak = False
            l, r = peak_start_x, X[curr_idx]
            if l > r: l, r = r, l
            intervals.append((l, r))

    if not intervals:
        return

    # 구간 정렬: 시작점(L)은 오름차순, 끝점(R)은 내림차순
    intervals.sort(key=lambda x: (x[0], -x[1]))

    # 다른 봉우리에 포함되지 않는 봉우리(Root) 개수 계산
    roots_count = 0
    max_reach = -2000000001 # 좌표 범위 밖의 최소값으로 초기화
    for l, r in intervals:
        if l > max_reach:
            roots_count += 1
            max_reach = r
    
    # 다른 봉우리를 포함하지 않는 봉우리(Leaf) 개수 계산
    leaves_count = 0
    num_intervals = len(intervals)
    for i in range(num_intervals):
        # 정렬 특성상, i번 봉우리가 어떤 봉우리를 포함한다면 반드시 바로 다음(i+1) 봉우리를 포함함
        if i + 1 < num_intervals and intervals[i+1][1] < intervals[i][1]:
            continue
        leaves_count += 1
        
    # 결과 출력: 최상위 봉우리 개수와 최하위 봉우리 개수
    sys.stdout.write(f"{roots_count} {leaves_count}\n")

if __name__ == "__main__":
    solve()

##################################################################################################

