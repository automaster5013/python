import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    rects = []
    xs = set()
    ys = set()
    
    idx = 1
    for _ in range(n):
        x1 = float(input_data[idx])
        y1 = float(input_data[idx+1])
        w = float(input_data[idx+2])
        h = float(input_data[idx+3])
        x2 = x1 + w
        y2 = y1 + h
        rects.append((x1, y1, x2, y2))
        xs.add(x1); xs.add(x2)
        ys.add(y1); ys.add(y2)
        idx += 4
        
    sorted_xs = sorted(list(xs))
    sorted_ys = sorted(list(ys))
    
    total_area = 0.0
    
    for i in range(len(sorted_xs) - 1):
        width = sorted_xs[i+1] - sorted_xs[i]
        for j in range(len(sorted_ys) - 1):
            height = sorted_ys[j+1] - sorted_ys[j]
            mid_x = sorted_xs[i] + width / 2.0
            mid_y = sorted_ys[j] + height / 2.0
            
            for rx1, ry1, rx2, ry2 in rects:
                if rx1 <= mid_x <= rx2 and ry1 <= mid_y <= ry2:
                    total_area += width * height
                    break
    
    # [수정된 출력 로직]
    # 1. 먼저 소수점 셋째 자리에서 반올림하여 둘째 자리까지 만듭니다.
    total_area = round(total_area, 2)
    
    # 2. 정수인지 확인하여 분기 처리합니다.
    if total_area == int(total_area):
        print(int(total_area))
    else:
        # 소수점이 있는 경우, 무조건 ".2f"를 사용하여 0을 포함한 2자리까지 출력합니다.
        print("{:.2f}".format(total_area))

if __name__ == "__main__":
    solve()

#####################################################################################


