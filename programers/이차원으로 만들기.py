def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i : i + n])
    return answer

#####################################################################(방법01)

def solution(num_list, n):
    return [num_list[i : i + n] for i in range(0, len(num_list), n)]

#####################################################################(방법02)
































