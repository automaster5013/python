import sys

def solve():
    # 모든 입력을 공백 단위로 쪼개어 리스트로 만듭니다.
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return
    
    R = int(raw_data[0])
    C = int(raw_data[1])
    
    # 1. 보드 데이터만 정확히 추출 (가장 중요!)
    # 모든 문자열을 하나로 합친 뒤, R*C만큼만 슬라이싱하여 불필요한 데이터를 버립니다.
    board_data = "".join(raw_data[2:])[:R*C]
    
    # 2. 비트보드 생성 (안전하게 정수 변환)
    # 65를 빼는 대신 ord(char)가 65 이상인지 확인하는 방어 로직을 추가할 수도 있습니다.
    bit_board = []
    for r in range(R):
        row = []
        for c in range(C):
            char = board_data[r * C + c]
            row.append(1 << (ord(char) - 65))
        bit_board.append(row)

    # 상, 하, 좌, 우 방향 벡터
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 3. 중복 상태를 방지하는 Set 기반 BFS (Python 최적화)
    max_len = 0
    # (행, 열, 현재까지 획득한 알파벳 비트마스크, 현재 거리)
    start_bit = bit_board[0][0]
    q = set([(0, 0, start_bit, 1)])

    while q:
        r, c, mask, dist = q.pop()
        
        if dist > max_len:
            max_len = dist
        
        # 알파벳은 총 26개이므로 26에 도달하면 즉각 종료
        if max_len == 26:
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                char_bit = bit_board[nr][nc]
                # 비트 연산으로 이미 방문한 알파벳인지 체크 (O(1))
                if not (mask & char_bit):
                    q.add((nr, nc, mask | char_bit, dist + 1))

    print(max_len)

if __name__ == "__main__":
    solve()

##################################################################

