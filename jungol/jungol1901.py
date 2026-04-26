# 1. 1,000,000까지 소수 판별 배열 미리 생성 (전처리)
# 이 부분이 함수 밖(전역)에 있어야 solve_v1에서 참조할 수 있습니다.
LIMIT = 1000000
is_prime = [True] * (LIMIT + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(LIMIT**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, LIMIT + 1, i):
            is_prime[j] = False

def solve_v1():
    try:
        # 첫 번째 줄: 테스트 케이스 개수 N
        line1 = input().strip()
        if not line1:
            return
        n = int(line1)
        
        for _ in range(n):
            # 두 번째 줄부터: 처리할 숫자 M
            line_m = input().strip()
            if not line_m:
                continue
            m = int(line_m)
            
            d = 0
            while True:
                results = []
                # m-d가 2 이상이고 소수인지 확인 (작은 수 우선)
                if m - d >= 2 and is_prime[m - d]:
                    results.append(m - d)
                
                # m+d가 범위 내 소수인지 확인 (중복 방지 d > 0)
                if d > 0 and m + d <= LIMIT and is_prime[m + d]:
                    results.append(m + d)
                
                if results:
                    # 결과가 있으면 오름차순 출력 후 루프 종료
                    print(*(results))
                    break
                d += 1
    except (EOFError, ValueError):
        pass

# 프로그램 실행 시작점
if __name__ == "__main__":
    solve_v1()

################################################################################

def check_p(k):
    if k < 2: return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0: return False
    return True

def solve_v4():
    try:
        n = int(input().strip())
        for _ in range(n):
            m = int(input().strip())
            d = 0
            while True:
                res = []
                if m - d >= 2 and check_p(m - d):
                    res.append(m - d)
                if d > 0 and m + d <= 1000000 and check_p(m + d):
                    res.append(m + d)
                
                if res:
                    print(*(res))
                    break
                d += 1
    except: pass

solve_v4()

################################################################################

def is_val_prime(k):
    if k < 2: return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0: return False
    return True

def solve_v5():
    try:
        n = int(input())
        for _ in range(n):
            m = int(input())
            d = 0
            while True:
                ans = []
                # 작은 쪽 검사
                if m - d >= 2 and is_val_prime(m - d):
                    ans.append(m - d)
                # 큰 쪽 검사
                if d > 0 and m + d <= 1000000 and is_val_prime(m + d):
                    ans.append(m + d)
                
                if ans:
                    print(*(ans))
                    break
                d += 1
    except:
        pass

solve_v5()

################################################################################


