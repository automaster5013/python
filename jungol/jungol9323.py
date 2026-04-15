S = int(input())
E = int(input())
# print(S, E)
step = 1 if S <= E else -1

for i in range(1, 10):
    for j in range(S, E + step, step):
        if j == E:
            print(f"{j} * {i} = {j * i}", end="")
        else:
            print(f"{j} * {i} = {j * i}", end="   ")
    print()

###############################################################################(방법01)

S = int(input())
E = int(input())
# print(S, E)
step = 1 if S <= E else -1
gugu = range(S, E + step, step)

for i in range(1, 10):
    line = [f"{dan} * {i} = {dan * i}" for dan in gugu]
    print("   ".join(line))

###############################################################################(방법02)

S, E = int(input()), int(input())
# print(S, E)
for i in range(1, 10):
    curr_dan = S
    while True:
        print(f"{curr_dan} * {i} = {curr_dan * i}", end="")
        if curr_dan == E:
            break
        print("   ", end="")
        
        if S <= E: curr_dan += 1
        else: curr_dan -= 1
    print()

###############################################################################(방법03)

S = int(input())
E = int(input())
# print(S, E)
i = 1
while i <= 9:
    j = S
    while True:
        print(f"{j} * {i} = {j * i}", end="")
        
        if j == E:
            break
        
        print("   ", end="")
        if S < E: j += 1
        else: j -= 1
        
    print()
    i += 1

###############################################################################(방법04)

def gugudan_printer(multiplier, start, end):
    line_parts = []
    step = 1 if start <= end else -1
    
    for dan in range(start, end + step, step):
        line_parts.append(f"{dan} * {multiplier} = {dan * multiplier}")
    
    return "   ".join(line_parts)

s_val, e_val = int(input()), int(input())
for i in range(1, 10):
    print(gugudan_printer(i, s_val, e_val))

###############################################################################(방법05)

class GugudanPrinter:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.step = 1 if s <= e else -1

    def display(self):
        for i in range(1, 10):
            row = []
            for dan in range(self.s, self.e + self.step, self.step):
                row.append(f"{dan} * {i} = {dan * i}")
            print("   ".join(row))

s_in, e_in = int(input()), int(input())
gugudan = GugudanPrinter(s_in, e_in)
gugudan.display()

###############################################################################(방법06)

S = int(input())
E = int(input())
# print(S, E)
step = 1
if S < E:
    step = 1
else:
    step = -1

for i in range(1, 10):
    for j in range(S, E + step, step):
        print(f"{j} * {i} = {j * i}   ", end='')
    print()

###############################################################################(방법07)


