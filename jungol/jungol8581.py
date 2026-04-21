import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 1. 입력 처리
    N = int(input_data[0])
    # 두 수열을 각각 리스트로 변환
    A = list(map(int, input_data[1:N+1]))
    B = list(map(int, input_data[N+1:2*N+1]))
    
    # 2. 재배열 부등식에 따라 두 수열을 모두 오름차순 정렬
    A.sort()
    B.sort()
    
    # 3. 같은 인덱스끼리 곱하여 합산
    total_sum = 0
    for i in range(N):
        total_sum += A[i] * B[i]
        
    # 4. 결과 출력
    print(total_sum)

if __name__ == "__main__":
    solve()


