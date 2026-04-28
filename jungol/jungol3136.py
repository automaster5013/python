import sys

def solve():
    # 고속 입력 설정
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    
    # 1. 누적 합 배열 초기화 (인덱스 에러 방지를 위해 N+1 크기)
    # 2차원 리스트 생성 시 그램의 메모리는 충분하므로 안전합니다.
    prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 2. 누적 합 계산
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            val = int(input[ptr])
            ptr += 1
            # 2D Prefix Sum 공식 적용
            prefix_sum[i][j] = val + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
            
    q = int(input[ptr])
    ptr += 1
    
    results = []
    # 3. 쿼리 처리
    for _ in range(q):
        sr, sc, er, ec = map(int, input[ptr:ptr+4])
        ptr += 4
        
        # O(1) 구간 합 계산 공식
        res = prefix_sum[er][ec] - prefix_sum[sr-1][ec] - prefix_sum[er][sc-1] + prefix_sum[sr-1][sc-1]
        results.append(str(res))
        
    # 결과 일괄 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

############################################################################################################

