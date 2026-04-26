import sys

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 각 지방의 예산 요청 리스트
    requests = [int(x) for x in input_data[1:n+1]]
    m = int(input_data[n+1])
    
    # 이진 탐색 범위: 0원부터 요청액 중 최대금액까지
    low = 0
    high = max(requests)
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        # 현재 상한액(mid)으로 배정했을 때의 총액 계산
        current_sum = 0
        for r in requests:
            if r > mid:
                current_sum += mid
            else:
                current_sum += r
        
        if current_sum <= m:
            # 예산 내에 들어오면, 상한액을 더 키워봅니다.
            ans = mid
            low = mid + 1
        else:
            # 예산 초과면, 상한액을 줄입니다.
            high = mid - 1
            
    print(ans)

if __name__ == "__main__":
    solve_v1()

#############################################################

import sys

def solve_v2():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    reqs = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    
    l, r = 0, max(reqs)
    result = 0
    
    while l <= r:
        limit = (l + r) // 2
        # 상한액보다 크면 limit, 작으면 r을 더함
        total = sum(r if r <= limit else limit for r in reqs)
        
        if total <= m:
            result = limit
            l = limit + 1
        else:
            r = limit - 1
    print(result)

solve_v2()

#############################################################

class BudgetDistributor:
    def __init__(self, requests, total_budget):
        self.requests = requests
        self.total_budget = total_budget

    def calculate_allocated_sum(self, limit):
        return sum(min(req, limit) for req in self.requests)

    def find_max_limit(self):
        low, high = 0, max(self.requests)
        best_limit = 0
        while low <= high:
            mid = (low + high) // 2
            if self.calculate_allocated_sum(mid) <= self.total_budget:
                best_limit = mid
                low = mid + 1
            else:
                high = mid - 1
        return best_limit

def solve_v3():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    distributor = BudgetDistributor(data[1:n+1], data[n+1])
    print(distributor.find_max_limit())

solve_v3()

#############################################################



#############################################################



