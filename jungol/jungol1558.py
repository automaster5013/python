import sys
from collections import deque

def solve():
    # 빠른 입력을 위해 전체 데이터를 읽어옵니다.
    raw = sys.stdin.read().split()
    if not raw: return
    
    K = int(raw[0])
    L1 = int(raw[1])
    S1 = raw[2]
    L2 = int(raw[3])
    S2 = raw[4]
    
    # 1. DP 계산: dp[i][j]는 (i, j)에서 시작하는 최장 K-부분서열 길이
    dp = [[0] * (L2 + 2) for _ in range(L1 + 2)]
    
    # row_max[i][j] = max(dp[i][j+1 : j+K+2])
    row_max = [[0] * (L2 + 2) for _ in range(L1 + 2)]
    
    # 각 열(column)의 슬라이딩 윈도우 최댓값을 관리할 데크들
    col_deques = [deque() for _ in range(L2 + 2)]

    # 역방향으로 DP 테이블을 채웁니다.
    for i in range(L1, 0, -1):
        # 현재 행 i에서 S1[i-1]과 매칭되는 S2의 j 위치들 탐색
        target_char = S1[i-1]
        
        # i+K+1행이 윈도우를 벗어났으므로 데크에서 제거 (Column-wise sliding window)
        out_i = i + K + 2
        if out_i <= L1:
            for j in range(1, L2 + 1):
                if col_deques[j] and col_deques[j][0][0] == out_i:
                    col_deques[j].popleft()

        # i+1행의 데이터를 각 열 데크에 추가
        in_i = i + 1
        if in_i <= L1:
            for j in range(1, L2 + 1):
                val = row_max[in_i][j]
                dq = col_deques[j]
                while dq and dq[-1][1] <= val:
                    dq.pop()
                dq.append((in_i, val))

        # dp[i][j] 결정
        for j in range(1, L2 + 1):
            if target_char == S2[j-1]:
                # g[i][j] = max(row_max[i+1...i+K+1][j])
                max_val = col_deques[j][0][1] if col_deques[j] else 0
                dp[i][j] = 1 + max_val

        # 현재 완성된 dp[i]를 바탕으로 row_max[i] 계산 (Row-wise sliding window)
        dq_row = deque()
        for j in range(L2, 0, -1):
            # j+K+1이 윈도우를 벗어나면 제거
            if dq_row and dq_row[0][0] == j + K + 2:
                dq_row.popleft()
            # j+1 위치의 dp[i] 값을 데크에 추가
            in_j = j + 1
            if in_j <= L2:
                val = dp[i][in_j]
                while dq_row and dq_row[-1][1] <= val:
                    dq_row.pop()
                dq_row.append((in_j, val))
            row_max[i][j] = dq_row[0][1] if dq_row else 0

    # 2. 최장 길이 탐색
    max_len = 0
    for i in range(1, L1 + 1):
        for j in range(1, L2 + 1):
            if dp[i][j] > max_len: max_len = dp[i][j]
    
    if max_len == 0:
        print("")
        return

    # 3. 비트셋을 활용한 사전식 복원
    # pos_bits[length][i] = dp[i][j] == length 인 j들의 비트셋
    pos_bits = [[0] * (L1 + 1) for _ in range(max_len + 1)]
    char_at = [[""] * (L2 + 1) for _ in range(L1 + 1)] # 좌표의 문자 저장
    
    for i in range(1, L1 + 1):
        for j in range(1, L2 + 1):
            l = dp[i][j]
            if l > 0:
                pos_bits[l][i] |= (1 << j)
                char_at[i][j] = S1[i-1]

    res = []
    # v_active[i] = 현재 가능한 경로의 마지막 인덱스 i에서의 j 비트셋
    v_active = [0] * (L1 + 1)
    
    # 첫 번째 문자 결정
    for char in "ACGT":
        found = False
        temp_active = [0] * (L1 + 1)
        for i in range(1, L1 + 1):
            if S1[i-1] == char:
                temp_active[i] = pos_bits[max_len][i]
                if temp_active[i]: found = True
        if found:
            res.append(char)
            v_active = temp_active
            break

    # 나머지 문자 결정
    for length in range(max_len - 1, 0, -1):
        for char in "ACGT":
            found = False
            temp_active = [0] * (L1 + 1)
            
            # 이전 활성 지점들로부터 거리 K 이내의 j 범위를 커버하는 비트 마스크
            for ni in range(1, L1 + 1):
                if S1[ni-1] != char or pos_bits[length][ni] == 0: continue
                
                # ni-K-1 <= i < ni 인 i들에 대해 v_active[i]의 j' 확인
                # j' < nj <= j'+K+1 인지 확인
                can_reach = False
                for pi in range(max(1, ni - K - 1), ni):
                    if v_active[pi]:
                        # pi 위치의 활성 j들에 대해 nj가 (j, j+K+1] 범위에 있는지 체크
                        # nj 기준으로는 (nj-K-1, nj) 범위에 pi의 j가 있어야 함
                        # pos_bits[length][ni]의 각 nj 비트에 대해 검사
                        target_j_bits = pos_bits[length][ni]
                        # 이 부분은 nj마다 도달 가능성을 비트로 한꺼번에 계산
                        # j_mask: 이전 j들의 영향을 받는 nj들의 집합
                        j_mask = 0
                        curr_v = v_active[pi]
                        # 1~K+1 비트 시프트하며 도달 가능한 영역 생성
                        for shift in range(1, K + 2):
                            j_mask |= (curr_v << shift)
                        
                        if j_mask & target_j_bits:
                            temp_active[ni] |= (j_mask & target_j_bits)
                            can_reach = True
                
                if can_reach: found = True
            
            if found:
                res.append(char)
                v_active = temp_active
                break
                
    print("".join(res))

solve()

###########################################################################################



