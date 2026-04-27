import sys

def solve():
    # 고속 입력
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x = list(map(int, input_data[1:]))

    # 최소 1장은 무조건 유지할 수 있음
    if n <= 2:
        # n이 2일 때는 무조건 공차를 만들 수 있으나, 
        # 두 수의 차이가 정수 공차를 만들 수 있는지 체크해야 함
        if n == 2:
            # 두 수의 차는 항상 1로 나누어지므로 0 출력
            print(0)
        else:
            print(0)
        return

    max_keep = 1
    
    # i번째 카드와 j번째 카드를 고정한다고 가정 (O(N^2))
    for i in range(n):
        counts = {}
        for j in range(n):
            if i == j:
                continue
            
            diff = x[j] - x[i]
            dist = j - i
            
            # 정수 공차가 발생하는 경우만 체크
            if diff % dist == 0:
                d = diff // dist
                counts[d] = counts.get(d, 0) + 1
        
        # 해당 i번째 카드를 기준으로 동일한 공차 d를 가진 카드들의 최대 개수 확인
        if counts:
            max_keep = max(max_keep, max(counts.values()) + 1)

    # 전체 개수 - 유지할 수 있는 최대 개수 = 최소 수정 횟수
    print(n - max_keep)

if __name__ == "__main__":
    solve()

#################################################################################

