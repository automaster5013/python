# 문제

# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.



# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

# 예제 입력 1 
# 472
# 385
# 예제 출력 1 
# 2360
# 3776
# 1416
# 181720

####################################################################

A = int(input())
B_str = input()

step1 = A * int(B_str[2])   # 5
step2 = A * int(B_str[1])   # 8
step3 = A * int(B_str[0])   # 3

total = A * int(B_str)

print(step1)
print(step2)
print(step3)
print(total)

####################################################################(방법01)

inp1 = input()
inp2 = input()

num1 = int(inp1)
num2 = int(inp2)

num21 = int(inp2[0])
num22 = int(inp2[1])
num23 = int(inp2[2])

print(num1 * num23)
print(num1 * num22)
print(num1 * num21)
print(num1 * num2)

####################################################################(방법02)

a=int(input())
b=input()

print(a * int(b[2]))    # 5
print(a * int(b[1]))    # 8
print(a * int(b[0]))    # 3
print(a * int(b))       # Total값 산출

####################################################################(방법03)

A = int(input())
B = int(input())

print(A * (B % 10))         # 5    : 나누기를 수행한 후 남은 나머지
print(A * ((B // 10) % 10)) # 8    : 백의 자리
print(A * (B // 100))       # 3    : 천의 자리
print(A * B)

####################################################################(방법04)

a = int(input())
b = input()

print(a * int(b[2]))    # 5
print(a * int(b[1]))    # 8
print(a * int(b[0]))    # 3
print(a * int(b))

####################################################################(방법05)

A = int(input())
B_str = input()

step1 = A * int(B_str[2])   # 5
step2 = A * int(B_str[1])   # 8
step3 = A * int(B_str[0])   # 3

total = A * int(B_str)

print(step1)
print(step2)
print(step3)
print(total)

####################################################################(방법06)

