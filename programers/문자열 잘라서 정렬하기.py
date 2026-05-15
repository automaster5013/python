def solution(myString):
    words = myString.split('x')
    return sorted([s for s in words if s != ""])

# print(solution("axbxcxdx"))
# print(solution("dxccxbbbxaaaa"))

#########################################################

def solution(myString):
    words = myString.replace('x', ' ').split()
    return sorted(words)

# print(solution("axbxcxdx"))
# print(solution("dxccxbbbxaaaa"))

#########################################################


































