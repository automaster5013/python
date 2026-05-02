import sys

# 나머지를 구할 기준값 (10^9 + 7)
MOD = 1000000007

def multiply(A, B):
    """2x2 행렬의 곱셈을 수행합니다."""
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def matrix_pow(A, n):
    """행렬 A의 n제곱을 분할 정복을 통해 구합니다."""
    res = [[1, 0], [0, 1]]  # 단위 행렬(Identity Matrix)
    while n > 0:
        if n % 2 == 1:
            res = multiply(res, A)
        A = multiply(A, A)
        n //= 2
    return res

def solve():
    # 모든 입력을 한꺼번에 읽어와 처리합니다.
    input_data = sys.stdin.read().split()
    
    for val in input_data:
        n = int(val)
        
        # n이 -1이면 입력을 중단합니다.
        if n == -1:
            break
        
        # n이 0일 경우 기저 사례 처리
        if n == 0:
            print(0)
            continue
        
        # 피보나치 변환 행렬
        T = [[1, 1], [1, 0]]
        
        # T^n 계산
        result_matrix = matrix_pow(T, n)
        
        # 행렬 공식에 따라 Fn은 결과 행렬의 [0][1] 또는 [1][0] 위치의 값입니다.
        print(result_matrix[0][1])

if __name__ == "__main__":
    solve()

################################################################################

