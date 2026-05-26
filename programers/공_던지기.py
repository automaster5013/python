    # (k - 1)번 던지는 동안 총 (k - 1) * 2 만큼 인덱스가 이동함
    # 원형 배열이므로 전체 길이로 나눈 나머지가 최종 인덱스가 됨
def solution(numbers, k):
    target_idx = ((k - 1) * 2) % len(numbers)
    return numbers[target_idx]

numbers1, k1 = [1,2,3,4], 2
numbers2, k2 = [1,2,3,4,5,6], 5
numbers3, k3 = [1,2,3], 3

print(solution(numbers1, k1))
print(solution(numbers2, k2))
print(solution(numbers3, k3))

######################################################

def solution(numbers, k):
    idx = 0
    n = len(numbers)
    for x in range(k - 1):
        idx = (idx + 2) % n
        
    return numbers[idx]


numbers1, k1 = [1,2,3,4], 2
numbers2, k2 = [1,2,3,4,5,6], 5
numbers3, k3 = [1,2,3], 3

print(solution(numbers1, k1))
print(solution(numbers2, k2))
print(solution(numbers3, k3))

######################################################

def solution(numbers, k):
    idx = 0
    n = len(numbers)
    throws = 0
    while throws < k - 1:
        idx += 2
        if idx >= n:
            idx -= n 
        throws += 1
        
    return numbers[idx]


numbers1, k1 = [1,2,3,4], 2
numbers2, k2 = [1,2,3,4,5,6], 5
numbers3, k3 = [1,2,3], 3

print(solution(numbers1, k1))
print(solution(numbers2, k2))
print(solution(numbers3, k3))

######################################################

