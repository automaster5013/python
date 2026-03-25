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
