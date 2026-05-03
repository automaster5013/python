import sys
from collections import deque

def solve():
    # 입력 처리: 4x4 격자판을 1차원 튜플로 변환
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    start_state = tuple(map(int, input_data))
    target_state = tuple(range(1, 17))

    if start_state == target_state:
        print(0)
        return

    # 행/열 회전 함수
    def get_next_states(state):
        results = []
        # 행 이동 (1 i k): i번째 행을 오른쪽으로 k칸
        for i in range(4):
            row_idx = [i*4, i*4+1, i*4+2, i*4+3]
            row_vals = [state[x] for x in row_idx]
            for k in range(1, 4):
                shifted = row_vals[4-k:] + row_vals[:4-k]
                new_state = list(state)
                for idx, val in zip(row_idx, shifted):
                    new_state[idx] = val
                results.append((tuple(new_state), (1, i+1, k)))
        
        # 열 이동 (2 i k): i번째 열을 아래쪽으로 k칸
        for j in range(4):
            col_idx = [j, j+4, j+8, j+12]
            col_vals = [state[x] for x in col_idx]
            for k in range(1, 4):
                shifted = col_vals[4-k:] + col_vals[:4-k]
                new_state = list(state)
                for idx, val in zip(col_idx, shifted):
                    new_state[idx] = val
                results.append((tuple(new_state), (2, j+1, k)))
        return results

    # 역방향 이동의 반대 연산 (회전 거리를 복원)
    def invert_move(move):
        m_type, i, k = move
        return (m_type, i, 4 - k)

    # 양방향 BFS 초기 설정
    q_f = deque([start_state])
    visited_f = {start_state: []}
    
    q_b = deque([target_state])
    visited_b = {target_state: []}

    # 최대 7번 이동이므로 각 방향에서 3~4단계씩 탐색
    for _ in range(4):
        # 정방향 확장
        for _ in range(len(q_f)):
            curr = q_f.popleft()
            if curr in visited_b:
                print_path(visited_f[curr], visited_b[curr])
                return
            
            for nxt, move in get_next_states(curr):
                if nxt not in visited_f:
                    visited_f[nxt] = visited_f[curr] + [move]
                    q_f.append(nxt)
                    if nxt in visited_b:
                        print_path(visited_f[nxt], visited_b[nxt])
                        return

        # 역방향 확장
        for _ in range(len(q_b)):
            curr = q_b.popleft()
            if curr in visited_f:
                print_path(visited_f[curr], visited_b[curr])
                return
            
            for nxt, move in get_next_states(curr):
                if nxt not in visited_b:
                    visited_b[nxt] = visited_b[curr] + [move]
                    q_b.append(nxt)
                    if nxt in visited_f:
                        print_path(visited_f[nxt], visited_b[nxt])
                        return

def print_path(path_f, path_b):
    # 역방향 경로는 이동 방향을 반전시키고 순서를 뒤집어야 함
    full_path = path_f + [invert_move(m) for m in reversed(path_b)]
    print(len(full_path))
    for move in full_path:
        print(f"{move[0]} {move[1]} {move[2]}")

def invert_move(move):
    m_type, i, k = move
    return (m_type, i, 4 - k)

if __name__ == "__main__":
    solve()

##############################################################################

