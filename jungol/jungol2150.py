import sys
from collections import deque

def solve():
    # 입력을 빠르게 읽어옵니다.
    A = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()
    
    if not A or not T:
        print(T)
        return

    len_a = len(A)
    rev_A = A[::-1] # 오른쪽 탐색을 위한 A의 역순
    
    left_stack = []
    right_stack = []
    
    lp = 0
    rp = len(T) - 1
    
    # 왼쪽 탐색 모드인지(True) 오른쪽 탐색 모드인지(False) 결정
    is_left_turn = True
    
    while lp <= rp:
        if is_left_turn:
            # 왼쪽에서부터 문자 추가
            left_stack.append(T[lp])
            lp += 1
            # 스택의 끝이 A와 일치하면 삭제 후 방향 전환
            if len(left_stack) >= len_a and "".join(left_stack[-len_a:]) == A:
                for _ in range(len_a):
                    left_stack.pop()
                is_left_turn = False
        else:
            # 오른쪽에서부터 문자 추가
            right_stack.append(T[rp])
            rp -= 1
            # 스택의 끝이 A의 역순과 일치하면 삭제 후 방향 전환
            if len(right_stack) >= len_a and "".join(right_stack[-len_a:]) == rev_A:
                for _ in range(len_a):
                    right_stack.pop()
                is_left_turn = True

    # 두 스택 병합 (오른쪽 스택은 역순으로 들어있으므로 뒤집어서 합침)
    result_stack = left_stack + right_stack[::-1]
    
    # 병합된 경계선에서 생겼을 수 있는 A를 최종적으로 제거
    final_res = []
    for char in result_stack:
        final_res.append(char)
        if len(final_res) >= len_a and "".join(final_res[-len_a:]) == A:
            for _ in range(len_a):
                final_res.pop()
                
    sys.stdout.write("".join(final_res) + "\n")

if __name__ == "__main__":
    solve()

############################################################################################3



