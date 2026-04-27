import sys
from bisect import bisect_left

def solve():
    # 고속 입력을 통해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    q_count = int(input_data[1])
    
    towns = []
    ptr = 2
    for _ in range(n):
        a = int(input_data[ptr])
        x = int(input_data[ptr+1])
        towns.append((x, a))
        ptr += 2
        
    # 1. 마을 위치 기준으로 정렬 (이진 탐색을 위해 필수)
    towns.sort()
    
    # 2. 누적 합 계산
    pref_a = [0] * (n + 1)   # 인원수 누적 합
    pref_ax = [0] * (n + 1)  # 위치 가중치(a * x) 누적 합
    
    for i in range(n):
        x, a = towns[i]
        pref_a[i+1] = pref_a[i] + a
        pref_ax[i+1] = pref_ax[i] + (a * x)
        
    # 정렬된 위치 리스트만 따로 추출 (bisect용)
    sorted_x = [t[0] for t in towns]
    
    # 3. 쿼리 처리
    results = []
    for _ in range(q_count):
        q = int(input_data[ptr])
        ptr += 1
        
        # q의 위치를 이진 탐색으로 찾음 (O(log N))
        idx = bisect_left(sorted_x, q)
        
        # 왼쪽 영역 (0 ~ idx-1)
        left_a = pref_a[idx]
        left_ax = pref_ax[idx]
        dist_l = q * left_a - left_ax
        
        # 오른쪽 영역 (idx ~ n-1)
        right_a = pref_a[n] - pref_a[idx]
        right_ax = pref_ax[n] - pref_ax[idx]
        dist_r = right_ax - q * right_a
        
        results.append(str(dist_l + dist_r))
        
    # 결과 일괄 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

#########################################################

