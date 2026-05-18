def solution(before, after):
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0


print(solution("olleh", "hello"))

print(solution("allpe", "apple"))

##################################################

def solution(before, after):
    unique_chars = set(before)

    for char in unique_chars:
        if before.count(char) != after.count(char):
            return 0

    return 1


print(solution("olleh", "hello"))

print(solution("allpe", "apple"))




































