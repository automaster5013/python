T = int(input())

for t in range(1, T + 1):
    nums = map(int, input().split())
    total = 0
    
    for n in nums:
        if n & 1:
            total += n
            
    print(f"#{t} {total}")

####################################################(방법01)

lst = int(input())
# print(lst)

sum = 0
for i in lst:
    print(i, end=' ')
    if int(i) % 2 != 0:
        sum += int(i)

print(f"#{test_case} {sum}")

####################################################(방법02)

N=int(input())
p=1
for _ in range(N):
    Y=list(map(int, input().split()))
    J=0
    for i in Y:
        if i%2!=0:
            J+=i
    print(f"#{p} {J}")
    p+=1

####################################################(방법03)



