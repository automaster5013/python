class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

x1, y1 = map(float, input().split())
# print(x1, y1)
p1 = Point(x1, y1)

x2, y2 = map(float, input().split())
# print(x2, y2)
p2 = Point(x2, y2)

p_add = p1 + p2
p_sub = p1 - p2
p_center = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

print(f"add = {p_add}")
print(f"sub = {p_sub}")
print(f"center = {p_center}")

#############################################################################

