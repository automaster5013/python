# 문제

# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.

# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)

# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

# 예제 입력 1 
# ZZZZZ 36
# 예제 출력 1 
# 60466175

###############################################################################################(방법01)

n, b = input().split()
# print(n, b)
b = int(b)
result = 0

for char in n:
    if '0' <= char <= '9':
        val = ord(char) - ord('0')
    else:
        val = ord(char) - ord('A') + 10
    
    result = result * b + val

print(result)

###############################################################################################(방법01)

n, b = input().split()
print(int(n, int(b)))

###############################################################################################(방법02)

n, b = input().split()
b = int(b)

mapping = {chr(i): i-48 if i<58 else i-55 for i in range(48, 91) if chr(i).isalnum()}

total = 0
power = 1
for i in range(len(n)-1, -1, -1):
    total += mapping[n[i]] * power
    power *= b

print(total)

###############################################################################################(방법03)

n, b = input().split()
b = int(b)

# 0~9, A~Z까지의 값을 미리 딕셔너리에 담아둡니다.
# '0':0 ... '9':9, 'A':10 ... 'Z':35
mapping = {chr(i): i-48 if i<58 else i-55 for i in range(48, 91) if chr(i).isalnum()}

total = 0
power = 1
# 뒤에서부터 하나씩 꺼내어 거듭제곱을 곱합니다.
for i in range(len(n)-1, -1, -1):
    total += mapping[n[i]] * power
    power *= b

print(total)

###############################################################################################(방법04)

n, b = input().split()
b = int(b)
alphabet = "01234567879ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0
# 문자열을 뒤집어서 0제곱부터 계산하거나, 지수를 활용합니다.
for i, char in enumerate(n[::-1]):
    # '0'~'Z'의 인덱스가 해당 문자의 실제 값이 됩니다.
    value = alphabet.index(char)
    result += value * (b ** i)

print(result)

###############################################################################################(방법05)

N, B = input().split()

res = 0
for idx, ch in enumerate(N):
    res += int(ch)*(int(B)**(len(N) - 1 - idx))

else:
    res += (ord(ch) - 55)*(int(B)**(len(N) - 1 - idx))
print(res)

###############################################################################################(방법05)

A = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']

N , B = input().split()
b = int(B)
n = len(N)
s = 0
for i in N:
    I = A.index(i)
    s += I*(b**(n-1))
    n -= 1
print(s)

###############################################################################################(방법06)

N, B = input().split()
B = int(B)

num_dict = {str(i): i for i in range(10)}
num_dict.update({chr(i + 55): i for i in range(10, 36)})

total = 0
square = len(N) - 1

index = 0
while index < len(N):
    total += num_dict[N[index]] * (B ** square)
    index += 1
    square -= 1

###############################################################################################(방법07)

