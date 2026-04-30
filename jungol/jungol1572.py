import sys

# 이 문제는 격자 그리드를 생성하여 영역을 탐색하는 방식으로 해결합니다.
# N이 1,000이므로 최대 1,000x1,000 격자가 생성되어 시간 내에 처리가 가능합니다.

def solve():
    # 고속 입력을 통해 데이터를 읽어옵니다.
    try:
        input_data = sys.stdin.read().split()
    except EOFError:
        return
    if not input_data:
        return
    
    n = int(input_data[0])
    vertices = []
    idx = 1
    for _ in range(n):
        if idx + 1 >= len(input_data): break
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        vertices.append((x, y))
        idx += 2
        
    # 1. 좌표 압축: 모든 x, y 좌표를 추출하여 정렬합니다.
    xs_raw = sorted(list(set(v[0] for v in vertices)))
    ys_raw = sorted(list(set(v[1] for v in vertices)))
    
    # 외부 영역 탐색을 쉽게 하기 위해 좌표 끝에 여백(-1, 10001)을 추가합니다.
    xs = [-1] + xs_raw + [10001]
    ys = [-1] + ys_raw + [10001]
    
    x_map = {val: i for i, val in enumerate(xs)}
    y_map = {val: i for i, val in enumerate(ys)}
    
    nx, ny = len(xs), len(ys)
    cols, rows = nx - 1, ny - 1
    
    # 격자 선분이 다각형의 변인지 체크하는 배열 (벽 표시)
    blocked_h = [[False] * ny for _ in range(nx)]
    blocked_v = [[False] * ny for _ in range(nx)]
    
    # 2. 다각형의 변을 격자 그리드에 벽으로 표시합니다.
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        
        if v1[0] == v2[0]: # 수직 선분
            ix = x_map[v1[0]]
            y_low, y_high = (v1[1], v2[1]) if v1[1] < v2[1] else (v2[1], v1[1])
            iy_start, iy_end = y_map[y_low], y_map[y_high]
            for j in range(iy_start, iy_end):
                blocked_v[ix][j] = True
        else: # 수평 선분
            iy = y_map[v1[1]]
            x_low, x_high = (v1[0], v2[0]) if v1[0] < v2[0] else (v2[0], v1[0])
            ix_start, ix_end = x_map[x_low], x_map[x_high]
            for i_idx in range(ix_start, ix_end):
                blocked_h[i_idx][iy] = True

    # 3. 플러드 필로 영역 탐색
    visited = [[False] * rows for _ in range(cols)]
    
    # 외부(무한 영역) 탐색: (0, 0)은 여백으로 인해 무조건 외부입니다.
    stack = [(0, 0)]
    visited[0][0] = True
    while stack:
        cx, cy = stack.pop()
        # 위쪽 셀 탐색 (수평 벽 확인)
        if cy + 1 < rows and not visited[cx][cy+1] and not blocked_h[cx][cy+1]:
            visited[cx][cy+1] = True
            stack.append((cx, cy+1))
        # 아래쪽 셀 탐색
        if cy - 1 >= 0 and not visited[cx][cy-1] and not blocked_h[cx][cy]:
            visited[cx][cy-1] = True
            stack.append((cx, cy-1))
        # 오른쪽 셀 탐색 (수직 벽 확인)
        if cx + 1 < cols and not visited[cx+1][cy] and not blocked_v[cx+1][cy]:
            visited[cx+1][cy] = True
            stack.append((cx+1, cy))
        # 왼쪽 셀 탐색
        if cx - 1 >= 0 and not visited[cx-1][cy] and not blocked_v[cx][cy]:
            visited[cx-1][cy] = True
            stack.append((cx-1, cy))
            
    # 내부 분할 영역 중 최대 면적 찾기
    max_area = 0
    for i in range(cols):
        for j in range(rows):
            if not visited[i][j]:
                curr_area = 0
                comp_stack = [(i, j)]
                visited[i][j] = True
                while comp_stack:
                    cx, cy = comp_stack.pop()
                    # 해당 셀의 면적 = (x 차이) * (y 차이)
                    curr_area += (xs[cx+1] - xs[cx]) * (ys[cy+1] - ys[cy])
                    
                    if cy + 1 < rows and not visited[cx][cy+1] and not blocked_h[cx][cy+1]:
                        visited[cx][cy+1] = True
                        comp_stack.append((cx, cy+1))
                    if cy - 1 >= 0 and not visited[cx][cy-1] and not blocked_h[cx][cy]:
                        visited[cx][cy-1] = True
                        comp_stack.append((cx, cy-1))
                    if cx + 1 < cols and not visited[cx+1][cy] and not blocked_v[cx+1][cy]:
                        visited[cx+1][cy] = True
                        comp_stack.append((cx+1, cy))
                    if cx - 1 >= 0 and not visited[cx-1][cy] and not blocked_v[cx][cy]:
                        visited[cx-1][cy] = True
                        comp_stack.append((cx-1, cy))
                
                max_area = max(max_area, curr_area)
                
    sys.stdout.write(str(max_area) + "\n")

if __name__ == "__main__":
    solve()

###################################################################################################
