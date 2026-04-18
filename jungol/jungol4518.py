def solve():
    # 1. 입력 받기 (N: 공의 개수, K: 팀 수)
    line = input().split()
    if not line:
        return
    n = int(line[0])
    k = int(line[1])
    
    # 2. 1부터 K까지의 합 계산 (최소한 필요한 공의 개수)
    # 합 공식: K * (K + 1) // 2
    min_required = k * (k + 1) // 2
    
    # 3. 공이 부족한 경우 -1 출력
    if n < min_required:
        print(-1)
        return
    
    # 4. 남은 공의 개수 확인
    # 일단 1, 2, ..., K개를 담았다고 가정하고 남은 양을 구함
    remainder = n - min_required
    
    # 5. 차이 계산
    # 남은 공을 K개 바구니에 하나씩 골고루 나누어 줄 수 있다면 차이는 K-1
    # 나누어 주고 나머지가 생긴다면 (일부만 더 커지므로) 차이는 K
    if remainder % k == 0:
        print(k - 1)
    else:
        print(k)

# 함수 실행
solve()


