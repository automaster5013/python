import sys

def solve():
    # 입력 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    # 8x8 생산량 자료를 2차원 리스트로 변환
    grid = []
    for i in range(8):
        grid.append([int(x) for x in input_data[1 + i*8 : 1 + (i+1)*8]])
    
    # D[i][j] = P[i][j] - M 계산
    D = [[grid[i][j] - M for j in range(8)] for i in range(8)]
    
    # 행 합(row_sums), 열 합(col_sums), 전체 합(total_sum) 계산
    row_sums = [sum(row) for row in D]
    col_sums = [0] * 8
    for j in range(8):
        col_sums[j] = sum(D[i][j] for i in range(8))
    total_sum = sum(row_sums)
    
    # 위에서 유도한 공식 적용
    S = total_sum // 15
    R = [(rs - S) // 7 for rs in row_sums]
    C = [(cs - S) // 7 for cs in col_sums]
    
    # x[i][j] = R[i] + C[j] - D[i][j] 계산 및 출력
    for i in range(8):
        ans_row = []
        for j in range(8):
            x = R[i] + C[j] - D[i][j]
            if x == 1:
                ans_row.append('+')
            elif x == -1:
                ans_row.append('-')
            else:
                ans_row.append('.')
        print(" ".join(ans_row))

if __name__ == "__main__":
    solve()

##################################################################

