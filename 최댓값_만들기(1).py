def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [0, 31, 24, 10, 1, 9]

print(solution(numbers1))
print(solution(numbers2))

##############################################

def solution(numbers):
    max1, max2 = 0, 0
    for num in numbers:
        if num > max1:
            max2 = max1 
            max1 = num  
        elif num > max2:
            max2 = num 
            
    return max1 * max2


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [0, 31, 24, 10, 1, 9]

print(solution(numbers1))
print(solution(numbers2))

##############################################

def solution(numbers):
    max_price = 0
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            current_price = numbers[i] * numbers[j]
            if current_price > max_price:
                max_price = current_price
                
    return max_price


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [0, 31, 24, 10, 1, 9]

print(solution(numbers1))
print(solution(numbers2))

##############################################




























