import sys

def solve():
    # 1. 입력 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0]) # 식탁의 길이
    k = int(input_data[1]) # 선택 가능 거리
    # 문자열을 리스트로 변환 (수정 가능하도록)
    table = list(input_data[2])
    
    count = 0
    
    # 2. 식탁을 처음부터 끝까지 탐색
    for i in range(n):
        # 만약 현재 위치가 사람(P)이라면
        if table[i] == 'P':
            # 3. 자신이 먹을 수 있는 범위 [i-k, i+k] 내에서 
            # 가장 왼쪽에 있는 햄버거(H)를 찾는다.
            start = max(0, i - k)
            end = min(n - 1, i + k)
            
            for j in range(start, end + 1):
                if table[j] == 'H':
                    # 햄버거를 찾으면 먹었다는 표시(X)를 하고 카운트 증가
                    table[j] = 'X'
                    count += 1
                    # 한 명당 하나만 먹으므로 안쪽 루프 탈출
                    break
                    
    # 4. 결과 출력
    print(count)

if __name__ == "__main__":
    solve()

#########################################################################

