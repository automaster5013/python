import sys

def solve():
    # 데이터 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    
    # 각 도시의 창고 건설 비용
    costs = []
    for _ in range(n):
        costs.append(int(input_data[ptr]))
        ptr += 1
        
    # 도로 정보 (인접 행렬)
    # reach[i][j]는 i에서 j로 갈 수 있는지 여부
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        line = input_data[ptr]
        ptr += 1
        for j in range(n):
            if line[j] == '1':
                reach[i][j] = True
        reach[i][i] = True # 자기 자신은 항상 도달 가능
        
    # 1. 플로이드-워셜로 모든 경로 유무 확인 (O(N^3))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
                    
    # 2. SCC 그룹화 및 최소 비용 합산
    visited = [False] * n
    total_min_cost = 0
    
    for i in range(n):
        if not visited[i]:
            # 새로운 SCC 발견
            curr_scc_min = costs[i]
            visited[i] = True
            
            # i와 서로 도달 가능한 정점들을 같은 SCC로 묶음
            for j in range(i + 1, n):
                if not visited[j] and reach[i][j] and reach[j][i]:
                    visited[j] = True
                    if costs[j] < curr_scc_min:
                        curr_scc_min = costs[j]
            
            total_min_cost += curr_scc_min
            
    # 결과 출력
    print(total_min_cost)

if __name__ == "__main__":
    solve()

#######################################################################

