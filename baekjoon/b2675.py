# 문제

# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
# S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

# 예제 입력 1 
# 2
# 3 ABC
# 5 /HTP
# 예제 출력 1 
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

###############################################(방법01)

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for char in S:
        print(char * R, end='') 
    print()

###############################################(방법01)

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    
    result = ''.join([char * R for char in S])
    print(result)

###############################################(방법02)

T = int(input())
for _ in range(T):
    R, S = input().split()

    print(*(char * int(R) for char in S), sep='')

###############################################(방법03)

T = int(input())

lstr = []
lsts = []

for n in range(T):
    R, S = input().split()
    lstr.append(int(R))
    lsts.append(S)

# for m in range(len(lstr)):
#     pront(lstr[m], lsts[m])

for m in range(T):
    for i in lsts[m]:
        for j in range(lstr[m]):
            print(i, end = '')

    print()    

###############################################(방법04)

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)

    for x in S:
        print(x * R, end='')
    
    print()

###############################################(방법05)

