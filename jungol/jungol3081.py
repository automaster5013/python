import sys

def solve():
    # 모든 데이터를 한 번에 읽어들여 입출력(I/O) 속도 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    A = []
    idx = 1
    
    # 2차원 리스트 구성
    for i in range(N):
        A.append([int(x) for x in input_data[idx : idx+N]])
        idx += N
        
    # 초기 DP 테이블 생성 및 값 계산
    DP = [[0] * N for _ in range(N)]
    DP[0][0] = A[0][0]
    
    for j in range(1, N):
        DP[0][j] = DP[0][j-1] + A[0][j]
        
    for i in range(1, N):
        DP_i = DP[i]
        DP_prev = DP[i-1]
        A_i = A[i]
        
        DP_i[0] = DP_prev[0] + A_i[0]
        for j in range(1, N):
            v1 = DP_prev[j]
            v2 = DP_i[j-1]
            # 파이썬 내장 max() 대신 인라인 삼항 연산자를 사용하여 속도 최적화
            DP_i[j] = (v1 if v1 > v2 else v2) + A_i[j]
            
    # 첫 DP 테이블의 모든 값의 합 저장
    total_sum = sum(sum(row) for row in DP)
    out = [str(total_sum)]
    
    # 각 변화(Query) 명령 처리
    while idx < len(input_data):
        type_char = input_data[idx]
        r = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        
        # 'U'는 +1, 'D'는 -1
        diff = 1 if type_char == 'U' else -1
        A[r][c] += diff
        
        # 변경이 시작되는 첫 번째 행(r) 처리
        DP_r = DP[r]
        DP_r[c] += diff
        R = c
        
        if r == 0:
            # 0번 행은 위에서 내려오는 경로가 없으므로 무조건 끝까지 영향이 파급됨
            if diff == 1:
                for j in range(c + 1, N):
                    DP_r[j] += 1
            else:
                for j in range(c + 1, N):
                    DP_r[j] -= 1
            R = N - 1
        else:
            DP_prev = DP[r-1]
            A_r = A[r]
            for j in range(c + 1, N):
                v1 = DP_prev[j]
                v2 = DP_r[j-1]
                new_val = (v1 if v1 > v2 else v2) + A_r[j]
                if new_val != DP_r[j]:
                    DP_r[j] += diff
                    R = j
                else:
                    break
                    
        L = c
        total_sum += diff * (R - L + 1)
        
        # r+1 행부터 맨 끝 행까지 변화의 파동을 전달
        for i in range(r + 1, N):
            DP_i = DP[i]
            DP_prev = DP[i-1]
            A_i = A[i]
            
            L_i = -1
            
            # Step 1: 변화가 시작되는 지점 (L_i) 찾기
            for j in range(L, R + 1):
                if j == 0:
                    new_val = DP_prev[0] + A_i[0]
                else:
                    v1 = DP_prev[j]
                    v2 = DP_i[j-1]
                    new_val = (v1 if v1 > v2 else v2) + A_i[j]
                    
                if new_val != DP_i[j]:
                    L_i = j
                    break
            
            # 행에서 변화가 발견되지 않으면 하위 행들도 안전하므로 조기 종료
            if L_i == -1:
                break
                
            # Step 2: 수학적으로 확실히 변경됨이 보장된 구간은 연산 없이 일괄 처리
            if diff == 1:
                for j in range(L_i, R + 1):
                    DP_i[j] += 1
            else:
                for j in range(L_i, R + 1):
                    DP_i[j] -= 1
                    
            # Step 3: 구간의 끝 (R_i) 이 어디까지 연장되는지 추적
            R_i = R
            for j in range(R + 1, N):
                v1 = DP_prev[j]
                v2 = DP_i[j-1]
                new_val = (v1 if v1 > v2 else v2) + A_i[j]
                
                if new_val != DP_i[j]:
                    DP_i[j] += diff
                    R_i = j
                else:
                    break
                    
            # 변경된 영역의 크기만큼 총합을 갱신
            total_sum += diff * (R_i - L_i + 1)
            
            # 다음 행의 탐색을 위해 현재 구간 넘겨주기
            L = L_i
            R = R_i
            
        out.append(str(total_sum))
        
    # 결과 일괄 출력
    print('\n'.join(out))

if __name__ == '__main__':
    solve()

###################################################################################

