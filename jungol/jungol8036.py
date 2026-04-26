import sys
from collections import Counter

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x_coords = []
    y_coords = []
    
    # x좌표와 y좌표를 각각 리스트에 담습니다.
    for i in range(n):
        x_coords.append(input_data[2*i + 1])
        y_coords.append(input_data[2*i + 2])
        
    # 각 좌표별 출현 빈도를 계산합니다.
    x_counts = Counter(x_coords)
    y_counts = Counter(y_coords)
    
    total_segments = 0
    
    # y축에 평행한 선분 (x값이 같은 점들의 조합)
    for count in x_counts.values():
        if count >= 2:
            total_segments += (count * (count - 1)) // 2
            
    # x축에 평행한 선분 (y값이 같은 점들의 조합)
    for count in y_counts.values():
        if count >= 2:
            total_segments += (count * (count - 1)) // 2
            
    print(total_segments)

if __name__ == "__main__":
    solve_v1()

###########################################################################

import sys

def solve_v2():
    input = sys.stdin.read().split()
    n = int(input[0])
    
    x_list = []
    y_list = []
    
    for i in range(n):
        x_list.append(int(input[2*i + 1]))
        y_list.append(int(input[2*i + 2]))
        
    # 좌표 정렬
    x_list.sort()
    y_list.sort()
    
    def count_pairs(arr):
        res = 0
        current_count = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                current_count += 1
            else:
                res += (current_count * (current_count - 1)) // 2
                current_count = 1
        # 마지막 그룹 처리
        res += (current_count * (current_count - 1)) // 2
        return res
        
    print(count_pairs(x_list) + count_pairs(y_list))

solve_v2()

###########################################################################

def solve_v3():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    
    x_map = {}
    y_map = {}
    
    for i in range(n):
        x, y = data[2*i+1], data[2*i+2]
        x_map[x] = x_map.get(x, 0) + 1
        y_map[y] = y_map.get(y, 0) + 1
        
    ans = 0
    # 수학적으로 n(n-1)/2를 적용
    for c in x_map.values():
        ans += c * (c - 1) // 2
    for c in y_map.values():
        ans += c * (c - 1) // 2
        
    print(ans)

solve_v3()

###########################################################################

class PointCloud:
    def __init__(self, n):
        self.n = n
        self.x_counts = {}
        self.y_counts = {}

    def add_point(self, x, y):
        self.x_counts[x] = self.x_counts.get(x, 0) + 1
        self.y_counts[y] = self.y_counts.get(y, 0) + 1

    def calculate_parallel_segments(self):
        total = 0
        for count in self.x_counts.values():
            total += (count * (count - 1)) // 2
        for count in self.y_counts.values():
            total += (count * (count - 1)) // 2
        return total

def solve_v4():
    import sys
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    cloud = PointCloud(n)
    for _ in range(n):
        cloud.add_point(next(it), next(it))
    print(cloud.calculate_parallel_segments())

solve_v4()

###########################################################################



###########################################################################





