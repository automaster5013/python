def getCircle_area(r):
    return r * r * 3.14

r = float(input())
area = getCircle_area(r)
print(f"{area:.2f}")

#######################################(방법01)

def CalcArea(r):
    return r

r = float(input())
CalcArea = lambda r: r * r * 3.14
print("{:.2f}".format(CalcArea(r)))

#######################################(방법02)

def get_area_circle(r):
    return r * r * 3.14

r = int(input())
ret = get_area_circle(r)
print(f"{ret:.2f}")

#######################################(방법03)

def get_area_circle(lth):       # lth = r
    area = lth * lth * 3.14
    return area

r = int(input())
# print(r)
ret = get_area_circle(r)
# print(ret)
print("%.2f" % ret)    # 형식지정자(.2f) 사용

#######################################(방법04)

class Cir:
    def __init__(self,harf,pi):
        self.harf=harf
        self.pi=pi

    def cla(self):
        return ((self.harf**2)*self.pi)

H=int(input())
P=3.14

p=Cir(H,P)
result=p.cla()
print(f"{result:.2f}")

#######################################(방법05)

