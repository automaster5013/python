def solution(array):
    nums = list(set(array))
    
    counts = [array.count(k) for k in nums]
    max_val = max(counts)
    
    if counts.count(max_val) > 1:
        return -1
    
    return nums[counts.index(max_val)]

##################################################

def solution(array):
    nums = 0
    max_val = 0
    for i in set(array):
        if array.count(i) > nums:
            nums = array.count(i)
            max_val = i
        elif array.count(i) == nums:
            max_val = -1
    return max_val

##################################################

def solution(array):
    count = {}
    for num in array:
        count[num] = count.get(num, 0) + 1
    
    max_count = max(count.values())
    candidates = [num for num, cnt in count.items() if cnt == max_count]
    
    return candidates[0] if len(candidates) == 1 else -1

##################################################











































