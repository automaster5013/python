import sys

def solve():
    # 1. 입력 처리
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())

    # 2. DP를 이용한 최소 이동 횟수 및 최적 k값 계산
    # dp[i]: 4개 기둥에서 i개 원판을 옮기는 최소 횟수
    dp = [0] * (n + 1)
    best_k = [0] * (n + 1)
    
    # 3개 기둥 하노이 이동 횟수: 2^n - 1
    def hanoi3_count(num):
        return (2 ** num) - 1

    for i in range(1, n + 1):
        min_moves = float('inf')
        for k in range(0, i):
            # Frame-Stewart 점화식: 2 * T(k, 4) + T(n-k, 3)
            moves = 2 * dp[k] + hanoi3_count(i - k)
            if moves <= min_moves:
                min_moves = moves
                best_k[i] = k
        dp[i] = int(min_moves)

    # 3. 이동 과정 출력 함수
    # 3개 기둥 하노이 과정
    def hanoi3(num, start, mid, end, disk_offset):
        if num == 0:
            return
        hanoi3(num - 1, start, end, mid, disk_offset)
        print(f"{num + disk_offset} : {start}->{end}")
        hanoi3(num - 1, mid, start, end, disk_offset)

    # 4개 기둥 하노이 과정
    def hanoi4(num, start, mid1, mid2, end, disk_offset):
        if num == 0:
            return
        if num == 1:
            print(f"{1 + disk_offset} : {start}->{end}")
            return
        
        k = best_k[num]
        # Step 1: k개를 보조 기둥(mid1)으로 이동 (4기둥 활용)
        hanoi4(k, start, mid2, end, mid1, disk_offset)
        # Step 2: n-k개를 목적 기둥(end)으로 이동 (3기둥 활용, mid1 제외)
        hanoi3(num - k, start, mid2, end, disk_offset + k)
        # Step 3: k개를 목적 기둥(end)으로 이동 (4기둥 활용)
        hanoi4(k, mid1, start, mid2, end, disk_offset)

    # 결과 출력
    print(dp[n])
    hanoi4(n, 'A', 'B', 'C', 'D', 0)

if __name__ == "__main__":
    solve()

########################################################################


