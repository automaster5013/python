import sys

def solve():
    # 입력을 빠르게 읽어오기 위해 모든 토큰을 리스트로 만듭니다.
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    N = int(tokens[0]) # 프로그램 개수
    K = int(tokens[1]) # 최소 바이러스 길이
    
    progs = []
    idx = 2
    for _ in range(N):
        m = int(tokens[idx]) # 프로그램 길이
        idx += 1
        # 프로그램 코드를 정수 리스트로 저장
        progs.append([int(x) for x in tokens[idx : idx + m]])
        idx += m
    
    # 롤링 해시를 위한 파라미터 (Double Hashing)
    base = 10007 # 코드 값이 1~10,000이므로 10,000보다 큰 소수 선택
    m1 = 10**9 + 7
    m2 = 10**9 + 9
    pw1 = pow(base, K - 1, m1)
    pw2 = pow(base, K - 1, m2)
    
    def get_double_hashes(prog):
        """프로그램 내 모든 길이 K의 부분 코드(정/역방향)의 해시 집합 생성"""
        if len(prog) < K:
            return set()
        
        res = set()
        
        def add_to_set(arr):
            h1 = 0
            h2 = 0
            # 첫 윈도우 해시 계산
            for i in range(K):
                h1 = (h1 * base + arr[i]) % m1
                h2 = (h2 * base + arr[i]) % m2
            res.add((h1, h2))
            
            # 슬라이딩 윈도우로 나머지 해시 계산
            for i in range(K, len(arr)):
                h1 = (h1 - arr[i - K] * pw1) % m1
                h2 = (h2 - arr[i - K] * pw2) % m2
                h1 = (h1 * base + arr[i]) % m1
                h2 = (h2 * base + arr[i]) % m2
                res.add((h1, h2))
        
        add_to_set(prog)          # 정방향 부분 코드들 추가
        add_to_set(prog[::-1])    # 역방향 부분 코드들 추가
        return res

    # 첫 번째 프로그램의 가능한 바이러스 해시들을 기준으로 시작
    common_hashes = get_double_hashes(progs[0])
    
    # 나머지 모든 프로그램과 교집합 수행
    for i in range(1, N):
        if not common_hashes:
            break
        common_hashes &= get_double_hashes(progs[i])
            
    # 교집합이 존재하면 YES, 아니면 NO 출력
    if common_hashes:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()

##################################################################3


