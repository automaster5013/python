import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(2000)

def solve():
    # 모든 입력을 한 번에 읽어와 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    while ptr < len(input_data):
        n = int(input_data[ptr])
        r = int(input_data[ptr+1])
        ptr += 2
        
        # 종료 조건
        if n == 0 and r == 0:
            break
            
        # 인접 리스트 생성 (무방향 트리)
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(input_data[ptr])
            v = int(input_data[ptr+1])
            w = int(input_data[ptr+2])
            adj[u].append((v, w))
            adj[v].append((u, w))
            ptr += 3
            
        def get_min_cut(u, p):
            # 현재 노드 u의 자식들 탐색
            total_cost = 0
            is_leaf = True
            
            for v, w in adj[u]:
                if v == p:
                    continue
                
                is_leaf = False
                # 자식 노드의 DP 결과값
                child_res = get_min_cut(v, u)
                
                if child_res == float('inf'):
                    # 자식이 잎 노드라면 해당 간선을 무조건 잘라야 함
                    total_cost += w
                else:
                    # 내부 노드라면 (간선 자르기)와 (하위에서 자르기) 중 최솟값 선택
                    total_cost += min(w, child_res)
            
            # 잎 노드인 경우 무한대 반환 (부모가 간선 가중치를 선택하도록 유도)
            if is_leaf and u != r:
                return float('inf')
            
            return total_cost

        # 결과 출력
        print(get_min_cut(r, -1))

if __name__ == "__main__":
    solve()

####################################################################################


