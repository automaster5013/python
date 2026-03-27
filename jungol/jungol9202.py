num1, num2 = map(int, input().split())
# print(num1, num2)

quotient = num1 // num2     # 나눈 몫
remainder = num1 % num2     # 나머지

print(f"{num1} / {num2} = {quotient} ... {remainder}")

#########################################################(방법01)

a, b = input().split()
# print(a, b)
na = int(a)
nb = int(b)
print(a, '/', b, '=', na//nb, '...', na%nb)

#########################################################(방법02)

a, b = map(int, input().split())
print(f"{a} / {b} = {a//b} ... {a%b}")

#########################################################(방법03)


