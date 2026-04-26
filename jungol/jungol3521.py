import sys

def solve():
    # 1. 입력 받기
    try:
        data = list(map(int, sys.stdin.read().split()))
        if len(data) < 6:
            return
        
        # a, b, c, d, e: 1, 2, 4, 8, 16그램 추의 개수
        # N: 목표 무게
        counts = data[:5]
        target_n = data[5]
    except (ValueError, EOFError):
        return

    # 무게 단위와 개수를 역순(큰 것부터)으로 매칭
    weights = [16, 8, 4, 2, 1]
    available_counts = counts[::-1] # e, d, c, b, a 순서로 변경
    
    total_used_weights = 0
    remaining_weight = target_n

    # 2. 그리디 탐색 시작
    for i in range(len(weights)):
        w = weights[i]
        count = available_counts[i]
        
        if remaining_weight == 0:
            break
            
        # 현재 무게에서 이 추를 최대 몇 개까지 쓸 수 있는지 계산
        needed = remaining_weight // w
        # 내가 가진 개수와 필요한 개수 중 작은 값을 선택
        use = min(needed, count)
        
        total_used_weights += use
        remaining_weight -= (use * w)

    # 3. 결과 출력
    if remaining_weight == 0:
        print(total_used_weights)
    else:
        print("impossible")

if __name__ == "__main__":
    solve()

###############################################################


