import sys

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0]) # 마을 수
    c = int(input_data[1]) # 트럭 용량
    m = int(input_data[2]) # 박스 정보 개수
    
    # 박스 정보: (보내는 마을, 받는 마을, 박스 개수)
    box_info = []
    idx = 3
    for _ in range(m):
        box_info.append((int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])))
        idx += 3
        
    # 핵심: 받는 마을(도착지) 기준으로 오름차순 정렬
    box_info.sort(key=lambda x: x[1])
    
    # 각 마을 사이 구간의 현재 적재량을 저장하는 배열
    # capacities[i]는 i번 마을에서 i+1번 마을로 갈 때의 적재량
    capacities = [0] * (n + 1)
    total_delivered = 0
    
    for start, end, count in box_info:
        # 1. 현재 구간(start ~ end-1)에서 이미 실려 있는 박스 중 최대치를 찾음
        max_current_load = 0
        for i in range(start, end):
            if capacities[i] > max_current_load:
                max_current_load = capacities[i]
        
        # 2. 이번에 더 실을 수 있는 최대 양 계산
        can_take = min(count, c - max_current_load)
        
        # 3. 트럭에 싣고 배송량 합산
        if can_take > 0:
            for i in range(start, end):
                capacities[i] += can_take
            total_delivered += can_take
            
    print(total_delivered)

if __name__ == "__main__":
    solve_v1()

############################################################################

import sys

def solve_v2():
    it = iter(map(int, sys.stdin.read().split()))
    n, c = next(it), next(it)
    m = next(it)
    
    # 도착지 기준 정렬
    orders = sorted([ (next(it), next(it), next(it)) for _ in range(m) ], key=lambda x: x[1])
    
    # 남은 용량을 관리하는 배열 (트럭 용량으로 초기화)
    remains = [c] * (n + 1)
    ans = 0
    
    for s, e, count in orders:
        # 구간 내에서 가장 적게 남은 용량을 확인
        available = min(remains[s:e])
        to_load = min(count, available)
        
        # 용량 차감 및 결과 합산
        for i in range(s, e):
            remains[i] -= to_load
        ans += to_load
        
    print(ans)

solve_v2()

############################################################################

class DeliveryTruck:
    def __init__(self, capacity, village_count):
        self.capacity = capacity
        self.current_load = [0] * (village_count + 1)
        self.total_delivered = 0

    def process_order(self, start, end, amount):
        # 해당 구간의 최대 적재량 확인
        max_load = max(self.current_load[start:end])
        # 실을 수 있는 양 결정
        can_load = min(amount, self.capacity - max_load)
        
        if can_load > 0:
            for i in range(start, end):
                self.current_load[i] += can_load
            self.total_delivered += can_load

def solve_v3():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    n, c, m = data[0], data[1], data[2]
    
    orders = []
    for i in range(m):
        orders.append(data[3 + i*3 : 6 + i*3])
    orders.sort(key=lambda x: x[1])
    
    truck = DeliveryTruck(c, n)
    for s, e, amt in orders:
        truck.process_order(s, e, amt)
        
    print(truck.total_delivered)

solve_v3()

############################################################################

