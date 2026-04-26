import sys

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 토큰화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    beads = [int(x) for x in input_data[2:]]
    
    # 이진 탐색 범위 설정
    low = max(beads)   # 한 그룹의 합은 최소한 가장 큰 구슬보다는 커야 함
    high = sum(beads)  # 모든 구슬을 한 그룹으로 묶을 때
    ans = high
    
    while low <= high:
        mid = (low + high) // 2 # 우리가 시도할 '그룹 합의 최댓값'
        
        # 결정 함수: mid를 상한선으로 했을 때 그룹이 몇 개 나오는지 확인
        count = 1
        current_sum = 0
        for x in beads:
            if current_sum + x > mid:
                count += 1
                current_sum = x
            else:
                current_sum += x
        
        if count <= m:
            # 그룹 수가 M개 이하로 가능하다면, 상한선(mid)을 더 줄여본다.
            ans = mid
            high = mid - 1
        else:
            # 그룹 수가 너무 많이 나오면, 상한선(mid)을 높여야 한다.
            low = mid + 1
            
    print(ans)

if __name__ == "__main__":
    solve_v1()

############################################################################

import sys

def can_divide(limit, beads, m):
    group_count = 1
    temp_sum = 0
    for b in beads:
        if temp_sum + b > limit:
            group_count += 1
            temp_sum = b
        else:
            temp_sum += b
    return group_count <= m

def solve_v2():
    it = iter(sys.stdin.read().split())
    try:
        n, m = int(next(it)), int(next(it))
        beads = [int(next(it)) for _ in range(n)]
        
        low, high = max(beads), sum(beads)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_divide(mid, beads, m):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        print(result)
    except StopIteration:
        pass

solve_v2()

############################################################################

class BeadDistributor:
    def __init__(self, n, m, values):
        self.n = n
        self.m = m
        self.values = values

    def get_min_max_sum(self):
        start, end = max(self.values), sum(self.values)
        ans = end
        
        while start <= end:
            mid = (start + end) // 2
            if self._is_possible(mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans

    def _is_possible(self, limit):
        cnt, s = 1, 0
        for v in self.values:
            if s + v > limit:
                cnt += 1
                s = v
            else:
                s += v
        return cnt <= self.m

def solve_v3():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    if data:
        distributor = BeadDistributor(data[0], data[1], data[2:])
        print(distributor.get_min_max_sum())

solve_v3()

############################################################################


