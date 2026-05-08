def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        rank = 1
        for j in range(len(emergency)):
            if emergency[j] > emergency[i]:
                rank += 1
        answer.append(rank)
    return answer

####################################################(방법01)

def solution(emergency):
    answer = []
    sorted_list = emergency[:] 
    n = len(sorted_list)
    for i in range(n):
        for j in range(n - 1 - i):
            if sorted_list[j] < sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    
    for x in emergency:
        for i in range(len(sorted_list)):
            if x == sorted_list[i]:
                answer.append(i + 1) 
    return answer

####################################################(방법02)

def solution(emergency):
    sorted_list = []
    temp = emergency[:]
    while temp:
        max_val = temp[0]
        for val in temp:
            if val > max_val:
                max_val = val
        sorted_list.append(max_val)
        temp.remove(max_val)
        
    rank_map = {}
    for i in range(len(sorted_list)):
        rank_map[sorted_list[i]] = i + 1
        
    return [rank_map[x] for x in emergency]

####################################################(방법03)

def solution(emergency):
    n = len(emergency)
    answer = [n] * n 
    
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if emergency[i] > emergency[j]:
                answer[i] -= 1
                
    return answer

####################################################(방법04)

def solution(emergency):    # 재귀함수 활용
    answer = [0] * len(emergency)
    
    def assign_rank(current_rank, temp_list):
        if current_rank > len(emergency):
            return
        
        max_idx = -1
        max_val = -1
        for i in range(len(emergency)):
            if answer[i] == 0: 
                if emergency[i] > max_val:
                    max_val = emergency[i]
                    max_idx = i
        
        answer[max_idx] = current_rank
        assign_rank(current_rank + 1, temp_list)

    assign_rank(1, emergency)
    return answer

####################################################(방법05)














