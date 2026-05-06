n_raw = input().split()
# print(n_raw)
if n_raw and n_raw[0].isdigit():
    n = int(n_raw[0])
    if 1 <= n <= 50 and n % 2 == 1:
        num = 1
        for i in range(1, n + 1):
            if i % 2 != 0:
                for _ in range(i):
                    print(num, end=" ")
                    num += 1
            else:
                start_val = num
                for j in range(start_val + i - 1, start_val - 1, -1):
                    print(j, end=" ")
                num += i 
            print()
    else:
        print("INPUT ERROR!")
else:
    print("INPUT ERROR!")

#####################################################################(방법01)

try:
    n = int(input())
    # print(n)
    if 1 <= n <= 50 and n % 2 == 1:
        curr = 1
        for i in range(1, n + 1):
            row = [curr + j for j in range(i)]
            curr += i
            
            display = row if i % 2 != 0 else row[::-1]
            print(" ".join(map(str, display)))
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

#####################################################################(방법02)

try:
    data = input().split()
    # print(data)
    if not data: exit()
    n = int(data[0])

    if 1 <= n <= 50 and n % 2 == 1:
        current_num = 1
        for i in range(1, n + 1):
            row = []
            for x in range(i):
                row.append(current_num)
                current_num += 1
            
            if i % 2 == 0:
                row.reverse()
            
            print(*(row))
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

#####################################################################(방법03)

