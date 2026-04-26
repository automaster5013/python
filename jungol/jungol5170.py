import sys

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    # 나무 높이들을 정수로 변환하여 리스트에 저장
    trees = [int(x) for x in input_data[2:]]
    
    # 이진 탐색 범위 설정
    low = 0
    high = max(trees)
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        # mid 높이로 잘랐을 때 가져가는 나무의 총합 계산
        # h > mid 인 나무들만 (h - mid) 만큼 가져감
        total = 0
        for h in trees:
            if h > mid:
                total += h - mid
        
        if total >= m:
            # 나무가 충분함 -> 높이를 더 높여도 되는지 확인
            ans = mid
            low = mid + 1
        else:
            # 나무가 부족함 -> 높이를 낮춰야 함
            high = mid - 1
            
    print(ans)

if __name__ == "__main__":
    solve_v1()

###################################################################

import sys

def solve_v2():
    it = iter(sys.stdin.read().split())
    n, m = int(next(it)), int(next(it))
    trees = [int(x) for x in it]
    
    l, r = 0, max(trees)
    result = 0
    
    while l <= r:
        mid = (l + r) // 2
        # 한 줄로 요약된 나무 합산 로직 (C언어 수준의 내부 루프 활용)
        got = sum(h - mid for h in trees if h > mid)
        
        if got >= m:
            result = mid
            l = mid + 1
        else:
            r = mid - 1
    print(result)

solve_v2()

###################################################################

class LoggingSystem:
    def __init__(self, trees):
        self.trees = trees
        self.max_h = max(trees)

    def calculate_wood(self, cutter_h):
        return sum(t - cutter_h for t in self.trees if t > cutter_h)

    def find_best_height(self, target_m):
        low, high = 0, self.max_h
        best_h = 0
        while low <= high:
            mid = (low + high) // 2
            if self.calculate_wood(mid) >= target_m:
                best_h = mid
                low = mid + 1
            else:
                high = mid - 1
        return best_h

def solve_v3():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    system = LoggingSystem(data[2:])
    print(system.find_best_height(data[1]))

solve_v3()

###################################################################

