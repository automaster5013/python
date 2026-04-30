import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 비용 행렬 (0-based 인덱스로 처리하기 위해 변환)
    costs = []
    idx = 1
    for _ in range(n):
        costs.append(list(map(int, input_data[idx:idx + n])))
        idx += n

    # dp[visited_mask][current_node]
    # visited_mask: 비트마스크로 표현된 방문 도시 집합
    # current_node: 현재 위치한 도시 번호
    inf = float('inf')
    dp = [[-1] * n for _ in range(1 << n)]

    def get_tsp(mask, curr):
        # 모든 도시를 방문한 경우
        if mask == (1 << n) - 1:
            # 마지막 도시에서 회사(0번)로 돌아가는 경로가 있는지 확인
            return costs[curr][0] if costs[curr][0] > 0 else inf
        
        # 이미 계산된 결과가 있는 경우 (메모이제이션)
        if dp[mask][curr] != -1:
            return dp[mask][curr]
        
        res = inf
        for next_node in range(n):
            # 아직 방문하지 않았고, 경로가 존재하는 도시라면
            if not (mask & (1 << next_node)) and costs[curr][next_node] > 0:
                # 다음 도시로 이동했을 때의 최솟값 계산
                temp = get_tsp(mask | (1 << next_node), next_node) + costs[curr][next_node]
                if temp < res:
                    res = temp
        
        dp[mask][curr] = res
        return res

    # 1번(0번 인덱스) 회사에서 출발
    result = get_tsp(1, 0)
    print(result)

if __name__ == "__main__":
    # 재귀 깊이 설정 (N=13이므로 기본값으로 충분하지만 안전을 위해 설정)
    sys.setrecursionlimit(2000)
    solve()

#############################################################################################

