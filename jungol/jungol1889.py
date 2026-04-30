import sys

def solve():
    # 1. 입력 처리
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)
    
    # 결과값을 저장할 변수
    count = 0
    
    # 2. 비트마스크 백트래킹 함수
    # col: 열 점유 상태
    # diag1: / 방향 대각선 점유 상태 (row + col)
    # diag2: \ 방향 대각선 점유 상태 (row - col)
    def backtrack(row, col, diag1, diag2):
        nonlocal count
        
        # 모든 행에 퀸을 다 놓았다면 성공!
        if row == n:
            count += 1
            return
        
        # 현재 행에서 퀸을 놓을 수 있는 자리를 비트로 계산
        # (1 << n) - 1 은 n개의 비트가 모두 1인 상태
        # ~(col | diag1 | diag2) 는 퀸을 놓을 수 있는 빈 자리들을 1로 만듦
        available_positions = ((1 << n) - 1) & ~(col | diag1 | diag2)
        
        while available_positions:
            # 가장 오른쪽에 있는 1(비트)을 선택 (퀸을 놓을 자리)
            pos = available_positions & -available_positions
            
            # 다음 행으로 이동
            # diag1과 diag2는 행이 바뀔 때마다 비트를 한 칸씩 밀어줌
            backtrack(row + 1, 
                      col | pos, 
                      (diag1 | pos) << 1, 
                      (diag2 | pos) >> 1)
            
            # 선택한 자리를 지우고 다음 가능성 탐색
            available_positions &= ~pos

    # 3. 탐색 시작
    backtrack(0, 0, 0, 0)
    print(count)

if __name__ == "__main__":
    solve()

###############################################################################

