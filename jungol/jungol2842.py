import sys

def solve():
    # 문자열 S와 T 입력 받기
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    
    n, m = len(s), len(t)
    
    # 1. KMP 실패 함수(Failure Function) 계산
    # t의 각 접미사가 접두사와 얼마나 일치하는지 기록
    fail = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and t[i] != t[j]:
            j = fail[j-1]
        if t[i] == t[j]:
            j += 1
        fail[i] = j
            
    # 2. 메인 프로세스: 스택을 이용한 검열
    stack_char = [] # 최종 문자열을 구성할 문자 스택
    stack_pos = [0] # 각 시점에서의 KMP 매칭 상태(index) 저장 스택
    
    for char in s:
        stack_char.append(char)
        
        # 현재 문자가 t의 어느 위치와 일치하는지 계산
        curr_match_idx = stack_pos[-1]
        while curr_match_idx > 0 and char != t[curr_match_idx]:
            curr_match_idx = fail[curr_match_idx - 1]
        
        if char == t[curr_match_idx]:
            curr_match_idx += 1
            
        # 새로운 매칭 상태를 스택에 기록
        stack_pos.append(curr_match_idx)
        
        # 3. 금지된 문자열 T를 발견한 경우
        if curr_match_idx == m:
            # T의 길이만큼 두 스택에서 제거
            for _ in range(m):
                stack_char.pop()
                stack_pos.pop()
                
    # 최종 결과 출력
    sys.stdout.write("".join(stack_char) + "\n")

if __name__ == "__main__":
    solve()

########################################################################3

