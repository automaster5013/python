import sys
import heapq

# 재귀 깊이 제한 확장 (20만 노드 처리용)
sys.setrecursionlimit(300000)

def solve():
    # 대량의 입력을 효율적으로 읽기 위한 제너레이터
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token
    
    tokens = get_tokens()
    try:
        first_token = next(tokens)
    except StopIteration:
        return
        
    N = int(first_token)
    E = int(next(tokens))
    
    # 각 교차점의 상금/벌금 정보 (1번 노드부터 시작)
    C = [0] * (N + 1)
    for i in range(1, N + 1):
        C[i] = int(next(tokens))
        
    # 트리 인접 리스트 구축
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(next(tokens))
        v = int(next(tokens))
        adj[u].append(v)
        adj[v].append(u)
        
    # 1번 노드를 루트로 하여 부모 관계와 탐색 순서(Post-order) 생성
    parent = [-1] * (N + 1)
    on_path = [False] * (N + 1)
    stack = [1]
    visit_order = []
    while stack:
        u = stack.pop()
        visit_order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
                
    # 도착점 E로부터 역추적하여 경로(1 -> ... -> E)를 찾음
    curr = E
    path = []
    while curr != -1:
        on_path[curr] = True
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    
    # 각 노드별 서브트리 요약 정보를 담을 힙(Small-to-Large merging용)
    heaps = [[] for _ in range(N + 1)]
    
    # 하향식으로 서브트리 정보 요약
    for u in reversed(visit_order):
        if not on_path[u]:
            # 자식 노드들의 요약 정보를 현재 노드로 병합
            for v in adj[u]:
                if v == parent[u]: continue
                # 성능을 위해 작은 힙을 큰 힙으로 병합
                if len(heaps[v]) > len(heaps[u]):
                    heaps[u], heaps[v] = heaps[v], heaps[u]
                for unit in heaps[v]:
                    heapq.heappush(heaps[u], unit)
                heaps[v] = [] # 메모리 해제
            
            # 현재 노드 u의 상금/벌금 처리
            if C[u] > 0:
                heapq.heappush(heaps[u], (0, C[u]))
            elif C[u] < 0:
                cur_m = -C[u] # 필요한 최소 상금
                cur_g = C[u]  # 현재 순이익
                # 벌금을 메울 수 있는 자식 서브트리 유닛들을 상금이 적게 드는 순서로 사용
                while heaps[u] and cur_g <= 0:
                    m, g = heapq.heappop(heaps[u])
                    cur_m = max(cur_m, m - cur_g)
                    cur_g += g
                # 최종적으로 이익이 나는 경우에만 새로운 유닛으로 등록
                if cur_g > 0:
                    heapq.heappush(heaps[u], (cur_m, cur_g))
                else:
                    heaps[u] = []
        else:
            # 경로 위에 있는 노드는 인접한 '경로 밖' 서브트리들만 병합해둠
            for v in adj[u]:
                if v == parent[u] or on_path[v]: continue
                if len(heaps[v]) > len(heaps[u]):
                    heaps[u], heaps[v] = heaps[v], heaps[u]
                for unit in heaps[v]:
                    heapq.heappush(heaps[u], unit)
                heaps[v] = []

    # 경로 따라 이동하며 탈출 시도
    current_reward = 0
    available_units = []
    for u in path:
        # 현재 위치에서 접근 가능한 서브트리 파밍 유닛들을 추가
        for unit in heaps[u]:
            heapq.heappush(available_units, unit)
        heaps[u] = [] # 메모리 해제
        
        # 이동 전: 현재 가진 돈으로 파밍할 수 있는 모든 서브트리 방문
        while available_units and current_reward >= available_units[0][0]:
            current_reward += heapq.heappop(available_units)[1]
        
        # 벌금 지불 확인
        if C[u] < 0:
            if current_reward < -C[u]:
                print("trapped")
                return
        
        # 상금 획득 또는 벌금 지불
        current_reward += C[u]
        
        # 이동 후: 늘어난 상금으로 추가 파밍이 가능한지 확인
        while available_units and current_reward >= available_units[0][0]:
            current_reward += heapq.heappop(available_units)[1]
            
    print("escaped")

if __name__ == "__main__":
    solve()

################################################################################

