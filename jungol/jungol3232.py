import sys

def solve():
    # 입력을 모두 읽어 공백 기준으로 분리합니다.
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
            
        # 첫 번째 박스 정보 (x1, y1, x2, y2)
        x1_1 = int(input_data[0])
        y1_1 = int(input_data[1])
        x2_1 = int(input_data[2])
        y2_1 = int(input_data[3])
        
        # 두 번째 박스 정보 (x1, y1, x2, y2)
        x1_2 = int(input_data[4])
        y1_2 = int(input_data[5])
        x2_2 = int(input_data[6])
        y2_2 = int(input_data[7])
        
        # x축 방향으로 겹치는 구간의 길이를 계산합니다.
        x_low = max(x1_1, x1_2)
        x_high = min(x2_1, x2_2)
        diff_x = x_high - x_low
        
        # y축 방향으로 겹치는 구간의 길이를 계산합니다.
        y_low = max(y1_1, y1_2)
        y_high = min(y2_1, y2_2)
        diff_y = y_high - y_low
        
        # 판별 로직
        if diff_x < 0 or diff_y < 0:
            print("NULL")
        elif diff_x > 0 and diff_y > 0:
            print("FACE")
        elif diff_x == 0 and diff_y == 0:
            print("POINT")
        else:
            # 한쪽은 겹치고(>0), 한쪽은 맞닿은(=0) 경우
            print("LINE")
            
    except EOFError:
        pass

if __name__ == "__main__":
    solve()

################################################################


