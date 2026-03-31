class Building:
    def __init__(self, year, price):
        self.year = year
        self.price = price

n = int(input())

delpi = [Building(*map(int, input().split())) for _ in range(n)]

target_y, target_p = map(int, input().split())

for b in delpi:
    if b.year >= target_y and b.price <= target_p:
        print(b.year, b.price)

###########################################################################(방법01)

class Building:
    def __init__(self, year, price):
        self.year = int(year)
        self.price = int(price)
        
    def is_match(self, target_y, target_p):
        return self.year >= target_y and self.price <= target_p

n = int(input())

delpi = []
for _ in range(n):
    y, p = map(int, input().split())
    delpi.append(Building(y, p))

Y, P = map(int, input().split())

for b in delpi:
    if b.is_match(Y, P):
        print(f"{b.year} {b.price}")

###########################################################################(방법02)

class Building:
    def __init__(self, y, p):
        self.year = y
        self.price = p

n = int(input())

data = []

for _ in range(n):
    data.append(Building(*map(int, input().split())))

y_limit, p_limit = map(int, input().split())

delpi = [b for b in data if b.year >= y_limit and b.price <= p_limit]

for item in delpi:
    print(item.year, item.price)

###########################################################################(방법03)

class Building:
    def __init__(self, year, price):
        self.year = year
        self.price = price
    def print_building(self):
        print(self.year, self.price)

blst = []

N = int(input())
for i in range(N):
    year, price = map(int, input().split())
    b = Building(year, price)
    blst.append(b)

Y, P = map(int, input().split())

for k in range(N):
    if blst[k].year >= Y and blst[k].price <= P:
        blst[k].print_building()

###########################################################################(방법04)

