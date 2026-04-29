import sys

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    papers = []
    
    idx = 1
    for _ in range(n):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        # 규격화: 항상 (큰 값, 작은 값) 순서로 저장
        papers.append((max(a, b), min(a, b)))
        idx += 2
        
    # 2. 가로 기준 내림차순, 가로가 같다면 세로 기준 내림차순 정렬
    papers.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    # 3. DP 배열 초기화 (모든 색종이는 자기 자신만으로 최소 1장)
    dp = [1] * n
    
    # 4. LIS(최대 부분 수열) 로직 적용
    for i in range(1, n):
        for j in range(i):
            # j번째 색종이 위에 i번째 색종이를 올릴 수 있는지 확인
            # 정렬 덕분에 papers[i][0] <= papers[j][0]은 어느 정도 보장됨
            if papers[i][0] <= papers[j][0] and papers[i][1] <= papers[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    # 5. 결과 출력
    print(max(dp))

if __name__ == "__main__":
    solve()

################################################################################

