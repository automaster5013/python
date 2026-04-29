import sys

def solve():
    # 1. 입력 처리
    n = int(sys.stdin.readline())
    necklace = sys.stdin.readline().strip()
    
    # 원형 처리를 위해 문자열을 두 배로 늘림
    extended = necklace * 2
    max_beads = 0

    # 2. 모든 가능한 절단 지점을 순회 (i는 절단면의 오른쪽 인덱스)
    for i in range(n):
        # 오른쪽 방향으로 모으기
        right_count = 0
        right_color = 'w'
        for j in range(n):
            curr = extended[i + j]
            if right_color == 'w' and curr != 'w':
                right_color = curr
            
            if curr == 'w' or curr == right_color:
                right_count += 1
            else:
                break
        
        # 왼쪽 방향으로 모으기 (절단면 기준 왼쪽인 i-1부터 시작)
        left_count = 0
        left_color = 'w'
        for j in range(1, n + 1):
            # 탐색할 위치는 (i - j)인데, extended 상에서는 n + i - j
            curr = extended[n + i - j]
            if left_color == 'w' and curr != 'w':
                left_color = curr
                
            if curr == 'w' or curr == left_color:
                left_count += 1
            else:
                break
        
        # 3. 최대값 갱신 (양쪽에서 모은 알의 합은 n을 넘을 수 없음)
        total = min(n, right_count + left_count)
        if total > max_beads:
            max_beads = total

    print(max_beads)

if __name__ == "__main__":
    solve()

###########################################################################


