import sys

def solve():
    # 입력을 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    costs = []
    for i in range(n):
        costs.append(list(map(int, input_data[1 + i*n : 1 + (i+1)*n])))
        
    INF = 10**9
    # dp[mask]는 해당 장소들을 사용했을 때의 최소 비용
    dp = [INF] * (1 << n)
    # parent[mask]는 해당 mask 상태를 만들 때 마지막으로 선택한 장소 인덱스
    parent = [0] * (1 << n)
    
    # 비트 위치를 인덱스로 빠르게 변환하기 위한 테이블 (2^0 ~ 2^19)
    bit_to_idx = {1 << i: i for i in range(n)}
    
    # 각 마스크의 비트 개수(켜진 비트 수)를 미리 계산하거나 
    # 루프 내에서 효율적으로 관리합니다.
    bit_counts = [0] * (1 << n)
    for i in range(1, 1 << n):
        bit_counts[i] = bit_counts[i >> 1] + (i & 1)

    dp[0] = 0
    
    # 1부터 2^N - 1까지 순회하며 최적해를 찾습니다.
    for mask in range(1, 1 << n):
        k = bit_counts[mask] # 현재 배정하려는 건물의 번호 (1-based)
        cost_row = costs[k-1]
        
        temp_mask = mask
        while temp_mask:
            # 가장 낮은 위치의 켜진 비트를 가져옵니다.
            low_bit = temp_mask & -temp_mask
            j = bit_to_idx[low_bit] # 장소 인덱스
            
            # 이전 상태 (해당 장소를 배정하기 전)
            prev_mask = mask ^ low_bit
            
            # 최소 비용 갱신
            current_total = dp[prev_mask] + cost_row[j]
            if current_total < dp[mask]:
                dp[mask] = current_total
                parent[mask] = j
            
            # 처리한 비트 제거
            temp_mask ^= low_bit
            
    # 1. 최소 비용 출력
    final_mask = (1 << n) - 1
    print(dp[final_mask])
    
    # 2. 경로 역추적
    res = [0] * n
    curr = final_mask
    for i in range(n - 1, -1, -1):
        idx = parent[curr]
        res[i] = idx + 1
        curr ^= (1 << idx)
        
    print(*(res))

if __name__ == "__main__":
    solve()

############################################################

