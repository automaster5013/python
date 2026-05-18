def solution(s):
    unique_chars = sorted([char for char in s if s.count(char) == 1])
    
    return "".join(unique_chars)

s1 = "abcabcadc"
s2 = "abcd"
s3 = "hello"

print(solution(s1))
print(solution(s2))
print(solution(s3))

###########################################################

def solution(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    result = []
    for char, count in char_counts.items():
        if count == 1:
            result.append(char)
            
    result.sort()
    return "".join(result)
 

s1 = "abcabcadc"
s2 = "abcd"
s3 = "hello"

print(solution(s1))
print(solution(s2))
print(solution(s3))

##########################################################

def solution(s):
    answer = []
    
    for char in set(s):
        if s.count(char) == 1:
            answer.append(char)
            
    return "".join(sorted(answer))

s1 = "abcabcadc"
s2 = "abdc"
s3 = "hello"

print(solution(s1))
print(solution(s2))
print(solution(s3))











