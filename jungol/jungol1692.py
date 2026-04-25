a = int(input())
b = int(input())

# 자릿수 추출
ones = b % 10
tens = (b % 100) // 10
hundreds = b // 100

# 결과 출력
print(a * ones)
print(a * tens)
print(a * hundreds)
print(a * b)

#########################################

a = int(input())
b_str = input() # 두 번째 숫자를 문자열로 받음

# 인덱스 2는 일의 자리, 1은 십의 자리, 0은 백의 자리
print(a * int(b_str[2]))
print(a * int(b_str[1]))
print(a * int(b_str[0]))
print(a * int(b_str))

#########################################

a = int(input())
b_str = input()

# 역순으로 하나씩 꺼내어 곱하기
for digit in b_str[::-1]:
    print(a * int(digit))

# 전체 결과 출력
print(a * int(b_str))

#########################################

a = int(input())
b = int(input())

temp_b = b
# 세 번의 연산을 통해 각 자릿수를 하향식으로 추출
for _ in range(3):
    temp_b, digit = divmod(temp_b, 10)
    print(a * digit)

print(a * b)

#########################################

a = int(input())
b = int(input())

# 10의 0승(일), 1승(십), 2승(백)의 자릿수를 리스트로 생성
digits = [(b // (10**i)) % 10 for i in range(3)]

for d in digits:
    print(a * d)

print(a * b)

#########################################

