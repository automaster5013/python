def solution(numbers):
    return sum(numbers) / len(numbers)


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print(solution(numbers1))
print(solution(numbers2))

###########################################################

def solution(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num  
        count += 1    
        
    return total / count


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print(solution(numbers1))
print(solution(numbers2))

###########################################################

def solution(numbers):
    arr = numbers[:]
    total = 0
    origin_length = len(arr)
    while arr:
        total += arr.pop()
        
    return total / origin_length


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print(solution(numbers1))
print(solution(numbers2))

###########################################################

def solution(numbers):
    def get_sum(arr):
        if not arr:
            return 0
        return arr[0] + get_sum(arr[1:])

    total_sum = get_sum(numbers)
    return total_sum / len(numbers)

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print(solution(numbers1))
print(solution(numbers2))


























