def solution(i, j, k):
    answer = 0
    alpha = str(k) 
    for num in range(i, j + 1):
        answer += str(num).count(alpha)
    return answer

##################################################################

def solution(i, j, k):
    alpha = str(k)
    counts = [str(num).count(alpha) for num in range(i, j + 1)]
    return sum(counts)

##################################################################

def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        temp = num
        while True:
            if temp % 10 == k: 
                answer += 1
            temp //= 10 
            if temp == 0: break
            
    return answer

##################################################################

















































