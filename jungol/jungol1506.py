import sys

def solve():
    # 입력을 공백 단위로 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 광선의 세기 K와 철판의 개수 N
    K = int(input_data[0])
    N = int(input_data[1])
    
    plates = []
    pointer = 2
    for _ in range(N):
        # n(ID), xn, ymin, ymax
        p_id = int(input_data[pointer])
        x_coord = int(input_data[pointer + 1])
        y_min = int(input_data[pointer + 2])
        y_max = int(input_data[pointer + 3])
        
        # y1을 최소값, y2를 최대값으로 정규화하여 저장
        plates.append({
            'id': p_id,
            'x': x_coord,
            'y1': min(y_min, y_max),
            'y2': max(y_min, y_max)
        })
        pointer += 4
        
    # 모든 y 좌표 경계값을 수집하여 정렬 (중복 제거)
    y_boundaries = set()
    for p in plates:
        y_boundaries.add(p['y1'])
        y_boundaries.add(p['y2'])
    sorted_ys = sorted(list(y_boundaries))
    
    safe_ids = []
    
    # 각 철판별로 안전 여부 검사
    for p in plates:
        is_safe = True
        
        # 철판이 차지하는 y 범위를 기초 구간 단위로 쪼개어 검사
        for i in range(len(sorted_ys) - 1):
            y_start = sorted_ys[i]
            y_end = sorted_ys[i + 1]
            # 구간의 중간 지점을 사용하여 해당 구간을 지나는 광선 시뮬레이션
            y_mid = (y_start + y_end) / 2.0
            
            # 현재 철판이 이 y 구간을 덮고 있는지 확인
            if p['y1'] <= y_mid <= p['y2']:
                # 현재 철판보다 왼쪽에 있으면서 동일한 y 구간을 가로막는 철판 개수 계산
                blocking_count = 0
                for other in plates:
                    if other['x'] < p['x']:
                        if other['y1'] <= y_mid <= other['y2']:
                            blocking_count += 1
                
                # 가로막는 철판이 K개 미만이면 광선이 도달하여 철판이 녹음
                if blocking_count < K:
                    is_safe = False
                    break
        
        if is_safe:
            safe_ids.append(p['id'])
            
    # 출력 처리
    if not safe_ids:
        print("0")
    else:
        # 안전한 철판 번호를 오름차순으로 정렬하여 출력
        safe_ids.sort()
        print(*(safe_ids))

if __name__ == '__main__':
    solve()

#####################################################################################

