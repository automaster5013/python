import sys

def solve():
    # 표준 입력을 통해 데이터를 읽어옴
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    # 각 행에서 0이 아닌 숫자만 추출하여 시퀀스 생성
    A = [int(x) for x in input_data[1:N+1] if int(x) != 0]
    B = [int(x) for x in input_data[N+1:2*N+1] if int(x) != 0]
    
    n1, n2 = len(A), len(B)
    INF = 10**15
    
    # m번의 매칭을 위한 DP 테이블 초기화
    # prev_f[i][j]: m-1번 매칭했을 때의 최대값
    prev_f = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    # 최소 매칭 수 조건: m >= n1 + n2 - N
    m_min = n1 + n2 - N
    max_ans = -INF
    if m_min <= 0:
        max_ans = 0 # 매칭을 전혀 하지 않아도 되는 경우 0으로 시작
        
    # 매칭 수 m을 1부터 순차적으로 증가시키며 탐색
    for m in range(1, min(n1, n2) + 1):
        curr_f = [[-INF] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(m, n1 + 1):
            a_val = A[i-1]
            cf_i = curr_f[i]
            cf_prev_i = curr_f[i-1]
            pf_prev_i = prev_f[i-1]
            
            for j in range(m, n2 + 1):
                # 점화식: (i, j 매칭) vs (i 건너뛰기) vs (j 건너뛰기)
                match_val = pf_prev_i[j-1] + a_val * B[j-1]
                skip_a = cf_prev_i[j]
                skip_b = cf_i[j-1]
                
                # 최적의 값 선택
                res = match_val
                if skip_a > res: res = skip_a
                if skip_b > res: res = skip_b
                cf_i[j] = res
        
        # 조건(N개 열 이내)을 만족하는 m에 대해 결과 갱신
        if m >= m_min:
            if curr_f[n1][n2] > max_ans:
                max_ans = curr_f[n1][n2]
        
        # 현재 테이블을 다음 m의 계산을 위한 이전 테이블로 교체
        prev_f = curr_f
        
    print(int(max_ans))

if __name__ == '__main__':
    solve()

#######################################################################

