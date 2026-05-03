import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a, b, c, d = map(int, input_data)

    if not (c == 0 or c == a or d == 0 or d == b):
        print("-1")
        return

    queue = deque([(0, 0, 0)])
    visited = set()
    visited.add((0, 0))

    while queue:
        wa, wb, dist = queue.popleft()

        if wa == c and wb == d:
            print(dist)
            return

        move_ab = min(wa, b - wb)
        move_ba = min(wb, a - wa)

        next_states = [
            (a, wb),                
            (wa, b),                
            (0, wb),                
            (wa, 0),                
            (wa - move_ab, wb + move_ab), 
            (wa + move_ba, wb - move_ba)  
        ]

        for nwa, nwb in next_states:
            if (nwa, nwb) not in visited:
                visited.add((nwa, nwb))
                queue.append((nwa, nwb, dist + 1))

    print("-1")

if __name__ == "__main__":
    solve()

############################################################



