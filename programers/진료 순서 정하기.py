def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        # 내 순위는 기본 1등에서 시작
        rank = 1
        for j in range(len(emergency)):
            # 나보다 응급도가 높은 사람을 발견하면 내 순위는 하나씩 밀려남
            if emergency[j] > emergency[i]:
                rank += 1
        answer.append(rank)
    return answer

####################################################(방법01)

def solution(emergency):
    answer = []
    # 1. 내림차순으로 정렬된 새로운 리스트 생성 (버블 정렬 활용)
    sorted_list = emergency[:] # 원본 복사
    n = len(sorted_list)
    for i in range(n):
        for j in range(n - 1 - i):
            if sorted_list[j] < sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    
    # 2. 원본 값이 정렬된 리스트에서 몇 번째(index)에 있는지 확인
    for x in emergency:
        for i in range(len(sorted_list)):
            if x == sorted_list[i]:
                answer.append(i + 1) # 인덱스는 0부터 시작하므로 +1
    return answer

####################################################(방법02)

def solution(emergency):
    # 내림차순 정렬 (슬라이싱과 sorted를 쓰지 않는 창의적 정렬)
    sorted_list = []
    temp = emergency[:]
    while temp:
        max_val = temp[0]
        for val in temp:
            if val > max_val:
                max_val = val
        sorted_list.append(max_val)
        temp.remove(max_val)
        
    # {응급도: 순위} 형태의 딕셔너리 생성
    rank_map = {}
    for i in range(len(sorted_list)):
        rank_map[sorted_list[i]] = i + 1
        
    # 원본 순서대로 딕셔너리에서 순위 추출
    return [rank_map[x] for x in emergency]

####################################################(방법03)

def solution(emergency):
    n = len(emergency)
    answer = [n] * n # 일단 모두를 꼴등으로 설정
    
    for i in range(n):
        for j in range(n):
            if i == j: continue
            # 내가 상대방보다 크다면, 내 등수는 1만큼 앞당겨짐(숫자가 작아짐)
            if emergency[i] > emergency[j]:
                answer[i] -= 1
                
    return answer

####################################################(방법04)

def solution(emergency):
    answer = [0] * len(emergency)
    
    def assign_rank(current_rank, temp_list):
        if current_rank > len(emergency):
            return
        
        # 아직 순위가 결정되지 않은 값들 중 최댓값 찾기
        max_idx = -1
        max_val = -1
        for i in range(len(emergency)):
            if answer[i] == 0: # 아직 순위가 안 정해진 경우
                if emergency[i] > max_val:
                    max_val = emergency[i]
                    max_idx = i
        
        answer[max_idx] = current_rank
        assign_rank(current_rank + 1, temp_list)

    assign_rank(1, emergency)
    return answer

####################################################(방법05)














