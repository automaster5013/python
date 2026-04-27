import sys

def solve():
    # 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    w = int(input_data[0]) # 격자 가로
    h = int(input_data[1]) # 격자 세로
    p = int(input_data[2]) # 초기 x
    q = int(input_data[3]) # 초기 y
    t = int(input_data[4]) # 경과 시간

    # X축 위치 계산
    # (p + t)를 2w로 나눈 나머지는 0 ~ 2w 사이의 값이 됨
    final_x = (p + t) % (2 * w)
    if final_x > w:
        final_x = 2 * w - final_x
        
    # Y축 위치 계산
    # (q + t)를 2h로 나눈 나머지는 0 ~ 2h 사이의 값이 됨
    final_y = (q + t) % (2 * h)
    if final_y > h:
        final_y = 2 * h - final_y

    # 결과 출력
    print(f"{final_x} {final_y}")

if __name__ == "__main__":
    solve()

###################################################################


