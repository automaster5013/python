### 벌집 Quiz ###

# 위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 
# 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 
# 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 
# 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 
# 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

# 입력 :
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

# 출력 :
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

# 예제 입력 :
# 13

# 예제 출력 :
# 3

#####################################################################(방법01)

def solve_while():
    n = int(input())
    if n == 1:
        print(1)
        return

    boundary = 1
    layer = 1
    
    while n > boundary:
        boundary += 6 * layer
        layer += 1
    print(layer)

solve_while()

#####################################################################(방법01)

class Honeycomb:
    def __init__(self):
        self.layer = 1
        self.max_room = 1

    def expand(self):
        self.max_room += 6 * self.layer
        self.layer += 1

    def find_dist(self, target):
        while target > self.max_room:
            self.expand()
        return self.layer

h = Honeycomb()
print(h.find_dist(int(input())))

#####################################################################(방법02)

def boundary_generator():
    boundary = 1
    layer = 1
    yield boundary
    while True:
        boundary += 6 * layer
        layer += 1
        yield (boundary, layer)

def solve_generator():
    n = int(input())
    if n == 1:
        print(1)
        return
        
    gen = boundary_generator()
    next(gen)
    
    for boundary, layer in gen:
        if n <= boundary:
            print(layer)
            break

solve_generator()

#####################################################################(방법03)

def get_layer_recursive(target, current_max, current_layer):          # 런타임 에러 (RecursionError)
    if target <= current_max:
        return current_layer
    
    return get_layer_recursive(target, current_max + 6 * current_layer, current_layer + 1)

n = int(input())
print(get_layer_recursive(n, 1, 1))

#####################################################################(방법04)

def solve_honeycomb():
    target_room = int(input())
    current_layer = 1
    max_room_in_layer = 1

    while target_room > max_room_in_layer:
        growth_amount = 6 * current_layer
        max_room_in_layer = max_room_in_layer + growth_amount
        current_layer = current_layer + 1

    print(current_layer)

solve_honeycomb()

#####################################################################(방법05)

N = int(input())
boundry = 1
layer = 1
while N > boundry:
    boundry += 6 * layer
    layer += 1

print(layer)

#####################################################################(방법05)

N = int(input())
# print(N)
boundry = 1
x = 1

while True:
    if x > boundry:
        break;
    boundry = boundry + (6 * x)
    x = x + 1
    # print(x, boundry)

print(x)

    # print("x :", x, ", num :", num, ", res :",(num + (6 * x)))




# num = 1
# for x in range(5):
#     print("x :", x, ", num :", num, ", res :",(num + (6 * x)))

# 1, 2, 8, 20, 38, 62, 92, 128, 170, 218, 272, ...
#     +6 +12 +18 +24 +30 +36  +42  +48  +54 +... (6의 배수)











