import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 물고기 종류 수
    k_limit = int(input_data[1]) # 최소 겹침 수
    
    boxes = []
    xs, ys, ds = [], [], []
    
    ptr = 2
    for _ in range(n):
        # x1, y1, d1, x2, y2, d2
        b = [int(x) for x in input_data[ptr:ptr+6]]
        boxes.append(b)
        xs.extend([b[0], b[3]])
        ys.extend([b[1], b[4]])
        ds.extend([b[2], b[5]])
        ptr += 6
        
    # 2. 좌표 압축 (정렬 및 중복 제거)
    ux = sorted(list(set(xs)))
    uy = sorted(list(set(ys)))
    ud = sorted(list(set(ds)))
    
    xi = {x: i for i, x in enumerate(ux)}
    yi = {y: i for i, y in enumerate(uy)}
    
    nx, ny, nd = len(ux), len(uy), len(ud)
    total_volume = 0
    
    # 3. 깊이 구간별로 스위핑
    for k in range(nd - 1):
        d_low, d_high = ud[k], ud[k+1]
        depth_h = d_high - d_low
        
        # 해당 깊이 구간에 서식하는 물고기 선별 및 2차원 차분 배열 초기화
        diff = [[0] * ny for _ in range(nx)]
        active_count = 0
        
        for b in boxes:
            if b[2] <= d_low and d_high <= b[5]:
                # x1, y1, x2, y2 인덱스 추출
                ix1, iy1, ix2, iy2 = xi[b[0]], yi[b[1]], xi[b[3]], yi[b[4]]
                # 2차원 차분 배열 업데이트
                diff[ix1][iy1] += 1
                diff[ix2][iy1] -= 1
                diff[ix1][iy2] -= 1
                diff[ix2][iy2] += 1
                active_count += 1
        
        if active_count < k_limit:
            continue
            
        # 4. 2차원 누적합(Prefix Sum) 계산 및 면적 산출
        area = 0
        # Y축 방향 누적합
        for i in range(nx):
            for j in range(1, ny):
                diff[i][j] += diff[i][j-1]
        
        # X축 방향 누적합 및 면적 계산
        for i in range(nx - 1):
            dx = ux[i+1] - ux[i]
            for j in range(ny - 1):
                if i > 0:
                    diff[i][j] += diff[i-1][j]
                
                # K종 이상 겹치는 경우 면적에 포함
                if diff[i][j] >= k_limit:
                    area += dx * (uy[j+1] - uy[j])
        
        total_volume += area * depth_h
        
    # 5. 결과 출력
    print(total_volume)

if __name__ == "__main__":
    solve()

######################################################################


