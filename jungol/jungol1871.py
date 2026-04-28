import sys

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 둘째 줄부터 하나씩 들어오는 아이들의 번호 리스트
    children = [int(x) for x in input_data[1:]]

    # dp[i]는 children[i]를 마지막 원소로 하는 LIS의 길이
    dp = [1] * n

    # LIS 구하기 (O(N^2))
    for i in range(n):
        for j in range(i):
            if children[j] < children[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 가장 긴 증가하는 부분 수열의 길이
    max_lis = max(dp) if dp else 0

    # 최소 이동 횟수 = 전체 인원 - LIS 길이
    print(n - max_lis)

if __name__ == "__main__":
    solve()

#########################################################################
