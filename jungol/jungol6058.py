import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    board = input_data[1:]
    
    # 열의 점유 상태를 확인하기 위한 배열
    col_used = [False] * n
    count = 0
    
    # 2. 백트래킹 함수 정의
    def backtrack(row):
        nonlocal count
        
        # 모든 행에 룩을 다 놓았다면 경우의 수 1 추가
        if row == n:
            count += 1
            return
        
        # 현재 행(row)에서 각 열(c)을 검사
        for c in range(n):
            # 1. 해당 열이 비어 있고
            # 2. 보드의 해당 칸이 장애물(#)이 아닐 때
            if not col_used[c] and board[row][c] == '.':
                # 룩 배치
                col_used[c] = True
                backtrack(row + 1)
                # 재귀 탈출 후 상태 복구 (Backtracking)
                col_used[c] = False

    # 3. 탐색 시작
    backtrack(0)
    print(count)

if __name__ == "__main__":
    solve()

##################################################################

