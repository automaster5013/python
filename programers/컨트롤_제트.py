def solution(s):
    stack = []
    for char in s.split():
        if char == "Z":
            if stack:
                stack.pop()
        else:
            stack.append(int(char))
            
    return sum(stack)


s1 = "1 2 Z 3"
s2 = "10 20 30 40"
s3 = "10 Z 20 Z 1"
s4 = "10 Z 20 Z"
s5 = "-1 -2 -3 Z"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))

################################################

def solution(s):
    answer = 0
    words = s.split()
    
    for i in range(len(words)):
        if words[i] == "Z":
            answer -= int(words[i-1])
        else:
            answer += int(words[i])
            
    return answer

s1 = "1 2 Z 3"
s2 = "10 20 30 40"
s3 = "10 Z 20 Z 1"
s4 = "10 Z 20 Z"
s5 = "-1 -2 -3 Z"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))










