import sys
from collections import deque

# DSU find 연산 (경로 압축 적용)
def find(parent, i):
    root = i
    while parent[root] != root:
        root = parent[root]
    curr = i
    while parent[curr] != root:
        parent[curr], curr = root, parent[curr]
    return root

def solve():
    # 빠른 입출력
    data = sys.stdin.read().split()
    if not data:
        return
    
    N, K = int(data[0]), int(data[1])
    width = N + 2
    # grid: 0(미개), -1(경계), 1~K(문명 ID)
    grid = [0] * (width * width)
    
    # 그리드 경계 패딩 처리
    for i in range(width):
        grid[i] = -1
        grid[width * (width - 1) + i] = -1
        grid[i * width] = -1
        grid[i * width + width - 1] = -1
        
    parent = list(range(K + 1))
    sets_count = K
    q = deque()
    
    # 문명 결합 함수
    def dsu_union(i, j):
        nonlocal sets_count
        root1 = find(parent, i)
        root2 = find(parent, j)
        if root1 != root2:
            parent[root1] = root2
            sets_count -= 1
            return True
        return False

    # 발상지 정보 입력
    it = iter(data[2:])
    for i in range(1, K + 1):
        x, y = int(next(it)), int(next(it))
        pos = x * width + y
        if grid[pos] == 0:
            grid[pos] = i
            q.append(pos)
        else:
            # 동일 위치 발상지 처리
            dsu_union(i, grid[pos])

    moves = [-width, width, -1, 1]
    
    # 0년차: 인접한 발상지 결합
    initial_list = list(q)
    for pos in initial_list:
        cid = grid[pos]
        for m in moves:
            npos = pos + m
            nval = grid[npos]
            if nval > 0:
                dsu_union(cid, nval)
    
    # 처음부터 하나인 경우
    if sets_count <= 1:
        print(0)
        return

    year = 0
    while q:
        year += 1
        # 한 해 동안의 전파 처리
        for _ in range(len(q)):
            pos = q.popleft()
            cid = grid[pos]
            
            for m in moves:
                npos = pos + m
                val = grid[npos]
                
                if val == -1: continue # 경계
                
                if val == 0: # 미개 지역 전파
                    grid[npos] = cid
                    q.append(npos)
                    # 새롭게 문명이 된 곳에서 인접 문명 확인
                    for m2 in moves:
                        nnpos = npos + m2
                        nnval = grid[nnpos]
                        if nnval > 0:
                            if dsu_union(cid, nnval):
                                if sets_count == 1:
                                    print(year)
                                    return
                elif val > 0: # 다른 문명과 만남
                    if dsu_union(cid, val):
                        if sets_count == 1:
                            print(year)
                            return

if __name__ == "__main__":
    solve()

###############################################################

