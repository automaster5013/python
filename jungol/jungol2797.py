import sys

def solve():
    # 고속 입력을 통해 D1, D2를 읽어옵니다.
    try:
        line = sys.stdin.read().split()
        if not line:
            return
        d1, d2 = map(int, line)
    except ValueError:
        return

    def get_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    used_seats_count = 0

    # D1부터 D2까지 각 원을 탐색
    for d in range(d1, d2 + 1):
        for k in range(d):
            # k/d를 기약분수 a/b로 나타냈을 때의 분모 b 계산
            common = get_gcd(k, d)
            b = d // common
            
            # [d1, d-1] 범위 내에 b의 배수가 있는지 확인
            # b의 배수 중 d1 이상인 가장 작은 값 계산
            first_multiple = ((d1 + b - 1) // b) * b
            
            # 그 최소 배수가 현재 반지름 d보다 같거나 크다면, 
            # 공연 범위 내에서 가로막는 좌석이 없다는 뜻입니다.
            if first_multiple >= d:
                used_seats_count += 1

    print(used_seats_count)

if __name__ == "__main__":
    solve()

########################################################################

