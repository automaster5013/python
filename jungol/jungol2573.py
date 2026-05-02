import sys
from bisect import bisect_right

def solve():
    # 1. sys.stdin.readline을 사용하여 한 줄씩 읽어 메모리 점유를 최소화합니다.
    input = sys.stdin.readline
    
    line = input().split()
    if not line:
        return
    n = int(line[0])

    # 2. 동물 번호는 버리고 (L, R) 쌍만 리스트에 담습니다.
    # 튜플은 리스트보다 메모리를 적게 사용합니다.
    intervals = []
    for _ in range(n):
        data = input().split()
        if not data:
            break
        # 데이터가 (번호, L, R) 순서이므로 1번, 2번 인덱스를 가져옵니다.
        l, r = int(data[1]), int(data[2])
        intervals.append((l, r))
    
    # 3. 정렬: L(오름차순), R(내림차순)
    # 정렬을 먼저 하면 나중에 순차적으로 돌며 중복을 쉽게 제거할 수 있습니다.
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    # 4. 중복된 (L, R) 구간 제거 및 R 값 추출
    # 문제에서 동일한 구간은 상위 관계가 될 수 없으므로 중복은 하나만 남깁니다.
    if not intervals:
        print(0)
        return

    unique_r = []
    if intervals:
        unique_r.append(-intervals[0][1]) # 비증가 수열을 찾기 위해 -R로 저장
        
    for i in range(1, len(intervals)):
        # 이전 구간과 다를 때만 추가 (중복 제거)
        if intervals[i] != intervals[i-1]:
            unique_r.append(-intervals[i][1])
    
    # 메모리 절약을 위해 정렬된 리스트는 삭제합니다.
    del intervals

    # 5. 최장 비감소 부분 수열(Longest Non-Decreasing Subsequence) 계산
    # R1 >= R2 >= R3... 관계는 -R1 <= -R2 <= -R3... 관계와 같습니다.
    # O(N log N) 알고리즘
    tails = []
    for x in unique_r:
        # 비감소(값이 같아도 됨)를 찾아야 하므로 bisect_right를 사용합니다.
        idx = bisect_right(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
            
    # 최종 결과 출력
    print(len(tails))

if __name__ == "__main__":
    solve()

##############################################################################

