import sys

def solve():
    # 입력을 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    y_sequence = list(map(int, input_data[1:]))
    
    # 결과 배열을 0으로 초기화 (0은 빈 칸을 의미)
    x_array = [0] * n
    curr_pos = 0
    
    for value in y_sequence:
        # 1. 현재 위치가 비어있지 않다면 빈 칸을 찾을 때까지 이동
        while x_array[curr_pos] != 0:
            curr_pos = (curr_pos + 1) % n
        
        # 2. 빈 칸에 현재 출력 값을 채워넣음
        x_array[curr_pos] = value
        
        # 3. 출력값만큼 점프하여 다음 위치 결정
        curr_pos = (value + curr_pos) % n
    
    # 결과 출력
    print(n)
    print(*(x_array))

if __name__ == "__main__":
    solve()

#################################################################

