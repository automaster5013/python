import sys

def solve():
    # 입력 데이터를 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 첫 번째 입력은 행렬의 크기 N입니다.
    n = int(input_data[0])
    matrix = []
    ptr = 1
    
    # N x N 행렬 원소를 읽어옵니다.
    for _ in range(n):
        # 계산 편의를 위해 미리 10000으로 나머지를 취해 저장합니다.
        matrix.append([int(x) % 10000 for x in input_data[ptr : ptr + n]])
        ptr += n
    
    # dp[mask]는 선택된 열의 집합(mask)에 대한 순열 곱의 합을 저장합니다.
    # mask의 비트 개수는 현재까지 처리한 행의 개수를 의미합니다.
    dp = [0] * (1 << n)
    dp[0] = 1
    
    # 비트 개수(처리한 행의 개수)에 따라 마스크를 그룹화하여 효율적으로 처리합니다.
    masks_by_bits = [[] for _ in range(n + 1)]
    for mask in range(1 << n):
        masks_by_bits[bin(mask).count('1')].append(mask)
    
    # 각 행(r)에 대해 가능한 마스크 상태를 탐색하며 DP 테이블을 채웁니다.
    for r in range(n):
        row_data = matrix[r]
        # 현재 r개의 행이 처리된 마스크들에 대해서만 전이 수행
        for mask in masks_by_bits[r]:
            current_val = dp[mask]
            if current_val == 0:
                continue
            
            # 아직 사용되지 않은 열(c)을 현재 행(r)에 배정합니다.
            for c in range(n):
                if not (mask & (1 << c)):
                    nxt_mask = mask | (1 << c)
                    # 합의 마지막 4자리만 필요하므로 매번 10000으로 나머지를 구합니다.
                    dp[nxt_mask] = (dp[nxt_mask] + current_val * row_data[c]) % 10000
                    
    # 모든 행과 열이 매칭된 최종 상태의 값을 출력합니다.
    print(dp[(1 << n) - 1])

if __name__ == "__main__":
    solve()

#########################################################################################


