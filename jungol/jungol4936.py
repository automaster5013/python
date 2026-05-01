import sys

def solve():
    # 고속 입력을 사용하여 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))

    # 메모이제이션을 통해 중복 계산을 방지합니다.
    memo = {}

    def get_cost(t_idx):
        if t_idx in memo:
            return memo[t_idx]
        
        # b_i = a[i] + |t_idx - i|를 생성합니다.
        # 이 배열의 중앙값 부근이 최적의 H가 됩니다.
        b = [a[i] + abs(t_idx - i) for i in range(n)]
        b.sort()
        
        # 꼭대기 높이 H는 모든 i에 대해 H - |t_idx - i| >= 1을 만족해야 합니다.
        # 즉, H >= 1 + |t_idx - i| 가 모든 i에 대해 성립해야 하므로
        # H >= max(1 + t_idx, n - t_idx) 입니다 (0-indexed 기준).
        min_h = max(t_idx + 1, n - t_idx)
        
        # 비용 함수 f(H) = sum(|b[i] - H|)는 [b[(n-1)//2], b[n//2]] 구간에서 최소입니다.
        # 제약 조건 H >= min_h를 만족하는 최적의 H를 찾습니다.
        # f(H)는 볼록하므로 제약 범위 내에서 median에 가장 가까운 값을 선택하면 됩니다.
        target_h = max(min_h, b[(n - 1) // 2])
        
        # 누적 합을 사용하여 비용 계산을 O(N)에서 O(1)로 줄일 수도 있으나,
        # 파이썬의 sum() 함수가 내장함수로서 매우 빠르므로 직접 계산합니다.
        # 단, 더 빠른 계산을 위해 아래와 같이 작성합니다.
        cost = 0
        # h보다 작은 원소들과 큰 원소들의 차이를 합산
        # 이 부분은 median의 성질을 이용해 최적화할 수 있습니다.
        import bisect
        k = bisect.bisect_left(b, target_h)
        
        # 비용 = (target_h * k - (k개 원소의 합)) + ((나머지 원소의 합) - target_h * (n-k))
        # 여기서는 단순히 sum()을 쓰되, 반복 횟수를 고려해 최적화된 sum을 사용합니다.
        # 파이썬의 sum은 C로 구현되어 있어 빠릅니다.
        cost = sum(abs(x - target_h) for x in b)
        
        memo[t_idx] = cost
        return cost

    # 삼분 탐색 (Ternary Search)
    low, high = 0, n - 1
    # 80번 정도의 반복이면 10^5 범위를 충분히 정밀하게 좁힙니다.
    for _ in range(80):
        if high - low <= 2:
            break
        m1 = (2 * low + high) // 3
        m2 = (low + 2 * high) // 3
        
        if get_cost(m1) < get_cost(m2):
            high = m2
        else:
            low = m1
    
    # 최종 구간 내에서 최솟값 검색
    ans = float('inf')
    for t in range(max(0, low - 2), min(n, high + 3)):
        ans = min(ans, get_cost(t))
    
    print(ans)

if __name__ == "__main__":
    solve()

###################################################################
