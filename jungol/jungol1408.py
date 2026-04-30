import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    lines = []
    
    idx = 1
    for _ in range(n):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        lines.append((a, b))
        idx += 2
        
    # 2. A 전봇대 번호 기준으로 오름차순 정렬
    lines.sort()
    
    # 3. B 전봇대 번호만 추출
    b_targets = [line[1] for line in lines]
    
    # 4. LIS(최장 증가 부분 수열) 길이 구하기
    # dp[i]는 i번째 전깃줄을 마지막으로 포함했을 때 가질 수 있는 최대 전깃줄 수
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if b_targets[j] < b_targets[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    # 5. 최대 남길 수 있는 개수 찾기
    max_kept = max(dp)
    
    # 6. 최소 제거 개수 = 전체 개수 - 최대 남길 수 있는 개수
    print(n - max_kept)

if __name__ == "__main__":
    solve()

##############################################################################

