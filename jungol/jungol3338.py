import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(5000)

def M(L, R, k, memo):
    """
    구간 [L, R] 내의 수 i에 대하여 J(i)의 최댓값을 구하는 함수.
    k는 현재 고려하고 있는 가장 큰 코인 Sk = 2^k - 1의 인덱스.
    """
    if L > R:
        return -1
    if k == 1:
        # S1 = 1인 경우, J(i) = i이므로 구간 [L, R]에서의 최댓값은 R이다.
        return R
    
    # 메모이제이션 (L, R, k 상태 저장)
    state = (L, R, k)
    if state in memo:
        return memo[state]
    
    sk = (1 << k) - 1
    res = -1
    
    # 탐욕 알고리즘의 특성상, Sk 코인은 i // sk 번 사용된다.
    # Sk = 2^k - 1 이므로 Sk+1 = 2*Sk + 1이다.
    # 따라서 i // sk의 값(a)은 0, 1, 2 중 하나만 가능하다 (3*Sk > Sk+1 이기 때문).
    for a in range(3):
        # i가 Sk를 a번 포함하는 범위: [a * sk, (a + 1) * sk - 1]
        low = a * sk
        high = (a + 1) * sk - 1
        
        # 현재 탐색 구간 [L, R]과의 교집합 계산
        curr_L = max(L, low)
        curr_R = min(R, high)
        
        if curr_L <= curr_R:
            # a개의 Sk 코인을 사용하고 남은 금액에 대해 재귀 호출
            val = a * k + M(curr_L - low, curr_R - low, k - 1, memo)
            if val > res:
                res = val
    
    memo[state] = res
    return res

def solve():
    # 표준 입력으로부터 데이터를 읽어옴
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    ptr = 1
    output = []
    
    for _ in range(T):
        x = int(input_data[ptr])
        y = int(input_data[ptr+1])
        ptr += 2
        
        # 각 테스트 케이스마다 메모이제이션 딕셔너리 초기화
        memo = {}
        # 2^31 - 1 > 10^9 이므로 k=30부터 시작
        ans = M(x, y, 30, memo)
        output.append(str(ans))
    
    # 결과 출력
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

###############################################################

