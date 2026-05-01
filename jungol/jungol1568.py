import sys

sys.setrecursionlimit(10**6)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    if n == 0:
        print(0)
        return

    events = []
    y_coords = set()
    
    idx = 1
    for _ in range(n):
        x1 = int(input_data[idx])
        x2 = int(input_data[idx+1])
        y1 = int(input_data[idx+2])
        y2 = int(input_data[idx+3])
        idx += 4
        
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
        y_coords.add(y1)
        y_coords.add(y2)

    events.sort()
    
    sorted_ys = sorted(list(y_coords))
    y_map = {val: i for i, val in enumerate(sorted_ys)}
    num_ys = len(sorted_ys)
    
    tree_cnt = [0] * (num_ys * 4)
    tree_len = [0] * (num_ys * 4)

    def update(node, start, end, l, r, val):
        if r <= sorted_ys[start] or l >= sorted_ys[end]:
            return
        
        if l <= sorted_ys[start] and sorted_ys[end] <= r:
            tree_cnt[node] += val
        else:
            mid = (start + end) // 2
            update(node * 2, start, mid, l, r, val)
            update(node * 2 + 1, mid, end, l, r, val)
        
        if tree_cnt[node] > 0:
            tree_len[node] = sorted_ys[end] - sorted_ys[start]
        else:
            if end - start > 1:
                tree_len[node] = tree_len[node * 2] + tree_len[node * 2 + 1]
            else:
                tree_len[node] = 0

    total_area = 0
    prev_x = events[0][0]
    
    for x, type_val, y1, y2 in events:
        total_area += (x - prev_x) * tree_len[1]
        
        update(1, 0, num_ys - 1, y1, y2, type_val)
        prev_x = x
        
    print(total_area)

if __name__ == "__main__":
    solve()

###############################################################################


