import sys

def solve():
    # 대량의 입력을 빠르게 처리하기 위해 전체 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    points = []
    
    # 좌표 데이터를 (x, y) 튜플 리스트로 변환
    for i in range(n):
        x = int(input_data[2 * i + 1])
        y = int(input_data[2 * i + 2])
        points.append((x, y))
        
    # 신발끈 공식 적용
    area_sum = 0
    for i in range(n):
        x_curr, y_curr = points[i]
        # 마지막 점인 경우 첫 번째 점과 연결
        x_next, y_next = points[(i + 1) % n]
        
        area_sum += (x_curr * y_next) - (x_next * y_curr)
        
    # 절대값을 취하고 2로 나누어 실제 면적 계산
    final_area = abs(area_sum) / 2.0
    
    # 소수 둘째 자리에서 반올림하여 첫째 자리까지 출력
    print(f"{final_area:.1f}")

if __name__ == "__main__":
    solve()

#################################################################


