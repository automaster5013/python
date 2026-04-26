import sys
import heapq

def solve():
    # 고속 입력을 위해 한 번에 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    P = int(input_data[1])
    # 메모리 절약을 위해 제너레이터나 리스트 슬라이싱 활용
    A = map(int, input_data[2:])
    
    selected_heap = [] # 선택된 허수아비들 (Min-Heap)
    pool_heap = []     # 대기 중인 허수아비들 (Max-Heap, 음수로 저장)
    current_sum = 0
    results = []

    for val in A:
        # 1. 일단 대기 풀에 넣음
        heapq.heappush(pool_heap, -val)
        
        # 2. 대기 풀에서 가장 큰 놈과 현재 선택된 가장 작은 놈을 교체하여 효율화
        if selected_heap and -pool_heap[0] > selected_heap[0]:
            top_in_pool = -heapq.heappop(pool_heap)
            bottom_in_selected = heapq.heappop(selected_heap)
            
            current_sum -= bottom_in_selected
            current_sum += top_in_pool
            
            heapq.heappush(selected_heap, top_in_pool)
            heapq.heappush(pool_heap, -bottom_in_selected)

        # 3. 합이 부족하면 대기 풀에서 가장 큰 놈들을 가져옴
        while current_sum < P and pool_heap:
            top_val = -heapq.heappop(pool_heap)
            current_sum += top_val
            heapq.heappush(selected_heap, top_val)
            
        # 4. 합이 넉넉하면 가장 작은 놈들을 빼서 개수를 최소화 (다이어트)
        while selected_heap and current_sum - selected_heap[0] >= P:
            removed_val = heapq.heappop(selected_heap)
            current_sum -= removed_val
            heapq.heappush(pool_heap, -removed_val)
            
        # 5. 결과 저장
        if current_sum >= P:
            results.append(str(len(selected_heap)))
        else:
            results.append("-1")
            
    # 결과를 한 번에 출력 (출력 병목 방지)
    sys.stdout.write(" ".join(results) + "\n")

if __name__ == "__main__":
    solve()

#################################################################################

