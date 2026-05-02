import sys
from bisect import bisect_left

def solve():
    # 입출력 속도 향상을 위한 설정
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    N = int(input[ptr]); ptr += 1
    Q = int(input[ptr]); ptr += 1
    
    # 정렬된 데이터 읽기
    A = [int(input[ptr + i]) for i in range(N)]
    ptr += N
    
    results = []
    
    # Q개의 질의 처리
    for _ in range(Q):
        query = int(input[ptr]); ptr += 1
        
        # 이분 탐색으로 질의값이 들어갈 위치 찾기
        idx = bisect_left(A, query)
        
        if idx == 0:
            # 질의값이 모든 데이터보다 작거나 같을 때
            results.append(str(A[0]))
        elif idx == N:
            # 질의값이 모든 데이터보다 클 때
            results.append(str(A[N-1]))
        else:
            # 주변의 두 값 중 더 가까운 값 찾기
            left_val = A[idx-1]
            right_val = A[idx]
            
            # 차이가 같으면 작은 수(left_val)를 선택해야 하므로 <= 사용
            if abs(query - left_val) <= abs(right_val - query):
                results.append(str(left_val))
            else:
                results.append(str(right_val))
                
    # 결과 한꺼번에 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

#########################################################################


