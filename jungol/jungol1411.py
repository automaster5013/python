import sys

def solve():
    # 1. 입력 처리
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)
    
    # 2. 예외 처리 (n이 1일 때)
    if n == 1:
        print(1)
        return
    
    # 3. DP 테이블 초기화
    # f[i]: 세로 i칸까지 채우는 방법의 수
    f = [0] * (n + 1)
    mod = 20100529
    
    # 4. 초기값 설정
    f[1] = 1
    f[2] = 3
    
    # 5. 점화식을 이용한 반복문 진행
    for i in range(3, n + 1):
        # f(i) = f(i-1) + 2 * f(i-2)
        f[i] = (f[i-1] + 2 * f[i-2]) % mod
        
    # 6. 결과 출력
    print(f[n])

if __name__ == "__main__":
    solve()

###################################################

