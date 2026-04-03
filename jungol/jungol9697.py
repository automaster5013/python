class Baseball:
    def __init__(self, name, ab, h):
        self.name = name
        self.ab = int(ab)
        self.h = int(h)

team = []
for _ in range(2):
    name, ab, h = input().split()
    team.append(Baseball(name, ab, h))
    # print(name, ab, h)

for member in team:
    raw_avg = member.h / member.ab
    rounded_avg = round(raw_avg, 3)
    
    res = f"name:{member.name}, AVG:{rounded_avg:.3f}, AB:{member.ab}, H:{member.h}"
    print(res)

###########################################################################################

class Player:
    def __init__(self, name, ab, h):
        self.name = name
        self.ab = ab
        self.h = h

    def print(self):
        print(f"name:{self.name}, AVG:{self.getAVG()}, AB:{self.ab}, H:{self.h}")
        print(format(self.getAVG(), ".3f"))

    def getAVG(self):
        return int(self.h) / int(self.ab)

for i in range(2):
    name, ab, h = input().split()
    print(name, ab, h)
    p = Player(name, ab, h)
    p.print()

###########################################################################################

