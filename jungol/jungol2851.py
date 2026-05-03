import sys
from collections import deque

def solve():
    # 1. 입력 처리: 3x3 입력을 하나의 문자열로 변환
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    start_state = "".join(input_data)
    target_state = "12345678X"

    if start_state == target_state:
        print(0)
        return

    # 2. BFS 초기 설정
    # visited[현재상태] = (이전상태, 옮겨진 타일 번호)
    queue = deque([start_state])
    visited = {start_state: (None, None)}

    # 상하좌우 이동을 위한 인덱스 변화 (3x3 격자 기준)
    # 인덱스: 0 1 2 / 3 4 5 / 6 7 8
    def get_next_states(state):
        idx = state.find('X')
        r, c = divmod(idx, 3)
        moves = []
        
        # 상, 하, 좌, 우 방향 탐색
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                n_idx = nr * 3 + nc
                # 타일 스왑
                state_list = list(state)
                moved_tile = state_list[n_idx] # 빈 공간으로 들어올 타일 번호
                state_list[idx], state_list[n_idx] = state_list[n_idx], state_list[idx]
                moves.append(("".join(state_list), moved_tile))
        return moves

    # 3. 탐색 시작
    found = False
    while queue:
        curr = queue.popleft()
        
        if curr == target_state:
            found = True
            break
            
        for nxt, tile in get_next_states(curr):
            if nxt not in visited:
                visited[nxt] = (curr, tile)
                queue.append(nxt)

    # 4. 결과 출력 및 경로 역추적
    if found:
        path = []
        curr = target_state
        while visited[curr][0] is not None:
            prev, tile = visited[curr]
            path.append(tile)
            curr = prev
        
        # 역추적이므로 뒤집기
        path.reverse()
        print(len(path))
        print(*(path))

if __name__ == "__main__":
    solve()

############################################################################################



