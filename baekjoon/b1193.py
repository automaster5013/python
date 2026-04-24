# 문제

# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

# 예제 입력 1 
# 1
# 예제 출력 1 
# 1/1
# 예제 입력 2 
# 2
# 예제 출력 2 
# 1/2
# 예제 입력 3 
# 3
# 예제 출력 3 
# 2/1
# 예제 입력 4 
# 4
# 예제 출력 4 
# 3/1
# 예제 입력 5 
# 5
# 예제 출력 5 
# 2/2
# 예제 입력 6 
# 6
# 예제 출력 6 
# 1/3
# 예제 입력 7 
# 7
# 예제 출력 7 
# 1/4
# 예제 입력 8 
# 8
# 예제 출력 8 
# 2/3
# 예제 입력 9 
# 9
# 예제 출력 9 
# 3/2
# 예제 입력 10 
# 14
# 예제 출력 10 
# 2/4

##################################################################(방법01)

X = int(input())
diagonal = 1
# X가 몇 번째 대각선에 있는지 찾기
while X > diagonal:
    X -= diagonal
    diagonal += 1
# diagonal이 짝수면 위로, 홀수면 아래로 방향 결정
if diagonal % 2 == 0:
    up = X
    down = diagonal - X + 1
else:
    up = diagonal - X + 1
    down = X

print(f"{up}/{down}")

##################################################################(방법01)

X = int(input())
diagonal = 0
total_count = 0

while True:
    diagonal += 1
    total_count += diagonal
    if total_count >= X:
        break

# 해당 라인에서의 상대적 위치 계산
gap = total_count - X
if diagonal % 2 == 0: # 짝수: 뒤에서부터 계산
    up = diagonal - gap
    down = 1 + gap
else: # 홀수: 앞에서부터 계산
    up = 1 + gap
    down = diagonal - gap

print(f"{up}/{down}")

##################################################################(방법02)

X = int(input())
current_max = 0

for diagonal in range(1, 5000): # 충분한 범위 설정
    current_max += diagonal
    if X <= current_max:
        # 현재 칸이 속한 대각선의 첫 번째 번호와의 거리
        pos = X - (current_max - diagonal)
        
        if diagonal % 2 == 0:
            print(f"{pos}/{diagonal - pos + 1}")
        else:
            print(f"{diagonal - pos + 1}/{pos}")
        break

##################################################################(방법03)

X = int(input())
diagonal = 1
while X > diagonal:
    X -= diagonal
    diagonal += 1

# 시작점 설정
if diagonal % 2 == 0:
    up, down = 1, diagonal
    step = 1 # 분자 증가 방향
else:
    up, down = diagonal, 1
    step = -1 # 분자 감소 방향

# X-1만큼 이동 (X는 현재 라인에서의 순번)
up += step * (X - 1)
down -= step * (X - 1)

print(f"{up}/{down}")

##################################################################(방법04)

X = int(input())
diagonal = 1
temp_x = X

while temp_x > diagonal:
    temp_x -= diagonal
    diagonal += 1
else:
    # 루프가 정상 종료된 후(대각선을 찾은 후) 실행
    if diagonal % 2 == 0:
        up, down = temp_x, diagonal - temp_x + 1
    else:
        up, down = diagonal - temp_x + 1, temp_x
    print(str(up) + "/" + str(down))

##################################################################(방법05)

X = int(input())

# n(n+1)/2 >= X 를 만족하는 정수 n을 수학적으로 근사
# 루프를 돌지 않고 바로 n값을 찾아내는 창의적 접근
n = int((2 * X) ** 0.5)
while n * (n + 1) // 2 < X:
    n += 1

# 이미 n(대각선 번호)을 찾았으므로 나머지는 동일하게 계산
gap = n * (n + 1) // 2 - X
if n % 2 == 0:
    print(f"{n - gap}/{1 + gap}")
else:
    print(f"{1 + gap}/{n - gap}")

