n = int(input())
# print(n)
for i in range(1, n + 1):
    if n % i == 0:
        print(f"{i}(은)는 {n}의 약수입니다.")

##############################################################(방법01)

n = int(input())
# print(n)
i = 1
while i <= n:
    if n % i == 0:
        print(f"{i}(은)는 {n}의 약수입니다.")
    i += 1

##############################################################(방법02)

n = int(input())
# print(n)
divisors = [i for i in range(1, n + 1) if n % i == 0]

for d in divisors:
    print(f"{d}(은)는 {n}의 약수입니다.")

##############################################################(방법03)

def print_divisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(f"{i}(은)는 {num}의 약수입니다.")

try:
    target = int(input())
    print_divisors(target)
except EOFError:
    pass

##############################################################(방법04)

data = input()
# print(data)
if data:
    n = int(data)
    for i in range(1, n + 1):
        if n % i == 0:
            print("%d(은)는 %d의 약수입니다." % (i, n))

##############################################################(방법05)

































