import sys
from collections import deque

def solve():
    # 1. 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data: return
    start_node = input_data[0]
    target_node = input_data[1]

    # 시작과 끝이 같으면 바로 0 출력
    if start_node == target_node:
        print(0)
        return

    # 2. 에라토스테네스의 체로 4자리 소수 판별기 만들기
    is_prime = [True] * 10000
    is_prime[0] = is_prime[1] = False
    for i in range(2, 101): # 100^2 = 10,000
        if is_prime[i]:
            for j in range(i*i, 10000, i):
                is_prime[j] = False

    # 3. BFS 탐색
    # (현재 번호, 버스 탄 횟수)
    queue = deque([(start_node, 0)])
    visited = [False] * 10000
    visited[int(start_node)] = True

    while queue:
        curr_str, dist = queue.popleft()
        
        # 도착 여부 확인
        if curr_str == target_node:
            print(dist)
            return

        # 각 자리수(0~3)를 변경
        for i in range(4):
            for digit in range(10):
                # 첫 번째 자리는 0이 될 수 없음
                if i == 0 and digit == 0:
                    continue
                
                # 현재 숫자와 같은 숫자로 바꾸는 것은 무시
                if curr_str[i] == str(digit):
                    continue
                
                # 새로운 숫자 생성
                next_list = list(curr_str)
                next_list[i] = str(digit)
                next_str = "".join(next_list)
                next_int = int(next_str)
                
                # 소수이고 방문하지 않았다면 탐색 추가
                if is_prime[next_int] and not visited[next_int]:
                    visited[next_int] = True
                    queue.append((next_str, dist + 1))

if __name__ == "__main__":
    solve()

####################################################################

