class Person:
    def __init__(self, cm, kg):
        self.cm = int(cm)
        self.kg = kg
    def __add__(self, other):
        # print("plus 키:", self.cm + other.cm, ", 몸무게: ", self.kg + other.kg)
        print(f"plus 키: {self.cm + other.cm}, 몸무게: {self.kg + other.kg}")
    def __sub__(self, other):
        print("minus 키:", abs(self.cm - other.cm), end='')
        print(f", 몸무게: {abs(p1.kg - p2.kg):.1f}")
    def __truediv__(self, other):
        print("avg 키:", int((self.cm + other.cm)/2), ", 몸무게:", (self.kg + other.kg)/2)
    def __str__(self):
        return f"키: {self.cm}, 몸무게: {self.kg:.1f}"

cm, kg = map(float, input("당신의 키와 몸무게를 입력하세요.").split())
p1 = Person(cm, kg)

cm, kg = map(float, input("친구의 키와 몸무게를 입력하세요.").split())
p2 = Person(cm, kg)

print("my", p1)
print("friend", p2)
p1 + p2
p1 - p2
p1 / p2

##############################################################################

class Data:
    def __init__(self, h, w):
        self.h = int(h)
        self.w = float(w)

    def __add__(self, other):
        return Data(self.h + other.h, self.w + other.w)

p1 = Data(*input("당신의 키와 몸무게를 입력하세요.").split())
p2 = Data(*input("친구의 키와 몸무게를 입력하세요.").split())

p1_plus_p2 = p1 + p2

print(f"my 키: {p1.h}, 몸무게: {p1.w:.1f}")
print(f"friend 키: {p2.h}, 몸무게: {p2.w:.1f}")
print(f"plus 키: {p1_plus_p2.h}, 몸무게: {p1_plus_p2.w:.1f}")

##############################################################################


