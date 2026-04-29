import sys

def solve():
    # 1. 고속 입력 및 초기화
    input_data = sys.stdin.read().split()
    if not input_data: return
    n = int(input_data[0])
    
    points = []
    y_coords = []
    ptr = 1
    for _ in range(n):
        x = int(input_data[ptr])
        y = int(input_data[ptr+1])
        w = int(input_data[ptr+2])
        points.append((x, y, w))
        y_coords.append(y)
        ptr += 3
        
    # 2. 좌표 압축
    y_coords = sorted(list(set(y_coords)))
    y_map = {y: i for i, y in enumerate(y_coords)}
    m = len(y_coords)
    points.sort() # X좌표 기준 정렬

    # 3. 세그먼트 트리 배열 (4개의 1차원 리스트로 분리 - 속도 핵심)
    size = 1
    while size < m: size *= 2
    
    t_max = [0] * (2 * size)
    t_pre = [0] * (2 * size)
    t_suf = [0] * (2 * size)
    t_sum = [0] * (2 * size)

    ans = 0
    
    # 4. 스위핑 루프
    for i in range(n):
        # 같은 X좌표에서 시작하는 중복 계산 방지
        if i > 0 and points[i][0] == points[i-1][0]:
            continue
            
        # 트리 초기화 (리스트 슬라이싱을 이용한 고속 초기화)
        t_max[:] = [0] * (2 * size)
        t_pre[:] = [0] * (2 * size)
        t_suf[:] = [0] * (2 * size)
        t_sum[:] = [0] * (2 * size)
        
        for j in range(i, n):
            # 5. 인라인 업데이트 (함수 호출 없이 직접 연산)
            idx = size + y_map[points[j][1]]
            w = points[j][2]
            
            t_sum[idx] += w
            v = t_sum[idx]
            t_max[idx] = t_pre[idx] = t_suf[idx] = max(0, v)
            
            p = idx // 2
            while p >= 1:
                l, r = p * 2, p * 2 + 1
                # 노드 병합 로직 (Maximum Subarray Sum)
                t_sum[p] = t_sum[l] + t_sum[r]
                t_pre[p] = max(t_pre[l], t_sum[l] + t_pre[r])
                t_suf[p] = max(t_suf[r], t_sum[r] + t_suf[l])
                # 최대값은 (왼쪽 최대, 오른쪽 최대, 왼쪽 접미사+오른쪽 접두사) 중 최대
                tm = t_suf[l] + t_pre[r]
                ml = t_max[l]
                mr = t_max[r]
                if ml > mr:
                    t_max[p] = ml if ml > tm else tm
                else:
                    t_max[p] = mr if mr > tm else tm
                p //= 2
            
            # X좌표가 같은 점들을 모두 처리한 후에만 정답 갱신
            if j == n - 1 or points[j][0] < points[j+1][0]:
                if t_max[1] > ans:
                    ans = t_max[1]
                    
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()

#########################################################################################
