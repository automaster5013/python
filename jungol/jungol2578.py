import sys
from collections import deque

def solve():
    # 1. 입력 가속 (그램의 RAM을 효율적으로 쓰기 위해 split 사용)
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    m, n = int(input_data[0]), int(input_data[1])
    k = int(input_data[2])
    
    h_buses = [] # (y, x1, x2, id)
    v_buses = [] # (x, y1, y2, id)
    
    ptr = 3
    for _ in range(k):
        b_id, x1, y1, x2, y2 = map(int, input_data[ptr:ptr+5])
        ptr += 5
        if y1 == y2: # 수평 버스
            h_buses.append((y1, min(x1, x2), max(x1, x2), b_id))
        else: # 수직 버스
            v_buses.append((x1, min(y1, y2), max(y1, y2), b_id))
            
    sx, sy, dx, dy = map(int, input_data[ptr:ptr+4])

    # 2. 출발지/목적지 버스 인덱스 찾기
    start_nodes = []
    target_ids = set()
    
    # H 버스 처리
    for i in range(len(h_buses)):
        y, x1, x2, b_id = h_buses[i]
        if y == sy and x1 <= sx <= x2: start_nodes.append(('h', i))
        if y == dy and x1 <= dx <= x2: target_ids.add(('h', i))
            
    # V 버스 처리
    for i in range(len(v_buses)):
        x, y1, y2, b_id = v_buses[i]
        if x == sx and y1 <= sy <= y2: start_nodes.append(('v', i))
        if x == dx and y1 <= dy <= y2: target_ids.add(('v', i))

    # 3. BFS (인접 리스트 없이 즉시 교차 판정으로 메모리 절약)
    visited_h = [-1] * len(h_buses)
    visited_v = [-1] * len(v_buses)
    queue = deque()
    
    for type, idx in start_nodes:
        if type == 'h':
            visited_h[idx] = 1
            queue.append(('h', idx))
        else:
            visited_v[idx] = 1
            queue.append(('v', idx))

    while queue:
        type, idx = queue.popleft()
        dist = visited_h[idx] if type == 'h' else visited_v[idx]
        
        if (type, idx) in target_ids:
            print(dist)
            return

        if type == 'h':
            y_h, x1_h, x2_h, _ = h_buses[idx]
            # H vs H (같은 y축 상에서 겹치는지)
            for i in range(len(h_buses)):
                if visited_h[i] == -1:
                    y, x1, x2, _ = h_buses[i]
                    if y == y_h and not (x2 < x1_h or x2_h < x1):
                        visited_h[i] = dist + 1
                        queue.append(('h', i))
            # H vs V (교차하는지)
            for i in range(len(v_buses)):
                if visited_v[i] == -1:
                    x_v, y1_v, y2_v, _ = v_buses[i]
                    if x1_h <= x_v <= x2_h and y1_v <= y_h <= y2_v:
                        visited_v[i] = dist + 1
                        queue.append(('v', i))
        else:
            x_v, y1_v, y2_v, _ = v_buses[idx]
            # V vs V (같은 x축 상에서 겹치는지)
            for i in range(len(v_buses)):
                if visited_v[i] == -1:
                    x, y1, y2, _ = v_buses[i]
                    if x == x_v and not (y2 < y1_v or y2_v < y1):
                        visited_v[i] = dist + 1
                        queue.append(('v', i))
            # V vs H (교차하는지)
            for i in range(len(h_buses)):
                if visited_h[i] == -1:
                    y_h, x1_h, x2_h, _ = h_buses[i]
                    if x1_h <= x_v <= x2_h and y1_v <= y_h <= y2_v:
                        visited_h[i] = dist + 1
                        queue.append(('h', i))

solve()

#############################################################################

