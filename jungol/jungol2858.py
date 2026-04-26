import sys

def solve_v1():
    # 입력을 빠르게 읽어옵니다.
    s = sys.stdin.readline().strip()
    if not s: return

    total_pieces = 0
    current_rods = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            current_rods += 1
        else: # ')' 인 경우
            current_rods -= 1
            if s[i-1] == '(': # 레이저인 경우
                total_pieces += current_rods
            else: # 막대기의 끝인 경우
                total_pieces += 1
                
    print(total_pieces)

solve_v1()

###############################################################

import sys

def solve_v2():
    data = sys.stdin.readline().strip()
    # 레이저를 'L'로 변환하여 쇠막대기의 괄호와 구분합니다.
    refined = data.replace('()', 'L')
    
    stack_count = 0
    ans = 0
    
    for char in refined:
        if char == '(':
            stack_count += 1
        elif char == ')':
            stack_count -= 1
            ans += 1 # 막대기가 끝날 때 생기는 마지막 조각
        else: # 'L' (레이저) 인 경우
            ans += stack_count # 현재 겹쳐진 막대기 수만큼 조각 추가
            
    print(ans)

solve_v2()

###############################################################

import sys

def solve_v3():
    s = sys.stdin.readline().strip()
    stack = []
    result = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            # 스택에서 하나를 꺼냄 (짝 맞추기)
            start_idx = stack.pop()
            if i - start_idx == 1: # 인덱스 차이가 1이면 레이저
                result += len(stack)
            else: # 막대기의 끝
                result += 1
                
    print(result)

solve_v3()

###############################################################

import sys

def solve_v4():
    line = sys.stdin.readline().strip()
    pieces = 0
    rods = 0
    prev = ""
    
    for char in line:
        if char == '(':
            rods += 1
        else:
            rods -= 1
            if prev == '(': # 레이저 판정
                pieces += rods
            else: # 막대기 끝 판정
                pieces += 1
        prev = char # 현재 상태를 저장
        
    print(pieces)

solve_v4()

###############################################################

import sys

def solve_v5():
    s = sys.stdin.readline().strip()
    
    def count_pieces(s):
        rods = 0
        total = 0
        for i, char in enumerate(s):
            if char == '(':
                rods += 1
            else:
                rods -= 1
                total += rods if s[i-1] == '(' else 1
        return total

    if s:
        print(count_pieces(s))

solve_v5()

###############################################################

