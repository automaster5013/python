import sys
import heapq

def solve():
    # 고속 입력을 위해 전체 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 널빤지 길이들을 리스트에 담습니다.
    planks = [int(x) for x in input_data[1:]]
    
    # 1. 리스트를 최소 힙 구조로 변환합니다. (O(N))
    heapq.heapify(planks)
    
    total_cost = 0
    
    # 2. 널빤지가 하나로 합쳐질 때까지 반복 (O(N log N))
    while len(planks) > 1:
        # 가장 짧은 두 널빤지를 꺼냅니다.
        first = heapq.heappop(planks)
        second = heapq.heappop(planks)
        
        # 두 개를 합치는 비용 계산
        current_merge_cost = first + second
        total_cost += current_merge_cost
        
        # 합쳐진 널빤지를 다시 힙에 넣습니다.
        heapq.heappush(planks, current_merge_cost)
        
    # 3. 최소 비용 출력
    print(total_cost)

if __name__ == "__main__":
    solve()

##################################################################

