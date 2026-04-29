import sys
from collections import deque

def solve():
    # 1. 모든 데이터를 한꺼번에 읽어오기 (가장 큰 속도 향상 포인트)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    r1 = int(input_data[1])
    r2 = int(input_data[2])
    
    if r1 == r2:
        print(0)
        return

    # 2. 인접 리스트 구성
    adj = [[] for _ in range(n + 1)]
    ptr = 3
    # N-1개의 간선 정보를 빠르게 처리
    for _ in range(n - 1):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        w = int(input_data[ptr+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        ptr += 3

    # 3. BFS 최적화: 객체 생성 최소화
    # parent_node와 parent_weight를 분리하여 메모리 오버헤드 감소
    parent_node = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    
    queue = deque([r1])
    parent_node[r1] = -1 # 시작 노드 표시
    
    found = False
    while queue:
        u = queue.popleft()
        if u == r2:
            found = True
            break
        
        for v, w in adj[u]:
            if parent_node[v] == 0: # 방문하지 않은 노드
                parent_node[v] = u
                parent_weight[v] = w
                queue.append(v)
        if found:
            break

    # 4. 경로 역추적 및 결과 계산
    total_dist = 0
    max_dist = 0
    curr = r2
    
    # 루트(-1)에 도달할 때까지 역추적
    while parent_node[curr] != -1:
        w = parent_weight[curr]
        total_dist += w
        if w > max_dist:
            max_dist = w
        curr = parent_node[curr]

    # (전체 경로 길이) - (가장 긴 통로 길이)
    sys.stdout.write(str(total_dist - max_dist) + '\n')

if __name__ == "__main__":
    solve()

##################################################################


