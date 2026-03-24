a = int(input().strip())
b = int(input().strip())

ones_place = b % 10
tens_place = (b // 10) % 10
hundreds_place = b // 100

print(a * ones_place)
print(a * tens_place)
print(a * hundreds_place)
print(a * b)
