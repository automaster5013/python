import sys
from bisect import bisect_left

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # 소의 요구사항 (맛 기준 내림차순)
    cows = []
    ptr = 2
    for _ in range(N):
        cows.append((int(input_data[ptr]), int(input_data[ptr+1])))
        ptr += 2
    cows.sort(key=lambda x: x[1], reverse=True)
    
    # 풀의 정보 (맛 기준 내림차순)
    grass = []
    for _ in range(M):
        grass.append((int(input_data[ptr]), int(input_data[ptr+1])))
        ptr += 2
    grass.sort(key=lambda x: x[1], reverse=True)
    
    # 가격 정보를 담을 리스트 (정렬 상태 유지)
    candidates = []
    total_cost = 0
    g_idx = 0
    
    for req_price, req_taste in cows:
        # 현재 소의 맛 조건을 만족하는 풀들을 모두 후보군에 추가
        while g_idx < M and grass[g_idx][1] >= req_taste:
            # 이분 탐색을 이용해 가격 순서대로 삽입 (정렬 유지)
            # 파이썬에서 list.insert는 O(N)이므로 데이터가 많을 경우 
            # 실제 대회에선 더 효율적인 SortedList 등을 고려해야 합니다.
            import bisect
            bisect.insort(candidates, grass[g_idx][0])
            g_idx += 1
            
        # 후보군 중 소의 가격 조건을 만족하는 가장 저렴한 풀 찾기
        idx = bisect_left(candidates, req_price)
        
        if idx < len(candidates):
            total_cost += candidates[idx]
            candidates.pop(idx) # 사용한 풀은 제거
        else:
            # 만족하는 풀이 없는 경우
            print("-1")
            return

    print(total_cost)

if __name__ == "__main__":
    solve()


