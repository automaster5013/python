def solution(array, n):
    array.sort() 
    
    diffs = [abs(x - n) for x in array]
    
    min_val = min(diffs)
    target_idx = diffs.index(min_val)
    
    return array[target_idx]

# n1 = 20
# n2 = 13

# print(solution([3,10,28], n1))
# print(solution([10,11,12], n2))

#################################################

def solution(array, n):

    temp = []
    for x in array:
        temp.append([abs(x - n), x])

    temp.sort()

    return temp[0][1]

# n1 = 20
# n2 = 13

# print(solution([3,10,28], n1))
# print(solution([10,11,12], n2))








































