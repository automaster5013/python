import sys
import heapq

def solve():
    # 고속 입력을 위해 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    buildings = []
    coords = []
    
    ptr = 1
    for _ in range(N):
        a = int(input_data[ptr])
        b = int(input_data[ptr+1])
        h = int(input_data[ptr+2])
        buildings.append((a, b, h))
        coords.append(a)
        coords.append(b)
        ptr += 3
        
    # 1. 좌표 압축: 모든 시작점과 끝점을 정렬하여 유일한 경계값들을 얻습니다.
    unique_x = sorted(list(set(coords)))
    
    # 2. 빌딩을 시작 위치(A) 기준으로 정렬합니다.
    buildings.sort()
    
    # 3. 스위핑 알고리즘 수행
    max_heap = [] # (-높이, 끝나는 위치) 저장
    total_area = 0
    b_idx = 0 # 처리할 빌딩의 인덱스
    
    # 압축된 좌표로 만들어지는 각 구간을 탐색합니다.
    for i in range(len(unique_x) - 1):
        curr_x = unique_x[i]
        next_x = unique_x[i+1]
        
        # 현재 위치(curr_x)에서 시작하는 모든 빌딩을 힙에 추가합니다.
        while b_idx < N and buildings[b_idx][0] <= curr_x:
            a, b, h = buildings[b_idx]
            heapq.heappush(max_heap, (-h, b))
            b_idx += 1
        
        # 현재 위치(curr_x) 이전에 이미 끝난 빌딩들을 힙에서 제거합니다 (Lazy Removal).
        while max_heap and max_heap[0][1] <= curr_x:
            heapq.heappop(max_heap)
            
        # 힙의 최상단에 있는 빌딩이 현재 구간의 최대 높이입니다.
        if max_heap:
            max_h = -max_heap[0][0]
            # (구간의 너비) * (최대 높이)를 더해줍니다.
            total_area += (next_x - curr_x) * max_h
            
    # 최종 넓이 출력
    print(total_area)

if __name__ == "__main__":
    solve()

#######################################################################################


