T = int(input())
# print(T)

for _ in range(T):
    R, S = input().split()
    # print(R, S)
    R = int(R)

    for char in S:
        print(char * R, end='') 
    print()

###############################################(방법01)

T = int(input())
# print(T)

for _ in range(T):
    R, S = input().split()
    # print(R, S)
    R = int(R)
    
    result = ''.join([char * R for char in S])
    print(result)

###############################################(방법02)

T = int(input())
for _ in range(T):
    R, S = input().split()
    # print(R, S)

    print(*(char * int(R) for char in S), sep='')

###############################################(방법03)

T = int(input())
# print(T)

for n in range(T):
    R, S = input().split()
    # print(R, S)
    R = int(R)
    
    for i in S:
        for j in range(int(R)):
            print(i, end = '')

###############################################(방법04)

T = int(input())
# print(T)

lstr = []
lsts = []

for n in range(T):
    R, S = input().split()
    # print(R, S)
    lstr.append(int(R))
    lsts.append(S)

# for m in range(len(lstr)):
#     pront(lstr[m], lsts[m])

for m in range(T):
    for i in lsts[m]:
        for j in range(lstr[m]):
            print(i, end = '')

    print()    

###############################################(방법05)

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for x in S:
        print(x * R, end='')
    
    print()

###############################################(방법06)