##################################################################(방법06)

X = int(input())
diagonal = 1
while X > diagonal:
    X -= diagonal
    diagonal += 1

# 짝수일 때 1, 홀수일 때 0이 되는 스위치
is_even = 1 - (diagonal % 2)

# if문 없이 수식으로만 계산 (is_even이 1이면 윗줄, 0이면 아랫줄 실행 효과)
top = X * is_even + (diagonal - X + 1) * (1 - is_even)
bottom = (diagonal - X + 1) * is_even + X * (1 - is_even)

print(f"{top}/{bottom}")

##################################################################(방법07)

X = int(input())
diagonal = 1
step = 100 # 100개 라인씩 점프!

# 크게 점프하여 범위 좁히기
while (diagonal + step) * (diagonal + step + 1) // 2 < X:
    diagonal += step

# 세부 탐색
while diagonal * (diagonal + 1) // 2 < X:
    diagonal += 1

# 현재 대각선까지의 누적합 계산
prev_max = (diagonal - 1) * diagonal // 2
pos = X - prev_max

if diagonal % 2 == 0:
    print(f"{pos}/{diagonal - pos + 1}")
else:
    print(f"{diagonal - pos + 1}/{pos}")

##################################################################(방법08)

x = int(input())

diagonal = 1
# 1. X가 몇 번째 대각선(line)에 있는지 찾기
while x > diagonal:
    x -= diagonal
    diagonal += 1

# 2. 지그재그 방향에 따라 분자, 분모 결정
if diagonal % 2 == 0:
    # 짝수번째 대각선: 위에서 아래로 (분자 증가, 분모 감소)
    up = x
    down = diagonal - x + 1
else:
    # 홀수번째 대각선: 아래에서 위로 (분자 감소, 분모 증가)
    up = diagonal - x + 1
    down = x

print(f"{up}/{down}")

##################################################################(방법09)

x = int(input())

# 1. n(n+1)/2 >= x 를 만족하는 최소의 n 찾기
# (물론 근의 공식으로 직접 구할 수도 있지만, 논리적 추론을 위해 반복 사용)
diagonal = 0
max_val = 0
while max_val < x:
    diagonal += 1
    max_val = diagonal * (diagonal + 1) // 2

# 2. 해당 라인의 끝 번호(max_val)와 X의 차이 계산
gap = max_val - x

if diagonal % 2 == 0:
    # 짝수 라인은 끝 번호가 n/1 형태
    up = diagonal - gap
    down = 1 + gap
else:
    # 홀수 라인은 끝 번호가 1/n 형태
    up = 1 + gap
    down = diagonal - gap

print(f"{up}/{down}")

##################################################################(방법10)

X = int(input())

# n번째 대각선까지의 총 개수는 n(n+1)/2
# 이 합이 X보다 크거나 같아지는 최소의 n(diagonal)을 탐색
diagonal = 1
while diagonal * (diagonal + 1) // 2 < X:
    diagonal += 1

# 해당 대각선의 최대 번호(last_num)를 구함
last_num = diagonal * (diagonal + 1) // 2
# 대각선 끝에서부터 X가 얼마나 떨어져 있는지 계산 (gap)
gap = last_num - X

if diagonal % 2 == 0:
    # 짝수 라인은 끝번호가 'diagonal/1'
    # 거기서 gap만큼 뒤로 가야 하므로 분자는 감소, 분모는 증가
    print(f"{diagonal - gap}/{1 + gap}")
else:
    # 홀수 라인은 끝번호가 '1/diagonal'
    # 거기서 gap만큼 뒤로 가야 하므로 분자는 증가, 분모는 감소
    print(f"{1 + gap}/{diagonal - gap}")

##################################################################(방법11)

X = int(input())

# 대각선 번호를 하나씩 올리며 X의 위치를 좁힌다.
diagonal = 0
max_val = 0
while X > max_val:
    diagonal += 1
    max_val += diagonal

