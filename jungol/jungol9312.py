for i in range(1, 10):
    for j in range(5, 8):
        if j < 7:
            print(f"{j} * {i} = {j * i}", end="   ")
        else:
            print(f"{j} * {i} = {j * i}", end="")

    print()

#############################################################################(방법01)

for i in range(1, 10):
    row = [f"{j} * {i} = {j * i}" for j in range(5, 8)]
    
    print("   ".join(row))

#############################################################################(방법02)

for i in range(1, 10):
    line = map(lambda j: f"{j} * {i} = {j * i}", [5, 6, 7])
    print("   ".join(line))

#############################################################################(방법03)

for i in range(1, 10):
    for dan in range(5, 8):
        print(f"{dan} * {i} = {dan * i}", end="   ")
    print()

#############################################################################(방법04)

for i in range(1, 10):
    row = [f"{dan} * {i} = {dan * i}" for dan in range(5, 8)]
    print(*row, sep="   ")

#############################################################################(방법05)

for i in range(1, 10):
    line = "   ".join([f"{dan} * {i} = {dan * i}" for dan in range(5, 8)])
    print(line)

#############################################################################(방법06)

i = 1
while i <= 9:
    j = 5
    while j <= 7:
        res = f"{j} * {i} = {j * i}"
        print(res, end="")
        
        if j < 7:
            print("   ", end="")
        
        j += 1
    print()
    i += 1

#############################################################################(방법07)

def get_gugudan_row(multiplier, start_dan, end_dan):
    row_items = []
    for dan in range(start_dan, end_dan + 1):
        row_items.append(f"{dan} * {multiplier} = {dan * multiplier}")
    
    return "   ".join(row_items)

for i in range(1, 10):
    print(get_gugudan_row(i, 5, 7))

#############################################################################(방법08)

class GugudanTable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_table(self):
        for i in range(1, 10):
            row = [f"{j} * {i} = {j * i}" for j in range(self.start, self.end + 1)]
            print("   ".join(row))

table = GugudanTable(5, 7)
table.print_table()

#############################################################################(방법09)

for i in range(1, 10):         # 이중 반복문( -> 2중 for문)
    for j in range(5, 8):
        print(f"{j} * {i} = {j * i}"   , end='')
    print()

#############################################################################(방법10)

def mul(a, b, c):
    for i in range(1, 10):
        print(f"{a} * {i} = {a * i}   {b} * {i} = {b * i}   {c} * {i} = {c * i}")
  
mul(5, 6, 7)

#############################################################################(방법11)

