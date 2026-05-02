import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    C = int(input_data[ptr]); ptr += 1
    N = int(input_data[ptr]); ptr += 1
    B = [int(input_data[ptr + i]) for i in range(N)]; ptr += N
    P = [int(input_data[ptr + i]) for i in range(C + 1)]
    
    S_total = sum(B)
    P0, PC = P[0], P[C]
    diff_P = PC - P0
    
    # 부분 집합의 주스 합 전처리 (O(2^N))
    sums = [0] * (1 << N)
    for i, val in enumerate(B):
        bit = 1 << i
        for mask in range(bit):
            sums[bit | mask] = sums[mask] + val
            
    # 각 부분 집합이 하나의 그룹일 때의 점수 h[mask] 계산
    h = [0] * (1 << N)
    for mask in range(1, 1 << N):
        r = sums[mask] % C
        if r != 0:
            h[mask] = C * (P[r] - P0) - r * diff_P
            
    # 동적 계획법 (O(3^N))
    dp = [0] * (1 << N)
    for mask in range(1, 1 << N):
        lb = mask & -mask # 마스크의 가장 낮은 비트 추출
        rest = mask ^ lb
        
        # 현재 마스크 전체를 하나의 그룹으로 보는 경우
        best = h[mask]
        
        # lb를 포함하는 모든 부분 집합(comp)을 순회
        sub = rest
        while sub:
            comp = sub | lb
            cand = h[comp] + dp[mask ^ comp]
            if cand > best:
                best = cand
            sub = (sub - 1) & rest
            
        # lb만 별개의 그룹으로 있는 경우 처리
        cand = h[lb] + dp[rest]
        if cand > best:
            best = cand
            
        dp[mask] = best
        
    # 최종 가치 계산 공식
    const_term = N * P0 * C + diff_P * S_total
    final_val = (const_term + dp[(1 << N) - 1]) // C
    
    sys.stdout.write(str(final_val) + '\n')

if __name__ == "__main__":
    solve()

############################################################

