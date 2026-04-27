import sys

def solve():
    # 고속 입력을 통해 N과 K, 그리고 온도 리스트를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    # 온도 리스트 (정수형 변환)
    temps = list(map(int, input_data[2:]))

    # 1. 초기 윈도우(첫 K일)의 합 계산
    current_sum = sum(temps[:k])
    max_sum = current_sum

    # 2. 슬라이딩 윈도우 시작
    # i는 새롭게 들어오는 날짜의 인덱스입니다.
    for i in range(k, n):
        # 윈도우의 가장 왼쪽 값(temps[i-k])을 빼고, 새로운 값(temps[i])을 더합니다.
        current_sum = current_sum - temps[i-k] + temps[i]
        
        # 최댓값 갱신
        if current_sum > max_sum:
            max_sum = current_sum

    # 결과 출력
    print(max_sum)

if __name__ == "__main__":
    solve()

##################################################################################

