def solution(numbers):
    answer = [n * 2 for n in numbers]
    return answer

#############################################(방법01)

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(n << 1)
    return answer

#############################################(방법02)

def solution(numbers):
        answer = [0] * len(numbers)
        for i in range(len(numbers)):
            answer[i] = numbers[i] * 2
        return answer

#############################################(방법03)

def solution(numbers):
    answer = list(map(lambda x: x * 2, numbers))
    return answer

#############################################(방법04)


