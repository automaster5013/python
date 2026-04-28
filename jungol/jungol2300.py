import sys

def solve():
    # 입력을 빠르게 읽어오기 위해 sys.stdin 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 입력이 이미 오름차순으로 정렬되어 있으므로 바로 리스트화
    liquids = list(map(int, input_data[1:]))

    left = 0
    right = n - 1
    
    # 초기 비교를 위한 아주 큰 값 설정
    min_abs_sum = float('inf')
    ans = (0, 0)

    while left < right:
        current_sum = liquids[left] + liquids[right]
        
        # 현재 합의 절댓값이 0에 더 가깝다면 갱신
        if abs(current_sum) < min_abs_sum:
            min_abs_sum = abs(current_sum)
            ans = (liquids[left], liquids[right])
            
            # 정확히 0이면 최적의 해이므로 즉시 탈출
            if current_sum == 0:
                break
        
        # 합의 부호에 따라 포인터 이동
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    # 오름차순으로 결과 출력
    print(f"{ans[0]} {ans[1]}")

if __name__ == "__main__":
    solve()

##############################################################