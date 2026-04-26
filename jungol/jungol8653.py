import sys

def solve():
    # 대량의 데이터를 빠르게 읽어오기 위한 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    # 높이 배열 생성 (0 ~ 10^18 범위를 고려한 정수 리스트)
    H = [int(x) for x in input_data[2:2+N]]
    queries = [int(x) for x in input_data[2+N:]]
    
    # 1. 꼭대기 인덱스 찾기 (O(log N))
    low, high = 0, N - 1
    while low < high:
        mid = (low + high) // 2
        if H[mid] < H[mid + 1]:
            low = mid + 1
        else:
            high = mid
    peak_idx = low
    peak_val = H[peak_idx]
    
    results = []
    
    # 2. 질문 처리 (Q * log N)
    for x in queries:
        if x == peak_val:
            results.append("T")
            continue
            
        found = False
        
        # 왼쪽 증가 구간 탐색
        l, r = 0, peak_idx - 1
        while l <= r:
            mid = (l + r) // 2
            if H[mid] == x:
                results.append("L")
                found = True
                break
            elif H[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        if found: continue
        
        # 오른쪽 감소 구간 탐색
        l, r = peak_idx + 1, N - 1
        while l <= r:
            mid = (l + r) // 2
            if H[mid] == x:
                results.append("R")
                found = True
                break
            elif H[mid] > x: # 감소 구간이므로 x보다 크면 오른쪽으로
                l = mid + 1
            else:
                r = mid - 1
        if found: continue
        
        # 어느 구간에도 존재하지 않는 경우
        results.append("N")
    
    # 결과 출력 최적화
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

##########################################################################

