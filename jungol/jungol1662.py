import sys

def solve():
    # 고속 입력을 위해 전체 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 체스판 정보 (1: 놓을 수 있음, 0: 없음)
    board = []
    for i in range(n):
        board.append(list(map(int, input_data[1 + i*n : 1 + (i+1)*n])))

    # 두 가지 대각선 방향의 사용 여부를 체크하는 배열
    # r + c 의 범위: 0 ~ 2n-2
    # r - c + n 의 범위: 1 ~ 2n-1
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)

    # 흰색 칸 그룹과 검은색 칸 그룹으로 좌표를 나눔
    # (r + c) % 2 == 0 이면 흰색, 1이면 검은색 (기준은 상대적임)
    white_cells = []
    black_cells = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                if (r + c) % 2 == 0:
                    white_cells.append((r, c))
                else:
                    black_cells.append((r, c))

    def backtrack(cells, index, count):
        nonlocal max_temp
        # 현재까지 찾은 최대값 갱신
        if count > max_temp:
            max_temp = count
        
        # 모든 후보 칸을 다 확인했으면 종료
        if index == len(cells):
            return
        
        # 가지치기: 남은 칸을 다 채워도 현재 최대값보다 작으면 탐색 중단
        if count + (len(cells) - index) <= max_temp:
            return

        r, c = cells[index]
        
        # 1. 현재 칸에 비숍을 놓는 경우 (대각선 간섭이 없을 때)
        if not diag1[r + c] and not diag2[r - c + n]:
            diag1[r + c] = True
            diag2[r - c + n] = True
            backtrack(cells, index + 1, count + 1)
            # 상태 복구 (Backtrack)
            diag1[r + c] = False
            diag2[r - c + n] = False
            
        # 2. 현재 칸에 비숍을 놓지 않고 다음 칸으로 넘어가는 경우
        backtrack(cells, index + 1, count)

    # 흰색 칸들에서 최대 개수 구하기
    max_temp = 0
    backtrack(white_cells, 0, 0)
    result_white = max_temp

    # 검은색 칸들에서 최대 개수 구하기 (대각선 배열 초기화는 자동임)
    max_temp = 0
    backtrack(black_cells, 0, 0)
    result_black = max_temp

    # 최종 결과 출력
    print(result_white + result_black)

if __name__ == "__main__":
    # 재귀 깊이 제한 설정 (N=10이므로 기본값으로도 충분함)
    sys.setrecursionlimit(2000)
    solve()

#####################################################################


