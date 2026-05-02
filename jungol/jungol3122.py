import sys

def solve():
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return
    
    n = int(raw_data[0])
    if n < 2:
        print(0)
        return
        
    segs = []
    ptr = 1
    for _ in range(n):
        x1 = int(raw_data[ptr]); ptr += 1
        y1 = int(raw_data[ptr]); ptr += 1
        x2 = int(raw_data[ptr]); ptr += 1
        y2 = int(raw_data[ptr]); ptr += 1
        
        min_x, max_x = (x1, x2) if x1 < x2 else (x2, x1)
        min_y, max_y = (y1, y2) if y1 < y2 else (y2, y1)
        
        segs.append((min_x, max_x, min_y, max_y, x1, y1, x2, y2))
        
    segs.sort()
    
    min_xs = [s[0] for s in segs]
    max_xs = [s[1] for s in segs]
    min_ys = [s[2] for s in segs]
    max_ys = [s[3] for s in segs]
    x1s = [s[4] for s in segs]
    y1s = [s[5] for s in segs]
    x2s = [s[6] for s in segs]
    y2s = [s[7] for s in segs]
    
    ans = 0
    for i in range(n):
        c_max_x = max_xs[i]
        c_min_y = min_ys[i]
        c_max_y = max_ys[i]
        c_x1, c_y1 = x1s[i], y1s[i]
        c_x2, c_y2 = x2s[i], y2s[i]
        
        dx1 = c_x2 - c_x1
        dy1 = c_y2 - c_y1
        
        for j in range(i + 1, n):
            if min_xs[j] > c_max_x:
                break
                
            if c_max_y < min_ys[j] or max_ys[j] < c_min_y:
                continue
            
            tx1, ty1 = x1s[j], y1s[j]
            tx2, ty2 = x2s[j], y2s[j]
            
            cp1 = dx1 * (ty1 - c_y1) - dy1 * (tx1 - c_x1)
            cp2 = dx1 * (ty2 - c_y1) - dy1 * (tx2 - c_x1)
            
            if cp1 * cp2 > 0:
                continue
                
            tdx = tx2 - tx1
            tdy = ty2 - ty1
            cp3 = tdx * (c_y1 - ty1) - tdy * (c_x1 - tx1)
            cp4 = tdx * (c_y2 - ty1) - tdy * (c_x2 - tx1)
            
            if cp3 * cp4 <= 0:
                ans += 1
                
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()

#################################################################

