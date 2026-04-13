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

###############################################################

n, b = input().split()
# print(n, b)
print(int(n, int(b)))

###############################################################

n, b = input().split()
b = int(b)

mapping = {chr(i): i-48 if i<58 else i-55 for i in range(48, 91) if chr(i).isalnum()}

total = 0
power = 1
for i in range(len(n)-1, -1, -1):
    total += mapping[n[i]] * power
    power *= b

print(total)

###############################################################

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

###############################################################################################









