import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 추의 개수
    weights = list(map(int, input_data[1:n+1])) # 추의 무게들
    
    m = int(input_data[n+1]) # 구슬의 개수
    marbles = list(map(int, input_data[n+2:])) # 구슬의 무게들
    
    # 2. 가능한 무게 조합 찾기 (Set 활용 DP)
    # possible_weights: 현재까지의 추들로 측정 가능한 무게의 집합
    possible_weights = {0}
    
    for w in weights:
        new_weights = set()
        for p in possible_weights:
            # 세 가지 경우의 수를 모두 집합에 추가
            new_weights.add(p + w)          # 반대편에 놓기
            new_weights.add(abs(p - w))     # 같은 편에 놓기
            new_weights.add(p)              # 안 놓기
        possible_weights = new_weights

    # 3. 구슬 확인 및 결과 출력
    results = []
    for g in marbles:
        # 구슬 무게가 측정 가능한 집합에 있는지 확인
        if g in possible_weights:
            results.append("Y")
        else:
            results.append("N")
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()

#############################################################################

