import sys
from collections import Counter

def solve():
    # 데이터 읽기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    cards = [int(x) for x in input_data[2:]]

    # 1. 반으로 나누기
    left_cards = cards[:n//2]
    right_cards = cards[n//2:]

    # 2. 왼쪽 그룹의 모든 부분 합 구하기 (Counter 활용)
    left_sums = Counter([0])
    for card in left_cards:
        new_sums = Counter()
        for s, count in left_sums.items():
            new_sums[s + card] += count
        left_sums.update(new_sums)

    # 3. 오른쪽 그룹의 모든 부분 합을 구하며 결과 계산
    right_sums = Counter([0])
    for card in right_cards:
        new_sums = Counter()
        for s, count in right_sums.items():
            new_sums[s + card] += count
        right_sums.update(new_sums)

    ans = 0
    # left_sums와 right_sums를 조합하여 M이 되는 경우 찾기
    for s_right, count_right in right_sums.items():
        target = m - s_right
        if target in left_sums:
            ans += count_right * left_sums[target]

    # 4. 공집합 제외 (M이 0일 때, 아무것도 안 뽑은 경우 1가지를 뺌)
    if m == 0:
        ans -= 1

    print(ans)

if __name__ == "__main__":
    solve()

########################################################################

