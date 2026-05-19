def solution(array):
    answer = 0
    for num in array:
        answer += str(num).count('7')
    return answer


array1 = [7, 77, 17]
array2 = [10, 29]

print(solution(array1))
print(solution(array2))

# #####################################################################

def solution(array):
    combined_str = "".join(map(str, array))
    return combined_str.count('7')

array1 = [7, 77, 17]
array2 = [10, 29]

print(solution(array1))
print(solution(array2))

# #####################################################################

def solution(array):
    all_chars = [char for num in array for char in str(num)]
    
    return all_chars.count('7')

array1 = [7, 77, 17]
array2 = [10, 29]

print(solution(array1))
print(solution(array2))

#####################################################################

def solution(array):
    full_str = "".join(map(str, array))
    
    removed_str = full_str.replace('7', '')
    
    return len(full_str) - len(removed_str)


array1 = [7, 77, 17]
array2 = [10, 29]

print(solution(array1))
print(solution(array2))














