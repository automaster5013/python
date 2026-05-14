def solution():
    t_str = input().strip()
    if not t_str: return
    T = int(t_str)
    
    for t in range(1, T + 1):
        str1 = input().strip()
        str2 = input().strip()
        n, m = len(str1), len(str2)
        
        found = 0
        for i in range(m - n + 1):
            if str2[i : i + n] == str1:
                found = 1
                break
        print(f"#{t} {found}")

solution()

################################################(방법01)

def solution():
    T = int(input().strip())
    for t in range(1, T + 1):
        s1, s2 = input().strip(), input().strip()
        n, m = len(s1), len(s2)
        ans = 0
        
        for i in range(m - n + 1):
            if s2[i] == s1[0]:
                if s2[i : i + n] == s1:
                    ans = 1
                    break
        print(f"#{t} {ans}")

solution()

################################################(방법02)

def solution():
    T = int(input().strip())
    for t in range(1, T + 1):
        s1, s2 = input().strip(), input().strip()
        
        parts = s2.split(s1)
        
        result = 1 if len(parts) > 1 else 0
        print(f"#{t} {result}")

solution()

################################################(방법03)

def solution():
    T = int(input().strip())
    for t in range(1, T + 1):
        s1, s2 = input().strip(), input().strip()
        n, m = len(s1), len(s2)
        ans = 0

        for i in range(m - n +1):
            match_count = 0
            for j in range(n):
                if s2[i + j] == s1[j]:
                    match_count += 1
                else:
                    break

            if match_count == n:
                ans = 1
                break
        print(f"#{t} {ans}")

solution()

################################################(방법04)

def solution():
    try:
        line = input().strip()
        if not line: return
        T = int(line)
        for t in range(1, T + 1):
            s1 = input().strip()
            s2 = input().strip()
            
            ans = 1 if s1 in s2 else 0
            print(f"#{t} {ans}")
    except EOFError: 
        pass

solution()

################################################(방법05)

