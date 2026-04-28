import sys

# 유클리드 호제법을 이용한 최대공약수 함수
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    g = int(input_data[0]) # 최대공약수
    l = int(input_data[1]) # 최소공배수
    
    # x * y = l / g 인 k를 구함
    k = l // g
    
    best_a, best_b = 0, 0
    
    # 두 수의 합을 최소로 만들기 위해 sqrt(k)부터 1까지 거꾸로 탐색
    # i는 x, k // i는 y가 됨
    for i in range(int(k**0.5), 0, -1):
        if k % i == 0:
            x = i
            y = k // i
            
            # x와 y가 서로소인지 확인 (중요!)
            if get_gcd(x, y) == 1:
                best_a = x * g
                best_b = y * g
                break # 가장 먼저 찾은 것이 차이가 가장 작으므로 즉시 종료
                
    # 작은 수부터 출력
    print(f"{best_a} {best_b}")

if __name__ == "__main__":
    solve()

############################################################################


