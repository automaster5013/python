
while True:
    a, b = map(int, input().split())
    if 2 <= a <= 9 and 2 <= b <= 9:
        step = 1 if a <= b else -1
        gugudan = range(a, b + step, step)
        
        for i in range(1, 10):
            line = [f"{nums} * {i} = {nums * i:2d}" for nums in gugudan]
            print("   ".join(line))
        break
    else:
        print("INPUT ERROR!")

##########################################################################(방법01)

while True:
    s, e = map(int, input().split())

    if 2 <= s <= 9 and 2 <= e <= 9:
        break
    else:
        print("INPUT ERROR!")

step = 1 if s <= e else -1

for i in range(1, 10):
    row = []
    for dan in range(s, e + step, step):
        row.append(f"{dan} * {i} = {dan * i:2d}")
    print("   ".join(row))

##########################################################################(방법02)

