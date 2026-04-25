# 라이브러리(sys, heapq 등)를 사용하지 않는 순수 알고리즘 구현

def solve():
    # 1. 입력 처리 (빠른 처리를 위해 표준 입력을 한꺼번에 읽음)
    try:
        import sys
        input_data = sys.stdin.read().split()
    except EOFError:
        return
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    
    vx = [0] * n
    vy = [0] * n
    for i in range(n):
        vx[i] = int(next(it))
        vy[i] = int(next(it))
        
    # 수평 선분 정보 추출 (x1, x2, y)
    segs_y = []
    segs_w = []
    for i in range(1, n - 1, 2):
        segs_y.append(vy[i])
        segs_w.append(vx[i+1] - vx[i])
        
    m = len(segs_y)
    k_holes = int(next(it))

    # 2. 데카르트 트리 빌드 (O(N))
    left = [-1] * m
    right = [-1] * m
    parent = [-1] * m
    stack = []
    for i in range(m):
        last = -1
        while stack and segs_y[stack[-1]] > segs_y[i]:
            last = stack.pop()
        if stack:
            right[stack[-1]] = i
            parent[i] = stack[-1]
        if last != -1:
            left[i] = last
            parent[last] = i
        stack.append(i)
    
    root = stack[0] if stack else -1
    if root == -1:
        print(0)
        return

    # 3. 트리 탐색 (반복문을 이용한 후위 순회로 재귀 제한 회피)
    total_w = [0] * m
    dp = [0] * m        # 해당 노드를 시작으로 리프까지의 최대 경로 합
    heavy = [-1] * m    # 최대 경로를 형성하는 자식 노드
    light = [-1] * m    # 나머지 자식 노드

    order = []
    search_stack = [root]
    while search_stack:
        u = search_stack.pop()
        order.append(u)
        if left[u] != -1: search_stack.append(left[u])
        if right[u] != -1: search_stack.append(right[u])

    for u in reversed(order):
        total_w[u] = segs_w[u]
        l_val = 0
        r_val = 0
        if left[u] != -1:
            total_w[u] += total_w[left[u]]
            l_val = dp[left[u]]
        if right[u] != -1:
            total_w[u] += total_w[right[u]]
            r_val = dp[right[u]]
        
        # 증분 면적 계산
        p_y = segs_y[parent[u]] if parent[u] != -1 else 0
        inc_area = total_w[u] * (segs_y[u] - p_y)
        
        # 더 큰 경로 선택
        if l_val >= r_val:
            dp[u] = inc_area + l_val
            heavy[u] = left[u]
            light[u] = right[u]
        else:
            dp[u] = inc_area + r_val
            heavy[u] = right[u]
            light[u] = left[u]

    # 4. 최대 힙(Heap) 구현 및 그리디 경로 선택
    heap = []
    def heap_push(val, node):
        heap.append((val, node))
        curr = len(heap) - 1
        while curr > 0:
            p = (curr - 1) // 2
            if heap[curr][0] > heap[p][0]:
                heap[curr], heap[p] = heap[p], heap[curr]
                curr = p
            else: break

    def heap_pop():
        if not heap: return None
        res = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            curr = 0
            while True:
                l, r = curr * 2 + 1, curr * 2 + 2
                target = curr
                if l < len(heap) and heap[l][0] > heap[target][0]: target = l
                if r < len(heap) and heap[r][0] > heap[target][0]: target = r
                if target != curr:
                    heap[curr], heap[target] = heap[target], heap[curr]
                    curr = target
                else: break
        return res

    heap_push(dp[root], root)
    ans = 0
    selected_count = 0
    
    while heap and selected_count < k_holes:
        val, u = heap_pop()
        ans += val
        selected_count += 1
        
        # 선택된 경로를 따라 내려가며 가지치기 된 자식들을 힙에 추가
        curr = u
        while curr != -1:
            if light[curr] != -1:
                heap_push(dp[light[curr]], light[curr])
            curr = heavy[curr]

    print(ans)

solve()

##################################################################################

