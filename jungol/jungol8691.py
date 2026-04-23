import sys

def solve():
    # 1. 입력 처리 (sys.stdin.read를 사용하여 대량의 데이터를 빠르게 읽음)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))

    # 2. X 구하기 (연속 중복 제거)
    if n == 0:
        x = 0
    else:
        x = 1 # 첫 번째 원소는 무조건 포함
        for i in range(1, n):
            # 현재 원소가 이전 원소와 다를 때만 카운트 증가
            if a[i] != a[i-1]:
                x += 1

    # 3. Y 구하기 (전체 중복 제거 - 서로 다른 값의 개수)
    # 파이썬의 set은 해시 테이블 기반으로 중복을 제거함
    y = len(set(a))

    # 4. 결과 출력
    print(f"{x} {y}")

if __name__ == "__main__":
    solve()

