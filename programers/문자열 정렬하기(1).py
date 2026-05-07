def solution(my_string):
    numbers = []
    for char in my_string:
        if '0' <= char <= '9':  # 65(A) ~ 97(a)
            numbers.append(int(char))
    
    n = len(numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

########################################################################(방법01)

def solution(my_string):
    counts = [0] * 10
    for char in my_string:
        if '0' <= char <= '9':
            counts[int(char)] += 1
            
    result = []
    for num in range(10):
        for _ in range(counts[num]):
            result.append(num)
    return result

########################################################################(방법02)

# function solution(my_string) {
#     return my_string.match(/\d/g).map(Number).sort((a, b) => a - b);
# }
# 자바스크립트
########################################################################(방법03)

