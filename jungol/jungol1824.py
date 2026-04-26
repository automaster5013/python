import sys

def solve():
    # 데이터를 읽어와 2차원 배열로 저장
    input_data = sys.stdin.read().split()
    if not input_data: return
    board = [list(map(int, input_data[i*9 : (i+1)*9])) for i in range(9)]

    # 비트마스크: 각 행, 열, 박스에 사용된 숫자를 9비트로 관리
    # 1 << n 은 n번 숫자가 사용됨을 의미
    row_bits = [0] * 9
    col_bits = [0] * 9
    box_bits = [0] * 9

    def get_box_idx(r, c):
        return (r // 3) * 3 + (c // 3)

    # 초기 보드 상태를 비트마스크에 기록
    empty_cells = []
    for r in range(9):
        for c in range(9):
            if board[r][c] != 0:
                num_bit = 1 << (board[r][c] - 1)
                row_bits[r] |= num_bit
                col_bits[c] |= num_bit
                box_bits[get_box_idx(r, c)] |= num_bit
            else:
                empty_cells.append((r, c))

    def get_possibilities(r, c):
        # 해당 칸에 들어갈 수 있는 숫자들을 비트로 반환
        # (row | col | box)를 통해 사용된 전체 비트를 구하고, 
        # 이를 반전(~)시킨 후 9비트(0x1FF)만 취함
        used = row_bits[r] | col_bits[c] | box_bits[get_box_idx(r, c)]
        return 0x1FF & ~used

    def backtrack():
        # 1. MRV 휴리스틱: 후보 숫자가 가장 적은 빈 칸을 찾음
        min_options = 10
        best_cell = None
        best_bits = 0
        best_idx = -1

        for i, (r, c) in enumerate(empty_cells):
            bits = get_possibilities(r, c)
            # 비트의 개수(후보 숫자의 수)를 셈
            count = bin(bits).count('1')
            
            # 후보가 하나도 없으면 이 경로는 실패
            if count == 0: return False
            
            if count < min_options:
                min_options = count
                best_cell = (r, c)
                best_bits = bits
                best_idx = i
                if count == 1: break # 후보가 1개면 바로 선택

        # 빈 칸이 없으면 완성!
        if not best_cell: return True

        r, c = best_cell
        # 탐색 효율을 위해 확인한 칸은 리스트에서 잠시 제거
        empty_cells.pop(best_idx)

        # 2. 가능한 숫자 대입 (비트 순회)
        for num in range(1, 10):
            if best_bits & (1 << (num - 1)):
                # 비트 셋
                num_bit = 1 << (num - 1)
                board[r][c] = num
                row_bits[r] |= num_bit
                col_bits[c] |= num_bit
                box_bits[get_box_idx(r, c)] |= num_bit

                if backtrack(): return True

                # 백트래킹 (원상복구)
                row_bits[r] &= ~num_bit
                col_bits[c] &= ~num_bit
                box_bits[get_box_idx(r, c)] &= ~num_bit
                board[r][c] = 0

        # 리스트 복구
        empty_cells.insert(best_idx, (r, c))
        return False

    if backtrack():
        for row in board:
            print(*(row))

if __name__ == "__main__":
    solve()

#############################################################

