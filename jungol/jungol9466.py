def print_line(n):
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end=' ')
            num += 1
        print() 

N = int(input())
print_line(N)

########################################(방법01)

def print_line(n):
    for i in range(n):
        row = range(i * n + 1, (i + 1) * n + 1)
        print(*row)

N = int(input())
print_line(N)

#######################################(방법02)

def print_line(n):
    for i in range(1, n * n + 1):
        print(i, end=' ')
        if i % n == 0:
            print()

N = int(input())
print_line(N)

#######################################(방법03)

def print_line(n):
    for i in range(n):
        row_str = " ".join(map(str, range(i * n + 1, (i + 1) * n + 1)))
        print(row_str)

N = int(input())
print_line(N)

#######################################(방법04)



















































