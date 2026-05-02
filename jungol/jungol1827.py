import sys

def solve():
    # 1. 입력 처리 (sys.stdin.read를 사용하여 속도 최적화)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    # 던지지 않는 경우(0점)를 포함시킵니다.
    scores = [0] + [int(x) for x in input_data[2:]]

    # 2. 2발을 던져서 얻을 수 있는 모든 점수의 합을 계산
    # 중복을 제거하여 연산 횟수를 줄입니다.
    sums_of_2 = []
    for i in range(len(scores)):
        for j in range(i, len(scores)):
            s = scores[i] + scores[j]
            if s <= m:
                sums_of_2.append(s)
    
    # 정렬 및 중복 제거 (투 포인터 효율성을 위해)
    sums_of_2 = sorted(list(set(sums_of_2)))
    
    # 3. 투 포인터를 사용하여 x + y <= m 인 최대값 찾기
    max_score = 0
    left = 0
    right = len(sums_of_2) - 1
    
    while left <= right:
        current_sum = sums_of_2[left] + sums_of_2[right]
        if current_sum <= m:
            if current_sum > max_score:
                max_score = current_sum
            # 합을 더 키워보기 위해 왼쪽 포인터 이동
            left += 1
        else:
            # 합이 m을 초과하면 오른쪽 포인터를 줄여서 합을 낮춤
            right -= 1
            
    # 최종 결과 출력
    print(max_score)

if __name__ == "__main__":
    solve()

###################################################################



