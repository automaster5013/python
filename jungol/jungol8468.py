import sys
from collections import deque

def solve():
    # 데이터 입력
    input = sys.stdin.read().split()
    if not input: return
    
    N = int(input[0])
    K = int(input[1])
    A = list(map(int, input[2:]))
    
    # 최댓값과 최솟값의 인덱스를 저장할 데크
    max_dq = deque()
    min_dq = deque()
    
    left = 0
    max_len = 0
    
    for right in range(N):
        # 최댓값 데크 업데이트 (새로 들어온 값보다 작은 기존 값들은 제거)
        while max_dq and A[max_dq[-1]] <= A[right]:
            max_dq.pop()
        max_dq.append(right)
        
        # 최솟값 데크 업데이트 (새로 들어온 값보다 큰 기존 값들은 제거)
        while min_dq and A[min_dq[-1]] >= A[right]:
            min_dq.pop()
        min_dq.append(right)
        
        # 최댓값 - 최솟값이 K를 초과하는 동안 left 이동
        while A[max_dq[0]] - A[min_dq[0]] > K:
            left += 1
            # 데크에 남아있는 인덱스가 윈도우 범위를 벗어나면 제거
            if max_dq[0] < left:
                max_dq.popleft()
            if min_dq[0] < left:
                min_dq.popleft()
        
        # 현재 가능한 최대 길이 갱신
        max_len = max(max_len, right - left + 1)
    
    print(max_len)

if __name__ == "__main__":
    solve()

