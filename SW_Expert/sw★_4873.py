def solution():
    t_input = input().strip()
    if not t_input: return
    T = int(t_input)
    
    for t in range(1, T + 1):
        s = input().strip()
        
        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  
            else:
                stack.append(char)  
        
        print(f"#{t} {len(stack)}")

solution()

#############################################(방법01)

def solution():
    T = int(input().strip())
    for t in range(1, T + 1):
        s = list(input().strip())
        top = -1  
        
        for i in range(len(s)):
            if top >= 0 and s[top] == s[i]:
                top -= 1
            else:
                top += 1
                s[top] = s[i]
                
        print(f"#{t} {top + 1}")

solution()

#############################################(방법02)

















