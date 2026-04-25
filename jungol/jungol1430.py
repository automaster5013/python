a = int(input())
b = int(input())
c = int(input())

# 1. 곱셈 결과 계산 후 문자열로 변환
result_str = str(a * b * c)

# 2. '0'부터 '9'까지 반복하며 각 숫자의 개수 출력
for i in range(10):
    print(result_str.count(str(i)))

##############################################################

a = int(input())
b = int(input())
c = int(input())

product = a * b * c
# 0부터 9까지의 빈도를 저장할 공간 (0으로 초기화)
counts = [0] * 10

# 곱셈 결과를 한 글자씩 확인하며 해당 인덱스의 값 증가
for digit in str(product):
    counts[int(digit)] += 1

# 결과 출력
for count in counts:
    print(count)

##############################################################

a = int(input())
b = int(input())
c = int(input())

product = a * b * c
counts = [0] * 10

# 숫자가 0이 될 때까지 마지막 자릿수를 하나씩 추출
temp = product
while temp > 0:
    digit = temp % 10  # 마지막 자리 숫자 추출
    counts[digit] += 1
    temp //= 10        # 마지막 자리 숫자 제거

for count in counts:
    print(count)

##############################################################

a = int(input())
b = int(input())
c = int(input())

product_str = str(a * b * c)
# 딕셔너리 초기화 (0~9까지 0으로 설정)
digit_map = {str(i): 0 for i in range(10)}

for char in product_str:
    digit_map[char] += 1

# 순서대로 출력
for i in range(10):
    print(digit_map[str(i)])

##############################################################

a = int(input())
b = int(input())
c = int(input())

res = str(a * b * c)

# 각 숫자 i에 대해 res의 글자 x가 i와 같은 경우만 모아 그 길이를 출력
for i in range(10):
    count = len([x for x in res if x == str(i)])
    print(count)

##############################################################

