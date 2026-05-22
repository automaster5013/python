def solution(array):
    max_val = max(array)
    max_idx = array.index(max_val)
    
    return [max_val, max_idx]


array1 = [1, 8, 3] 
array2 = [9, 10, 11, 8] 

print(solution(array1))
print(solution(array2))

################################################

def solution(array):
    max_val = array[0]
    max_idx = 0
    
    for i in range(1, len(array)):
        if array[i] > max_val:
            max_val = array[i]  
            max_idx = i         
            
    return [max_val, max_idx]


array1 = [1, 8, 3] 
array2 = [9, 10, 11, 8] 

print(solution(array1))
print(solution(array2))

################################################

def solution(array):
    answer = [-1, -1]
    for idx, num in enumerate(array):
        if num > answer[0]:
            answer = [num, idx] 
            
    return answer


array1 = [1, 8, 3] 
array2 = [9, 10, 11, 8] 

print(solution(array1))
print(solution(array2))

################################################






