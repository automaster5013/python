def solve_v1():
    s = input().strip()
    t = input().strip()
    
    # S 안에 T가 존재하는 동안 무한 반복
    while t in s:
        # T를 빈 문자열("")로 딱 한 번(1) 교체
        s = s.replace(t, "", 1)
        
    print(s)

solve_v1()

################################################################

def solve_v2():
    s = input().strip()
    t = list(input().strip()) # 비교를 위해 리스트화
    t_len = len(t)
    stack = []
    
    for char in s:
        stack.append(char)
        # 스택의 끝부분이 T와 일치하는지 확인
        if len(stack) >= t_len and stack[-t_len:] == t:
            # 일치하면 T의 길이만큼 스택에서 제거
            for _ in range(t_len):
                stack.pop()
                
    print("".join(stack))

solve_v2()

################################################################

def remove_t(s, t):
    if t not in s:
        return s
    # 처음 발견된 T를 지우고 다시 호출
    return remove_t(s.replace(t, "", 1), t)

def solve_v3():
    s = input().strip()
    t = input().strip()
    print(remove_t(s, t))

solve_v3()

################################################################

def solve_v4():
    s = input().strip()
    t = input().strip()
    t_len = len(t)
    
    while True:
        idx = s.find(t)
        if idx == -1: # 더 이상 T가 없으면 탈출
            break
        # 인덱스를 기준으로 앞과 뒤를 잘라 붙임
        s = s[:idx] + s[idx + t_len:]
        
    print(s)

solve_v4()

################################################################

import re

def solve_v5():
    s = input().strip()
    t = input().strip()
    
    # T에 특수문자가 섞여 있을 수 있으므로 escape 처리
    pattern = re.escape(t)
    
    while True:
        # subn은 (결과문자열, 치환횟수)를 반환함
        s, count = re.subn(pattern, "", s, count=1)
        if count == 0:
            break
            
    print(s)

solve_v5()

################################################################


