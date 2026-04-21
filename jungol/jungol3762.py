import heapq
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])
    
    cows = []
    ptr = 3
    for i in range(N):
        p = int(input_data[ptr])
        c = int(input_data[ptr+1])
        cows.append((p, c, i))
        ptr += 2
        
    # 1. 쿠폰 가격(C) 기준으로 정렬하여 가장 싼 K마리를 먼저 구매 시도
    cows.sort(key=lambda x: x[1])
    
    used = [False] * N
    total_cost = 0
    count = 0
    
    # 우선 가장 저렴한 C를 가진 K마리 구매
    for i in range(min(K, N)):
        if total_cost + cows[i][1] <= M:
            total_cost += cows[i][1]
            used[i] = True
            count += 1
        else:
            print(count)
            return

    if count < K: # 예산 부족으로 K마리도 못 산 경우
        print(count)
        return

    # 2. 남은 소들을 위한 힙 구성
    # q_c: 안 산 소들의 쿠폰 가격 (index 포함)
    # q_p: 안 산 소들이 제값 가격 (index 포함)
    # q_diff: 이미 쿠폰 써서 산 소들의 (P - C) 값
    q_c = []
    q_p = []
    q_diff = []
    
    for i in range(N):
        if used[i]:
            heapq.heappush(q_diff, cows[i][0] - cows[i][1])
        else:
            heapq.heappush(q_c, (cows[i][1], i))
            heapq.heappush(q_p, (cows[i][0], i))
            
    # 3. 추가 구매 시도
    while count < N:
        # 이미 처리된(산) 소는 힙에서 제거
        while q_c and used[q_c[0][1]]: heapq.heappop(q_c)
        while q_p and used[q_p[0][1]]: heapq.heappop(q_p)
        
        if not q_c: break
        
        # 방법 A: 그냥 생돈 내고 사기 (P_i)
        cost_a = q_p[0][0]
        
        # 방법 B: 쿠폰 돌려막기 (C_i + (P_j - C_j))
        cost_b = q_c[0][0] + q_diff[0]
        
        if cost_a <= cost_b:
            if total_cost + cost_a <= M:
                total_cost += cost_a
                used[q_p[0][1]] = True
                heapq.heappop(q_p)
                count += 1
            else: break
        else:
            if total_cost + cost_b <= M:
                total_cost += cost_b
                used[q_c[0][1]] = True
                # 쿠폰을 돌려막았으므로, 새로 산 소의 (P-C)를 q_diff에 추가
                idx = q_c[0][1]
                heapq.heappop(q_c)
                heapq.heappop(q_diff)
                heapq.heappush(q_diff, cows[idx][0] - cows[idx][1])
                count += 1
            else: break
            
    print(count)

solve()

