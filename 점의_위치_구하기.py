def solution(dot):
    x, y = dot[0], dot[1]
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3

dot1 = [2, 4]
dot2 = [-7, 9]

print(solution(dot1))
print(solution(dot2))

############################################

def solution(dot):
    x, y = dot[0], dot[1]
    if x > 0 and y > 0:   return 1
    elif x < 0 and y > 0: return 2
    elif x < 0 and y < 0: return 3
    elif x > 0 and y < 0: return 4


dot1 = [2, 4]
dot2 = [-7, 9]

print(solution(dot1))
print(solution(dot2))

############################################

def solution(dot):
    x, y = dot[0], dot[1]
    matrix = [
        [3, 2], 
        [4, 1]  
    ]
    
    return matrix[x > 0][y > 0]

dot1 = [2, 4]
dot2 = [-7, 9]

print(solution(dot1))
print(solution(dot2))

############################################



























































