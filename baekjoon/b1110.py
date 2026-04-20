N = int(input())
# print(N)

number = N
count = 0
while True:
    ten = number // 10
    one = number % 10
    
    hap_val = ten + one
    
    number = (one * 10) + (hap_val % 10)
    count += 1
    
    if number == N:
        break

print(count)

##############################################################(방법01)

N = int(input())
anonym = [N // 10, N % 10]
start = list(anonym)
count = 0

while True:
    count += 1
    
    new_box = (anonym[0] + anonym[1]) % 10
    anonym[0], anonym[1] = anonym[1], new_box
    
    if anonym == start:
        break
print(count)

##############################################################(방법02)



