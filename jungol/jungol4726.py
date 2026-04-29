import sys

def solve():
    input = sys.stdin.read().split()
    if not input: return
    
    n = int(input[0])
    honey = list(map(int, input[1:]))
    
    # 누적 합 배열 생성
    s = [0] * n
    s[0] = honey[0]
    for i in range(1, n):
        s[i] = s[i-1] + honey[i]
        
    ans = 0
    
    # 시나리오 1: 벌(0) - 벌(i) - 벌통(n-1)
    for i in range(1, n-1):
        # (전체 - 0번 - i번) + (전체 - i번까지 누적합)
        total = (s[n-1] - honey[0] - honey[i]) + (s[n-1] - s[i])
        if total > ans: ans = total
        
    # 시나리오 2: 벌통(0) - 벌(i) - 벌(n-1)
    for i in range(1, n-1):
        # (n-2번까지 누적합 - i번) + (i-1번까지 누적합)
        total = (s[n-2] - honey[i]) + s[i-1]
        if total > ans: ans = total
        
    # 시나리오 3: 벌(0) - 벌통(i) - 벌(n-1)
    for i in range(1, n-1):
        # 전체 - 양끝 + 벌통위치꿀 (벌통위치 꿀은 양쪽 벌이 모두 먹음)
        total = s[n-1] - honey[0] - honey[n-1] + honey[i]
        if total > ans: ans = total
        
    print(ans)

if __name__ == "__main__":
    solve()

########################################################################



