n, m = map(int, input().split())
# print(n, m)
baskets = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    # print(i, j, k)
    baskets[i : j + 1] = [k] * (j - i + 1)

print(*(baskets[1:]))

##################################################################################(방법01)

n, m = map(int, input().split())
# print(n, m)
baskets = [0] * n 

for _ in range(m):
    i, j, k = map(int, input().split())
    # print(i, j, k)
    for idx in range(i - 1, j):
        baskets[idx] = k

print(*(baskets))

##################################################################################(방법02)

n, m = map(int, input().split())
# print(n, m)
baskets = [0] * n

for _ in range(m):
    start, end, ball = map(int, input().split())
    baskets = [ball if start - 1 <= idx < end else baskets[idx] for idx in range(n)]

print(*(baskets))

##################################################################################(방법03)

n, m = map(int, input().split())
# print(n, m)
basket_map = {num: 0 for num in range(1, n + 1)}

for _ in range(m):
    i, j, k = map(int, input().split())
    # print(i, j, k)
    for basket_num in range(i, j + 1):
        basket_map[basket_num] = k

results = [basket_map[num] for num in range(1, n + 1)]

print(*(results))

##################################################################################

class BasketSystem:
    def __init__(self, size):
        self.data = [0] * size

    def fill_range(self, i, j, k):
        for idx in range(i - 1, j):
            self.data[idx] = k

    def __str__(self):
        return " ".join(map(str, self.data))

n, m = map(int, input().split())
# print(n, m)
system = BasketSystem(n)

for _ in range(m):
    i, j, k = map(int, input().split())
    # print(i, j, k)
    system.fill_range(i, j, k)

print(system)

############################################################


