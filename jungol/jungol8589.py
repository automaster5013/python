import heapq
import sys

def solve_v1():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    
    # 초기 돈 리스트를 최소 힙으로 변환
    money_heap = [int(x) for x in input_data[ptr:ptr+N]]
    heapq.heapify(money_heap)
    ptr += N
    
    M = int(input_data[ptr]); ptr += 1
    falling_money = [int(x) for x in input_data[ptr:ptr+M]]
    
    for x in falling_money:
        # 1. 가장 적은 돈을 가진 사람의 금액을 꺼냄 (O(log N))
        min_val = heapq.heappop(money_heap)
        # 2. 돈을 더해서 다시 넣음 (O(log N))
        heapq.heappush(money_heap, min_val + x)
        
    # 최종 결과는 오름차순 정렬하여 출력
    print(*(sorted(money_heap)))

if __name__ == "__main__":
    solve_v1()

#########################################################################

import heapq
import sys

def solve_v2():
    it = iter(sys.stdin.read().split())
    try:
        n = int(next(it))
        # 초기 데이터를 힙으로 생성
        heap = []
        for _ in range(n):
            heapq.heappush(heap, int(next(it)))
            
        m = int(next(it))
        for _ in range(m):
            drop = int(next(it))
            # 가장 작은 값을 꺼내고 동시에 새 값을 넣는 최적화 함수
            heapq.heapreplace(heap, heap[0] + drop)
            
        # 힙을 정렬된 리스트로 변환하여 출력
        print(*(sorted(heap)))
    except StopIteration:
        pass

solve_v2()

#########################################################################

import heapq

class MoneyManager:
    def __init__(self, initial_amounts):
        self.heap = initial_amounts
        heapq.heapify(self.heap)

    def add_money(self, amount):
        # 최하위 금액 소유자에게 지급
        current_min = heapq.heappop(self.heap)
        heapq.heappush(self.heap, current_min + amount)

    def get_sorted_balances(self):
        return sorted(self.heap)

def solve_v3():
    import sys
    tokens = sys.stdin.read().split()
    if not tokens: return
    
    n = int(tokens[0])
    manager = MoneyManager([int(x) for x in tokens[1:n+1]])
    
    m_idx = n + 1
    m = int(tokens[m_idx])
    for i in range(m_idx + 1, m_idx + 1 + m):
        manager.add_money(int(tokens[i]))
        
    print(*(manager.get_sorted_balances()))

solve_v3()

#########################################################################

import heapq
import sys

def input_gen():
    for line in sys.stdin:
        for word in line.split():
            yield int(word)

def solve_v4():
    gen = input_gen()
    try:
        n = next(gen)
        h = [next(gen) for _ in range(n)]
        heapq.heapify(h)
        
        m = next(gen)
        for _ in range(m):
            # heapreplace는 pop+push를 한 번에 수행하여 효율적입니다.
            heapq.heapreplace(h, h[0] + next(gen))
            
        h.sort()
        sys.stdout.write(" ".join(map(str, h)) + "\n")
    except StopIteration:
        pass

solve_v4()

#########################################################################

