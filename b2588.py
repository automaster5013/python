a = int(input().strip())
b = int(input().strip())

ones_place = b % 10             # 5     ' % ' 연산자 (Modulo) - 나누기를 수행한 후 남은 나머지를 구합니다.
tens_place = (b // 10) % 10     # 8     '//' 연산자 (Floor Division): 
hundreds_place = b // 100       # 3      - 나누기를 수행한 뒤, 소수점 이하를 버리고 **결과의 정수 부분(몫)**만 남깁니다.

print(a * ones_place)
print(a * tens_place)
print(a * hundreds_place)
print(a * b)
