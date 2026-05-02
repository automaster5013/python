import sys

def solve():
    # 입력을 빠르게 읽어옵니다.
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    dice = []
    idx = 1
    for _ in range(n):
        dice.append(list(map(int, input[idx:idx+6])))
        idx += 6

    # 마주보는 면의 인덱스 매핑 (A-F, B-D, C-E)
    # 0-5, 1-3, 2-4
    opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
    
    max_total_sum = 0
    
    # 첫 번째 주사위의 아랫면 숫자를 1~6까지 하나씩 시도
    for start_val in range(1, 7):
        current_sum = 0
        # 현재 층의 아랫면 숫자를 결정
        bottom_val = start_val
        
        for i in range(n):
            current_die = dice[i]
            # 현재 주사위에서 아랫면 숫자의 인덱스를 찾음
            b_idx = current_die.index(bottom_val)
            # 마주보는 윗면의 인덱스를 찾음
            t_idx = opposite[b_idx]
            top_val = current_die[t_idx]
            
            # 옆면 중 최댓값 찾기 (6, 5, 4 순서로 검사)
            max_side = 0
            for side_candidate in range(6, 3, -1):
                if side_candidate != bottom_val and side_candidate != top_val:
                    max_side = side_candidate
                    break
            
            current_sum += max_side
            # 다음 주사위의 아랫면은 현재 주사위의 윗면과 같아야 함
            bottom_val = top_val
            
        # 6가지 시작 경우 중 최대합 갱신
        if current_sum > max_total_sum:
            max_total_sum = current_sum
            
    print(max_total_sum)

if __name__ == "__main__":
    solve()

###############################################################################

