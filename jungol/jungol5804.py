import sys

def solve_v1():
    # 고속 입력을 위해 전체 읽기
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N = int(input_data[0])
    C = int(input_data[1])
    # 위치 정보 정렬
    pos = sorted([int(input_data[i]) for i in range(2, N + 2)])
    
    start = 1
    end = pos[-1] - pos[0]
    result = 0
    
    while start <= end:
        mid = (start + end) // 2 # 인접한 두 나무 사이의 최소 거리 후보
        
        # 결정 함수: 거리 mid 이상으로 C그루를 심을 수 있는가?
        count = 1
        last_installed = pos[0]
        
        for i in range(1, N):
            if pos[i] - last_installed >= mid:
                count += 1
                last_installed = pos[i]
        
        if count >= C:
            # 성공: 거리를 더 늘려본다
            result = mid
            start = mid + 1
        else:
            # 실패: 거리를 줄여야 한다
            end = mid - 1
            
    print(result)

if __name__ == "__main__":
    solve_v1()

########################################################################

import sys

def is_possible(dist, pos, C):
    count = 1
    last = pos[0]
    for i in range(1, len(pos)):
        if pos[i] - last >= dist:
            count += 1
            last = pos[i]
    return count >= C

def solve_v2():
    it = iter(sys.stdin.read().split())
    N, C = int(next(it)), int(next(it))
    pos = sorted([int(next(it)) for _ in range(N)])
    
    low, high = 1, pos[-1] - pos[0]
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid, pos, C):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

solve_v2()

########################################################################

class TreePlanter:
    def __init__(self, positions, count_needed):
        self.pos = sorted(positions)
        self.C = count_needed

    def can_plant(self, min_dist):
        count = 1
        current_pos = self.pos[0]
        for i in range(1, len(self.pos)):
            if self.pos[i] - current_pos >= min_dist:
                count += 1
                current_pos = self.pos[i]
        return count >= self.C

    def find_max_min_dist(self):
        low, high = 1, self.pos[-1] - self.pos[0]
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if self.can_plant(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result

def solve_v3():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    planter = TreePlanter(data[2:], data[1])
    print(planter.find_max_min_dist())

solve_v3()

########################################################################

