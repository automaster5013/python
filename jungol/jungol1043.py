import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    d = int(input_data[0])
    n = int(input_data[1])
    
    poly = []
    idx = 2
    for _ in range(n):
        poly.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
        
    # 1. 수직 간선 및 변을 확장한 직사각형(Bounding Boxes) 구하기
    v_edges = []
    rects = []
    for i in range(n):
        p1 = poly[i]
        p2 = poly[(i+1) % n]
        
        if p1[0] == p2[0]:
            v_edges.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))
            
        xmin, xmax = min(p1[0], p2[0]), max(p1[0], p2[0])
        ymin, ymax = min(p1[1], p2[1]), max(p1[1], p2[1])
        rects.append((xmin - d, xmax + d, ymin - d, ymax + d))
        
    # 2. X, Y 좌표 압축
    xs_set = set()
    ys_set = set()
    for x, y in poly:
        xs_set.update([x-d, x, x+d])
        ys_set.update([y-d, y, y+d])
        
    xs = sorted(list(xs_set))
    ys = sorted(list(ys_set))
    
    # 3. 그리드 생성 및 색칠
    G = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            cx = (xs[i] + xs[i+1]) / 2.0
            cy = (ys[j] + ys[j+1]) / 2.0
            
            inside = False
            for rx1, rx2, ry1, ry2 in rects:
                if rx1 <= cx <= rx2 and ry1 <= cy <= ry2:
                    inside = True
                    break
                    
            if not inside:
                count = 0
                for vx, vy1, vy2 in v_edges:
                    if vx > cx and vy1 <= cy < vy2:
                        count += 1
                if count % 2 == 1:
                    inside = True
                    
            G[i][j] = inside

    def get_G(i, j):
        if 0 <= i < len(xs)-1 and 0 <= j < len(ys)-1:
            return G[i][j]
        return False

    # 4. 외곽선 방향 간선 그래프 생성 (반시계 방향)
    edges = defaultdict(list)
    
    for i in range(len(xs) - 1):
        for j in range(len(ys)):
            TR = get_G(i, j)
            BR = get_G(i, j-1)
            if TR and not BR: edges[(xs[i], ys[j])].append((xs[i+1], ys[j]))
            if not TR and BR: edges[(xs[i+1], ys[j])].append((xs[i], ys[j]))

    for i in range(len(xs)):
        for j in range(len(ys) - 1):
            TR = get_G(i, j)
            TL = get_G(i-1, j)
            if not TR and TL: edges[(xs[i], ys[j])].append((xs[i], ys[j+1]))
            if TR and not TL: edges[(xs[i], ys[j+1])].append((xs[i], ys[j]))

    # 5. 시작점 찾기 (수정: 가장 왼쪽을 1순위로, 맨 아래를 2순위로)
    V_0 = None
    for v in edges.keys():
        if V_0 is None:
            V_0 = v
        else:
            if v[0] < V_0[0] or (v[0] == V_0[0] and v[1] < V_0[1]):
                V_0 = v

    def get_dir(u, v):
        if v[0] > u[0]: return 0
        if v[1] > u[1]: return 1
        if v[0] < u[0]: return 2
        if v[1] < u[1]: return 3
        return -1

    def turn_rank(cdir, ndir):
        turn = (ndir - cdir) % 4
        if turn == 3: return 4
        if turn == 0: return 3
        if turn == 1: return 2
        if turn == 2: return 1
        return 0

    # 6. 최외곽 경계선 추적
    curr_v = V_0
    curr_dir = 0
    path = [curr_v]

    while True:
        cands = edges[curr_v]
        if not cands: break
        
        best_cand = None
        best_rank = -1
        best_dir = -1
        
        for cand in cands:
            ndir = get_dir(curr_v, cand)
            rank = turn_rank(curr_dir, ndir)
            if rank > best_rank:
                best_rank = rank
                best_cand = cand
                best_dir = ndir
                
        next_v = best_cand
        edges[curr_v].remove(next_v)
        
        if next_v == V_0:
            break
            
        path.append(next_v)
        curr_dir = best_dir
        curr_v = next_v

    # 7. 모서리만 추출
    corners = []
    N_path = len(path)
    for i in range(N_path):
        prev_v = path[(i-1) % N_path]
        curr_v = path[i]
        next_v = path[(i+1) % N_path]
        
        if get_dir(prev_v, curr_v) != get_dir(curr_v, next_v):
            corners.append(curr_v)

    # 8. 가장 왼쪽, 맨 아래 꼭짓점을 시작점으로 배열 회전 (수정된 로직)
    min_idx = 0
    for i in range(1, len(corners)):
        if corners[i][0] < corners[min_idx][0]:
            min_idx = i
        elif corners[i][0] == corners[min_idx][0] and corners[i][1] < corners[min_idx][1]:
            min_idx = i
            
    corners = corners[min_idx:] + corners[:min_idx]

    # 출력
    print(len(corners))
    for x, y in corners:
        print(f"{x} {y}")

if __name__ == '__main__':
    solve()

################################################################################################



