# 문제

# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
# 예를 들어, 10번 문제의 점수는 3이 된다.

# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
# 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.

# 예제 입력 1 
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
# 예제 출력 1 
# 10
# 9
# 7
# 55
# 30

#############################################################(방법01)

T = int(input())

for i in range(T):
    ox_res = input()
    total_score = 0
    current_streak = 0
    
    for char in ox_res:
        match char:
            case 'O':
                current_streak += 1
                total_score += current_streak
            case 'X':
                current_streak = 0
            case _:
                pass
    print(total_score)

#############################################################(방법01)

t = int(input())
# 1. 인덱스 초기화
i = 0 
while i < t:
    ox_res = input()

    total_score = 0 
    current_streak = 0 
    
    # 2. 문자열 탐색용 인덱스 초기화
    j = 0
    while j < len(ox_res):
        # 인덱스를 이용해 문자에 접근
        char = ox_res[j]
        
        if char == 'O':
            current_streak += 1
            total_score += current_streak
        else:
            current_streak = 0
        # 3. 다음 문자로 넘어가기 위해 인덱스를 1 증가
        j += 1
           
    print(total_score)
    
    # 4. 다음 테스트 케이스로 넘어가기 위해 인덱스를 1 증가
    i += 1

#############################################################(방법02)

t = int(input())
for i in range(t):
    ox_res = input()

    total_score = 0 
    current_streak = 0 

    for char in ox_res:
        if char == 'O':
            current_streak += 1
            total_score += current_streak
        else:
            current_streak = 0
           
    print(total_score)

#############################################################(방법03)

T = int(input())
for i in range(T):
    ox = input()
    total_score = 0
    current_streak = 0
    
    for char in ox:
        current_streak = current_streak + 1 if char == 'O' else 0
        total_score += current_streak
        
    print(total_score)

#############################################################(방법04)

T = int(input())
for i in range(T):
    # 'X'를 기준으로 나누면 'OO', 'O', 'OOO' 같은 덩어리만 남는다.
    groups = input().split('X')
    score = 0
    
    for g in groups:
        n = len(g)
        # 각 덩어리의 길이를 n이라 할 때, 1~n까지의 합을 바로 더한다.
        score += n * (n + 1) // 2
        
    print(score)

#############################################################(방법05)

T = int(input())
for i in range(T):
    ox = input()
    # 각 칸의 점수를 저장할 리스트를 만든다.
    memo = [0] * len(ox)
    
    for i in range(len(ox)):
        if ox[i] == 'O':
            # 첫 번째 칸이거나 이전 칸이 'X'라면 1점, 아니면 이전 점수 + 1
            if i == 0 or ox[i-1] == 'X':
                memo[i] = 1
            else:
                memo[i] = memo[i-1] + 1
                
    # 모든 칸에 기록된 점수의 총합이 정답
    print(sum(memo))

#############################################################(방법06)

def get_score(string, idx, streak):
    # 더 이상 읽을 문자가 없으면 종료 (Base Case)
    if idx == len(string):
        return 0
    
    # 현재 문자가 'O'면 streak을 높이고, 'X'면 0으로 초기화
    new_streak = streak + 1 if string[idx] == 'O' else 0
    
    # (현재 내 점수) + (다음 칸부터의 점수들)을 합산하여 반환
    return new_streak + get_score(string, idx + 1, new_streak)

T = int(input())
for i in range(T):
    print(get_score(input(), 0, 0))

#############################################################(방법07)

T = int(input())
for i in range(T):
    ox = input()
    n = len(ox)
    total = 0
    i = 0
    
    while i < n:
        if ox[i] == 'O':
            start = i
            # 'O'가 끝날 때까지 오른쪽 포인터를 이동
            while i < n and ox[i] == 'O':
                i += 1
            # 찾아낸 'O' 군집의 길이를 계산
            length = i - start
            total += length * (length + 1) // 2
        else:
            i += 1
            
    print(total)

#############################################################(방법08)

### Hint ###
T = int(input())
for x in range(T):
    str = input()       # OOXXOXXOOO
    # print(str)

    sum = 0
    score = 1
    for i in str:
        # print(i, end=' ')
        if i == 'O':
            sum += score
            score += 1
        else:
            score = 1
    print(sum)

#############################################################(방법09)

N = int(input())

for _ in range(N):
    OXshow = list(input())
    Q = 0
    coin = 0
    for i in range(len(OXshow)):
        if OXshow[i] == "O" :
            coin += 1
        else:
            coin = 0
        Q += coin
    print(Q)

#############################################################(방법10)





