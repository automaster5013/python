import sys
from collections import deque

def solve_v1():
    # 데이터를 한 번에 읽어와 리스트로 분리 (고속 IO)
    data = sys.stdin.read().split()
    if not data: return
    
    P = int(data[0])
    N = int(data[1])
    
    # 1번부터 P번까지의 피자 종류별 큐 생성 (0번 인덱스는 비워둠)
    pizza_queues = [deque() for _ in range(P + 1)]
    total_revenue = 0
    
    idx = 2
    for _ in range(N):
        cmd = int(data[idx])
        if cmd == 0:
            # 피자 생산: 종류(p), 가격(m)
            p = int(data[idx+1])
            m = int(data[idx+2])
            pizza_queues[p].append(m)
            idx += 3
        else:
            # 피자 주문: 종류(p)
            p = int(data[idx+1])
            if pizza_queues[p]:
                # 가장 먼저 만든 피자의 가격을 매출에 합산
                total_revenue += pizza_queues[p].popleft()
            idx += 2
            
    print(total_revenue)

solve_v1()

#########################################################################

from collections import deque
import sys

def solve_v2():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    P, N = int(next(it)), int(next(it))
    
    # 존재하는 종류만 동적으로 큐를 생성
    storage = {}
    revenue = 0
    
    for _ in range(N):
        cmd = int(next(it))
        p = int(next(it))
        
        if cmd == 0:
            m = int(next(it))
            if p not in storage:
                storage[p] = deque()
            storage[p].append(m)
        else:
            # 해당 종류의 피자가 있고 큐가 비어있지 않은지 확인
            if p in storage and storage[p]:
                revenue += storage[p].popleft()
                
    print(revenue)

solve_v2()

#########################################################################

def solve_v3():
    import sys
    tokens = sys.stdin.read().split()
    P, N = int(tokens[0]), int(tokens[1])
    
    pizzas = [[] for _ in range(P + 1)]
    heads = [0] * (P + 1) # 각 큐의 시작점을 가리키는 포인터
    total = 0
    
    ptr = 2
    for _ in range(N):
        cmd = int(tokens[ptr])
        p = int(tokens[ptr+1])
        if cmd == 0:
            m = int(tokens[ptr+2])
            pizzas[p].append(m)
            ptr += 3
        else:
            # 포인터가 리스트 길이보다 작으면 피자가 남아있는 것
            if heads[p] < len(pizzas[p]):
                total += pizzas[p][heads[p]]
                heads[p] += 1
            ptr += 2
            
    print(total)

solve_v3()

#########################################################################

class PizzaShop:
    def __init__(self, p_count):
        from collections import deque
        self.inventory = [deque() for _ in range(p_count + 1)]
        self.revenue = 0

    def produce(self, p_type, price):
        self.inventory[p_type].append(price)

    def order(self, p_type):
        if self.inventory[p_type]:
            self.revenue += self.inventory[p_type].popleft()

def solve_v4():
    import sys
    it = iter(sys.stdin.read().split())
    shop = PizzaShop(int(next(it)))
    N = int(next(it))
    
    for _ in range(N):
        cmd = int(next(it))
        p = int(next(it))
        if cmd == 0:
            shop.produce(p, int(next(it)))
        else:
            shop.order(p)
    print(shop.revenue)

solve_v4()

#########################################################################

import sys
from collections import deque

def solve_v5():
    # 입력을 토큰화하여 리스트로 저장
    raw = sys.stdin.read().split()
    if not raw: return
    
    p_queues = [deque() for _ in range(int(raw[0]) + 1)]
    total = 0
    ptr = 2
    
    while ptr < len(raw):
        cmd = raw[ptr]
        p_type = int(raw[ptr+1])
        
        if cmd == '0':
            p_queues[p_type].append(int(raw[ptr+2]))
            ptr += 3
        else:
            if p_queues[p_type]:
                total += p_queues[p_type].popleft()
            ptr += 2
            
    sys.stdout.write(str(total) + '\n')

if __name__ == "__main__":
    solve_v5()

#########################################################################





