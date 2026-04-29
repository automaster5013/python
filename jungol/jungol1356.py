import sys

def solve():
    # 고속 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 양 끝에 가상의 숫자 0과 n+1을 추가하여 경계 검사를 단순화
    board = [0] + [int(x) for x in input_data[1:]] + [n + 1]

    # 1. 불연속 지점을 기반으로 후보 인덱스 추출
    points = set()
    for i in range(n + 1):
        if abs(board[i] - board[i+1]) != 1:
            points.add(i)
            points.add(i + 1)
    
    # 1부터 n 사이의 유효한 인덱스만 후보로 사용
    candidates = sorted([p for p in points if 1 <= p <= n])
    
    # 만약 후보가 너무 적으면 강제로 추가 (예: 이미 정렬된 경우 등)
    if 1 not in candidates: candidates.append(1)
    if n not in candidates: candidates.append(n)
    candidates = sorted(list(set(candidates)))

    # 2. 첫 번째 뒤집기 시도
    num_c = len(candidates)
    for i in range(num_c):
        for j in range(i, num_c):
            p1, p2 = candidates[i], candidates[j]
            
            # 첫 번째 뒤집기 실행
            temp_board = board[:p1] + board[p1:p2+1][::-1] + board[p2+1:]
            
            # 3. 두 번째 뒤집기 구간 찾기
            # 정렬된 상태(A[k] == k)와 다른 시작점(L)과 끝점(R)을 찾음
            L, R = -1, -1
            for k in range(1, n + 1):
                if temp_board[k] != k:
                    if L == -1: L = k
                    R = k
            
            # 이미 정렬된 경우 (두 번째 뒤집기는 아무데나, 예: [1, 1])
            if L == -1:
                print(f"{p1} {p2}")
                print("1 1")
                return
            
            # 두 번째 후보 구간 [L, R]을 뒤집어보고 최종 확인
            final_board = temp_board[:L] + temp_board[L:R+1][::-1] + temp_board[R+1:]
            
            is_ok = True
            for k in range(1, n + 1):
                if final_board[k] != k:
                    is_ok = False
                    break
            
            if is_ok:
                print(f"{p1} {p2}")
                print(f"{L} {R}")
                return

if __name__ == "__main__":
    solve()

#########################################################################################

