import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    # 최소 영양 성분 기준
    mp, mf, ms, mv = map(int, input_data[1:5])
    
    # 식재료 정보 저장 (단백질, 지방, 탄수화물, 비타민, 가격)
    ingredients = []
    idx = 5
    for _ in range(N):
        ingredients.append(list(map(int, input_data[idx:idx+5])))
        idx += 5

    min_cost = float('inf')
    best_path = []

    # 백트래킹 함수
    def find_combination(depth, p, f, s, v, cost, path):
        nonlocal min_cost, best_path
        
        # 조건 충족 확인
        if p >= mp and f >= mf and s >= ms and v >= mv:
            # 현재 비용이 더 저렴한 경우 갱신
            if cost < min_cost:
                min_cost = cost
                best_path = path[:]
            # 비용이 같은 경우 사전식 순서 비교
            elif cost == min_cost:
                if not best_path or path < best_path:
                    best_path = path[:]
            # 조건을 만족한 시점에서 더 재료를 추가할 필요는 없지만, 
            # 가격이 0인 재료가 있을 수 있으므로 탐색을 지속하거나 
            # 문제 조건에 따라 최적화할 수 있습니다. 
            # (이 문제에서는 더 깊이 탐색해도 사전식에서 밀릴 가능성이 큼)

        if depth == N:
            return

        # 1. 현재 재료를 선택하는 경우
        find_combination(
            depth + 1, 
            p + ingredients[depth][0], 
            f + ingredients[depth][1], 
            s + ingredients[depth][2], 
            v + ingredients[depth][3], 
            cost + ingredients[depth][4], 
            path + [depth + 1]
        )
        
        # 2. 현재 재료를 선택하지 않는 경우
        find_combination(depth + 1, p, f, s, v, cost, path)

    # 탐색 시작
    find_combination(0, 0, 0, 0, 0, 0, [])

    # 결과 출력
    if min_cost == float('inf'):
        print("-1")
    else:
        print(min_cost)
        print(*(best_path))

if __name__ == "__main__":
    # 재귀 깊이 제한 설정
    sys.setrecursionlimit(2000)
    solve()

#######################################################################

