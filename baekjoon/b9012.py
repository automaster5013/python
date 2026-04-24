t = int(input())
# print(t)
for x in range(t):
    ps = input()
    count = 0
    
    for char in ps:
        if char == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            break
            
    if count == 0:
        print("YES")
    else:
        print("NO")

############################################(방법01)

t = int(input())
# print(t)
for x in range(t):
    ps = input()
    stack = []
    isVPS = True
    
    for char in ps:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                isVPS = False
                break
            stack.pop()
    
    if isVPS and len(stack) == 0:
        print("YES")
    else:
        print("NO")

############################################(방법02)








































t = int(input())
# print(t)
for x in range(t):
    ps = input()

    while True:
        index = ps.find("()")
        if index == -1:
            break
        ps = ps[:index] + ps[index+2:]
        
    if ps == "":
        print("YES")
    else:
        print("NO")

############################################(방법03)








