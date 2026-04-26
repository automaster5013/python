import sys

def solve_v1():
    # 입력 받기
    m = int(sys.stdin.readline())
    expr = sys.stdin.readline().split()
    
    stack = []
    
    for token in expr:
        if token.isdigit(): # 피연산자(숫자)인 경우
            stack.append(int(token))
        else: # 연산자인 경우
            # 스택에서 두 개의 값을 꺼냄 (순서 주의)
            b = stack.pop()
            a = stack.pop()
            
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': 
                # 소수점 이하를 버리는 정수 나눗셈 처리
                stack.append(int(a / b))
                
    print(stack[0])

solve_v1()

##################################################################

import operator

def solve_v2():
    n = int(input())
    tokens = input().split()
    
    # 연산자와 함수를 1:1 매핑
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': lambda x, y: int(x / y) # 나눗셈 조건 반영
    }
    
    stack = []
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
            
    print(stack[0])

solve_v2()

##################################################################

class PostfixCalculator:
    def __init__(self):
        self.stack = []

    def calculate(self, tokens):
        for t in tokens:
            if t.isdigit():
                self.stack.append(int(t))
            else:
                self._operate(t)
        return self.stack[0]

    def _operate(self, op):
        val2 = self.stack.pop()
        val1 = self.stack.pop()
        if op == '+': self.stack.append(val1 + val2)
        elif op == '-': self.stack.append(val1 - val2)
        elif op == '*': self.stack.append(val1 * val2)
        elif op == '/': self.stack.append(int(val1 / val2))

def solve_v3():
    m = int(input())
    expr = input().split()
    calc = PostfixCalculator()
    print(calc.calculate(expr))

solve_v3()

##################################################################

def solve_v4():
    m = int(input())
    data = input().split()
    stack = []
    
    for item in data:
        if item.isdigit():
            stack.append(item)
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            # 수식을 문자열로 만들어 eval로 실행
            # 나눗셈은 int()로 감싸서 소수점 제거
            if item == '/':
                res = int(eval(f"{v1} / {v2}"))
            else:
                res = eval(f"{v1} {item} {v2}")
            stack.append(str(res))
            
    print(stack[0])

solve_v4()

##################################################################

def solve_v5():
    m = int(input())
    tokens = input().split()
    
    while len(tokens) > 1:
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                # 연산자 발견 시 앞의 두 피연산자와 함께 계산
                v1, v2, op = int(tokens[i-2]), int(tokens[i-1]), tokens[i]
                
                if op == '+': res = v1 + v2
                elif op == '-': res = v1 - v2
                elif op == '*': res = v1 * v2
                else: res = int(v1 / v2)
                
                # 계산된 3개의 토큰을 결과값 하나로 교체
                tokens[i-2:i+1] = [str(res)]
                break
                
    print(tokens[0])

solve_v5()

##################################################################









