def factorial_recursive(n):
    # 기저 조건 (Base Case): 1!에 도달했을 때
    if n == 1:
        print("1! = 1")
        return 1
    
    # 문제의 형식에 맞춰 과정 출력
    print(f"{n}! = {n} * {n-1}!")
    
    # 자기 자신을 호출하며 결과 계산
    return n * factorial_recursive(n - 1)

n = int(input())
result = factorial_recursive(n)
print(result)

###########################################################

n = int(input())
target = n
result = 1

# 출력용 루프
while target > 1:
    print(f"{target}! = {target} * {target-1}!")
    target -= 1
print("1! = 1")

# 계산용 루프 (1부터 n까지 곱하기)
for i in range(1, n + 1):
    result *= i

print(result)

###########################################################

n = int(input())

# 과정 메시지 생성
steps = [f"{i}! = {i} * {i-1}!" for i in range(n, 1, -1)]
steps.append("1! = 1")

# 계산 수행
result = 1
for i in range(1, n + 1):
    result *= i

# 한꺼번에 출력
for s in steps:
    print(s)
print(result)

###########################################################

n = int(input())

def solve(x, current_val):
    if x == 1:
        print("1! = 1")
        return current_val
    
    print(f"{x}! = {x} * {x-1}!")
    return solve(x - 1, current_val * x)

# 초기값 1부터 시작하는 꼬리 재귀(Tail Recursion) 형태
print(solve(n, 1))

###########################################################

n = int(input())
output_buffer = ""
total = 1

# 1부터 n까지 계산하며 과정을 버퍼에 쌓기
# 출력 순서를 맞추기 위해 역순(n부터 2까지) 루프
for i in range(n, 1, -1):
    output_buffer += f"{i}! = {i} * {i-1}!\n"
    total *= i

output_buffer += "1! = 1"

print(output_buffer)
print(total)

###########################################################



