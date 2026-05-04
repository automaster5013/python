for i in range(3, 0, -1):
    print('*' * i)

for i in range(2, 4):
    print('*' * i)

#################################################(방법01)

for i in range(1, 6):
    count = abs(i - 3) + 1
    print('*' * count)

#################################################(방법02)

counts = [3, 2, 1, 2, 3]

for c in counts:
    print('*' * c)

#################################################(방법03)

star_count = 3
step = -1 

for x in range(5):
    print('*' * star_count)
    
    if star_count == 1:
        step = 1
        
    star_count += step

#################################################(방법04)

N = 3

for i in range(N):
    for j in range(N - i, 0, -1):
        print('*', end='')
    print()

for i in range(1, N):
    for j in range(i + 1):
        print('*', end='')
    print() 

#################################################(방법05)

