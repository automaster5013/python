N = int(input())
# print(N)
for i in range(10, N + 1):
    if i % 10 == 0:  
        print(i)

########################################################(방법01)

N = int(input())
# print(N)
for i in range(10, N + 1, 10):
    print(i)

########################################################(방법02)

def print_tens(N):
    i = 10
    while i <= N:
        print(i)
        i += 10

limit = int(input())
# print(limit)
print_tens(limit)

########################################################(방법03)

def print_tens(N):
    if N < 10: return
    
    i = 10
    while True:
        print(i)
        i += 10
        
        if i > N:
            break

limit = int(input())
# print(limit)
print_tens(limit)

########################################################(방법04)

N = int(input())
# print(N)

for i in range(10, N+1):
    if i % 10 == 0:
        print(i)

########################################################(방법05 - for문)

N = int(input())
# print(N)

j = 10
while j <= N:
    print(j)
    j += 10

########################################################(방법06 - while문)

