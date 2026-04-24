import sys

# 희소 테이블을 위한 로그 상수를 설정합니다 (2^18 > 250,000)
LOG = 19 

def solve():
    # 모든 입력을 한 번에 읽어 처리 속도를 높입니다.
    try:
        data = sys.stdin.read().split()
    except EOFError:
        return
    if not data:
        return
    
    N = int(data[0])
    Q = int(data[1])
    
    # 1-indexed를 유지하기 위해 앞에 0을 추가합니다.
    A = [0] * (N + 1)
    for i in range(1, N + 1):
        A[i] = int(data[i + 1])
        
    # D[i]: A[i]가 A[i-1]보다 크거나 같아지기 위해 필요한 최소 2의 지수 차이
    D = [0] * (N + 1)
    for i in range(2, N + 1):
        a_p, a_c = A[i-1], A[i]
        if a_p <= a_c:
            # A[i]가 더 큰 경우, 지수를 얼마나 줄일 수 있는지 계산
            D[i] = -((a_c // a_p).bit_length() - 1)
        else:
            # A[i]가 더 작은 경우, 지수를 얼마나 늘려야 하는지 계산
            D[i] = ((a_p - 1) // a_c).bit_length()
    
    # 상대적 지수 차이의 누적합
    prefD = [0] * (N + 1)
    for i in range(2, N + 1):
        prefD[i] = prefD[i-1] + D[i]
        
    # prefD의 구간 합을 구하기 위한 누적합
    sum_prefD = [0] * (N + 1)
    for i in range(1, N + 1):
        sum_prefD[i] = sum_prefD[i-1] + prefD[i]
        
    # Next Smaller Value (NSV): 자신보다 작은 값이 처음 나타나는 위치
    R = [N + 1] * (N + 1)
    stack = []
    for i in range(1, N + 1):
        p_val = prefD[i]
        while stack and prefD[stack[-1]] > p_val:
            R[stack.pop()] = i
        stack.append(i)
        
    # 희소 테이블 초기화 (점프 위치 및 누적 최솟값 합)
    up = [[N + 1] * (N + 2) for _ in range(LOG)]
    cost = [[0] * (N + 2) for _ in range(LOG)]
    
    for i in range(1, N + 1):
        r_idx = R[i]
        up[0][i] = r_idx
        cost[0][i] = (r_idx - i) * prefD[i]
        
    # 희소 테이블 채우기 (2^k 점프)
    for k in range(1, LOG):
        u_prev, c_prev = up[k-1], cost[k-1]
        u_curr, c_curr = up[k], cost[k]
        for i in range(1, N + 1):
            mid = u_prev[i]
            u_curr[i] = u_prev[mid]
            c_curr[i] = c_prev[i] + c_prev[mid]
            
    # 쿼리 처리
    query_idx = N + 2
    results = []
    for _ in range(Q):
        l = int(data[query_idx])
        r = int(data[query_idx + 1])
        query_idx += 2
        
        if l == r:
            results.append("0")
            continue
        
        # 전체 합 - (구간별 최솟값의 합)
        total_p = sum_prefD[r] - sum_prefD[l-1]
        
        curr, total_m = l, 0
        for k in range(LOG - 1, -1, -1):
            if up[k][curr] <= r + 1:
                total_m += cost[k][curr]
                curr = up[k][curr]
        
        if curr <= r:
            total_m += (r - curr + 1) * prefD[curr]
            
        results.append(str(total_p - total_m))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