# gap: 현재 대각선의 가장 마지막 번호와 X의 차이
gap = max_val - X

# 짝수/홀수에 따른 분자(a), 분모(b) 결정
# 짝수는 아래로 내려가는 방향, 홀수는 위로 올라가는 방향
if diagonal % 2 == 0:
    up = diagonal - gap
    down = gap + 1
else:
    up = gap + 1
    down = diagonal - gap

# 문자열 포맷팅으로 속도 확보
print(str(up) + "/" + str(down))

##################################################################(방법12)

X = int(input())
diagonal = 1
while X > diagonal:
    X -= diagonal
    diagonal += 1

# [홀수일 때 결과, 짝수일 때 결과]를 리스트에 미리 담아둠
# 홀수(diagonal%2==1): 분자 감소(diagonal-X+1), 분모 증가(X)
# 짝수(diagonal%2==0): 분자 증가(X), 분모 감소(diagonal-X+1)
results = [
    (X, diagonal - X + 1),          # diagonal이 짝수일 때 (index 0)
    (diagonal - X + 1, X)           # diagonal이 홀수일 때 (index 1)
]

# diagonal % 2 결과에 따라 튜플을 선택하고 언패킹 출력
up, down = results[diagonal % 2]
print(f"{up}/{down}")

##################################################################(방법13)

X = int(input())
diagonal = 1
while diagonal * (diagonal + 1) // 2 < X:
    diagonal += 1

# 일단 모든 대각선 라인이 짝수(아래서 위로)라고 가정하고 좌표 계산
# n번째 대각선의 마지막 번호에서 X까지의 거리(gap) 이용
gap = diagonal * (diagonal + 1) // 2 - X
up, down = diagonal - gap, 1 + gap

# 만약 홀수 라인이면 분자와 분모를 스왑(Swap)
if diagonal % 2 == 1:
    up, down = down, up

print(f"{up}/{down}")

##################################################################(방법14)

X = int(input())
diagonal = 1
while X > diagonal:
    X -= diagonal
    diagonal += 1

# 짝수면 분자가 X, 홀수면 분자가 (diagonal - X + 1)
# 분자만 결정되면 분모는 (합계 - 분자)로 자동 결정됨
target_sum = diagonal + 1
up = [diagonal - X + 1, X][diagonal % 2 == 0] 
down = target_sum - up

print(f"{up}/{down}")

##################################################################(방법15)

X = int(input())
# print(X)
L = 1
while X > L:
    X -= L
    L += 1

# 짝수/홀수 판별과 계산을 동시에 수행
print(f"{X}/{L-X+1}" if L%2==0 else f"{L-X+1}/{X}")

##################################################################(방법16)

X = int(input())
diagonal = 1
while X > diagonal:
    X -= diagonal
    diagonal += 1

# diagonal이 짝수인지 여부를 숫자로 변환 (1 또는 0)
even = int(diagonal % 2 == 0)
odd = 1 - even

# if 없이 수식만으로 분자(up)와 분모(down) 결정
up = X * even + (diagonal - X + 1) * odd
down = (diagonal - X + 1) * even + X * odd

print(f"{up}/{down}")

##################################################################(방법17)

a = int(input())  
group = 1

while a > group: 
   a -= group 
   group += 1

if group % 2 == 0:   
   bunja = a
   bunmo = group - a + 1
   
else: 
   bunja = group - a + 1
   bunmo = a

print(f"{bunja}/{bunmo}")

##################################################################(방법18)

n = int(input())
f = 1  # 층수
m = 0  # 대빵
while m+f < n:
    m += f
    f += 1
l = n-m
if f % 2 == 0: #짝수 층(왼-오)
    x = l
    y = f-l+1
else:         #홀수 층(오-왼)
    x = f-l+1
    y = l
print(f"{x}/{y}")

##################################################################(방법19)

