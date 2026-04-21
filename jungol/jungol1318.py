def solve():
    import sys
    
    # 1. 1,500번째까지의 못생긴 수 미리 계산 (DP)
    ugly = [0] * 1501
    ugly[1] = 1
    
    p2 = p3 = p5 = 1
    
    for i in range(2, 1501):
        # 각 포인터가 가리키는 값에 2, 3, 5를 곱한 값 중 최소값 선택
        next2 = ugly[p2] * 2
        next3 = ugly[p3] * 3
        next5 = ugly[p5] * 5
        
        res = min(next2, next3, next5)
        ugly[i] = res
        
        # 선택된 값과 일치하는 포인터 전진 (중복 제거를 위해 if-if-if 사용)
        if res == next2: p2 += 1
        if res == next3: p3 += 1
        if res == next5: p5 += 1

    # 2. 여러 개의 쿼리 처리
    input_data = sys.stdin.read().split()
    for n_str in input_data:
        n = int(n_str)
        if n == 0:
            break
        print(ugly[n])

if __name__ == "__main__":
    solve()

