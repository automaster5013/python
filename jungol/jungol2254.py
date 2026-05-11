import sys
from bisect import bisect_left, bisect_right

def solve():
    # 빠른 입출력 처리를 위해 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    M = int(input_data[1])
    
    A = [int(x) for x in input_data[2:2+N]]
    B = [int(x) for x in input_data[2+N:2+N+M]]
    
    # 누적 합(Prefix Sum) 계산
    PA = [0] * (N + 1)
    for i in range(N):
        PA[i+1] = PA[i] + A[i]
        
    PB = [0] * (M + 1)
    for i in range(M):
        PB[i+1] = PB[i] + B[i]
        
    # 전체 무게의 차이
    Delta = PA[N] - PB[M]
    
    # 1. 첫 번째 자르는 지점 (A1, B1) - 가장 앞쪽 인덱스(min)만 저장
    Best1 = {}
    for i in range(1, N - 1): # i는 A1의 크기 (최소 1, 뒤에 2단원 남아야 하므로 N-2까지)
        target_min = PA[i] - 50
        target_max = PA[i] + 50
        
        # 이분 탐색으로 유효한 B1의 크기 j의 범위를 찾음
        j_start = bisect_left(PB, target_min)
        j_end = bisect_right(PB, target_max)
        
        for j in range(max(1, j_start), min(M - 1, j_end)):
            X1 = PA[i] - PB[j]
            if -50 <= X1 <= 50:
                # 앞에서부터 순회하므로 처음 등장하는 i, j가 자동으로 최솟값이 됨
                if X1 not in Best1:
                    Best1[X1] = (i, j)
                    
    # 2. 두 번째 자르는 지점 (A2, B2 끝) - 가장 뒤쪽 인덱스(max)만 저장
    Best2 = {}
    for i in range(N - 1, 1, -1): # i는 A1+A2의 크기 (뒤에서부터 순회)
        target_min = PA[i] - Delta - 50
        target_max = PA[i] - Delta + 50
        
        j_start = bisect_left(PB, target_min)
        j_end = bisect_right(PB, target_max)
        
        for j in range(max(2, j_start), min(M, j_end)):
            X2 = PA[i] - PB[j]
            if Delta - 50 <= X2 <= Delta + 50:
                # 뒤에서부터 순회하므로 처음 등장하는 i, j가 자동으로 최댓값이 됨
                if X2 not in Best2:
                    Best2[X2] = (i, j)
                    
    # 3. 저장된 최적의 후보들끼리만 묶어서 최소 줄다리기 값 찾기
    min_diff = float('inf')
    best_ans = None
    
    for X1, (i1, j1) in Best1.items():
        for X2, (i2, j2) in Best2.items():
            # 첫 번째 자른 지점이 두 번째 자른 지점보다 앞서야 하고, 두 번째 그룹의 무게 차이도 50 이하여야 함
            if i1 < i2 and j1 < j2 and abs(X2 - X1) <= 50:
                # 세 그룹 무게 차이의 최댓값
                diff = max(abs(X1), abs(X2 - X1), abs(Delta - X2))
                if diff < min_diff:
                    min_diff = diff
                    best_ans = (i1, i2, j1, j2)
                    
    # 4. 정답 출력
    if best_ans is None:
        print("-1") # 불가능한 경우
    else:
        i1, i2, j1, j2 = best_ans
        # 단위 줄의 사람 수를 계산하여 출력
        print(f"{i1} {i2 - i1} {N - i2}")
        print(f"{j1} {j2 - j1} {M - j2}")

if __name__ == '__main__':
    solve()

################################################################################################################



