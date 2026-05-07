def solution(my_str, n):
    result = []
    for i in range(0, len(my_str), n):
        result.append(my_str[i : i + n])
    return result

#################################################(방법01)

def solution(my_str, n):
    result = []
    total_length = len(my_str)
    num_chunks = (total_length + n - 1) // n
    
    for i in range(num_chunks):
        chunk = ""
        for j in range(i * n, (i + 1) * n):
            if j < total_length: 
                chunk += my_str[j]
        result.append(chunk)
    return result

#################################################(방법02)

def solution(my_str, n):
    result = []
    temp = ""
    for char in my_str:
        temp += char
        if len(temp) == n:
            result.append(temp)
            temp = ""
    
    if temp:
        result.append(temp)
    return result

#################################################(방법03)

def solution(my_str, n):
    result = []
    target = my_str
    while len(target) > 0:
        result.append(target[:n])
        target = target[n:]
    return result

#################################################(방법04)

def solution(my_str, n):
    return [my_str[i : i + n] for i in range(0, len(my_str), n)]

#################################################(방법05)


