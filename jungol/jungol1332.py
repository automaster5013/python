import sys

def solve():
    # 입력 속도 최적화를 위해 sys.stdin.read() 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    for s in input_data:
        n = len(s)
        # 1. 실패 함수 (pi 배열) 계산
        pi = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pi[j-1]
            if s[i] == s[j]:
                j += 1
                pi[i] = j
        
        # 2. 접두어와 접미어가 동시에 되는 길이 역추적
        results = []
        curr = pi[n-1]
        while curr > 0:
            results.append(curr)
            # 이전 단계의 일치하는 접두어 길이로 점프
            curr = pi[curr-1]
        
        # 전체 길이 N도 접두어이자 접미어이므로 추가
        results.append(n)
        
        # 3. 오름차순 정렬 후 출력
        results.sort()
        print(*(results))

if __name__ == "__main__":
    solve()

###############################################################


