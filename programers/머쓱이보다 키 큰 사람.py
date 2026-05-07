def solution(array, height):
    answer = 0
    for h in array:
        if h > height:
            answer += 1
    return answer

###########################################(방법01)

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

###########################################(방법02)

def solution(array, height):
    return sum(1 for a in array if a > height)

###########################################(방법03)

def solution(array, height):
    return len([i for i in array if i>height])

###########################################(방법04)

# function solution(array, height) {
#     return array.filter(v => v > height).length;
# }
# 자바스크립트
###########################################(방법05)

