import sys

def solve():
    # 1. 입력 받기
    try:
        W = int(sys.stdin.readline())
        # 500, 100, 50, 10, 5, 1원 순서
        counts = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return

    denoms = [500, 100, 50, 10, 5, 1]
    
    # 2. 전체 금액 계산
    total_sum = sum(d * c for d, c in zip(denoms, counts))
    
    # 3. 남겨야 할 금액 계산
    change = total_sum - W
    
    # 4. 남길 금액(change)을 최소한의 동전 개수로 구성 (역 그리디)
    removed = [0] * 6
    for i in range(6):
        # 해당 액수의 동전을 최대한 많이 사용하되, 
        # 내가 가진 개수(counts[i])와 남은 금액(change)을 넘지 않도록 함
        num = min(counts[i], change // denoms[i])
        removed[i] = num
        change -= num * denoms[i]
        
    # 5. 실제로 지불에 사용된 동전 개수 구하기 (전체 - 남긴 것)
    used = [c - r for c, r in zip(counts, removed)]
    
    # 6. 결과 출력
    print(sum(used))
    print(*(used))

if __name__ == "__main__":
    solve()

################################################################################


