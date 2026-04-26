import sys

def solve_v1():
    # 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    chemicals = []
    
    # 화학 물질 정보를 [최저, 최고] 리스트로 저장
    for i in range(n):
        low = int(input_data[2*i + 1])
        high = int(input_data[2*i + 2])
        chemicals.append([low, high])
        
    # 1. 최고 온도(y_i)를 기준으로 오름차순 정렬
    # 빨리 상하는 것부터 기준을 잡기 위함입니다.
    chemicals.sort(key=lambda x: x[1])
    
    count = 0
    # 현재 냉장고의 유지 온도 (초기값은 아주 낮은 온도로 설정)
    current_fridge_temp = -1000 
    
    for low, high in chemicals:
        # 2. 현재 냉장고 온도가 이 물질의 최저 보관 온도보다 낮다면
        # 새로운 냉장고가 필요합니다.
        if current_fridge_temp < low:
            count += 1
            # 새 냉장고 온도는 현재 물질의 최고 온도에 맞춥니다.
            # (그래야 뒤에 오는 물질들을 최대한 많이 포함할 수 있습니다.)
            current_fridge_temp = high
            
    print(count)

if __name__ == "__main__":
    solve_v1()

###########################################################################

import sys

def get_min_fridges(n, chemicals):
    # 최고 온도 기준 정렬
    chemicals.sort(key=lambda x: x[1])
    
    count = 0
    last_temp = -float('inf')
    
    for low, high in chemicals:
        if last_temp < low:
            count += 1
            last_temp = high
    return count

def solve_v2():
    it = iter(map(int, sys.stdin.read().split()))
    try:
        n = next(it)
        chems = []
        for _ in range(n):
            chems.append([next(it), next(it)])
        print(get_min_fridges(n, chems))
    except StopIteration:
        pass

solve_v2()

###########################################################################

class Chemical:
    def __init__(self, low, high):
        self.low = low
        self.high = high

def solve_v3():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    chemicals = []
    for i in range(n):
        chemicals.append(Chemical(data[2*i+1], data[2*i+2]))
        
    # 최고 온도 기준 정렬
    chemicals.sort(key=lambda c: c.high)
    
    fridge_count = 0
    ref_temp = -1000
    
    for c in chemicals:
        if ref_temp < c.low:
            fridge_count += 1
            ref_temp = c.high
            
    print(fridge_count)

solve_v3()

###########################################################################

