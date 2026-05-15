def solution(n):
    answer = []
    num = 1
    while num <= n:
        answer.append(num)
        num += 2 
    return answer

# n1 = 10
# n2 = 15

# print(solution(n1))
# print(solution(n2))

######################################################

def solution(n):
    return [i for i in range(1, n + 1) if i % 2 == 1]

######################################################











































