def solution(my_string):
    if not any(c.isdigit() for c in my_string):
        return 0
    
    start = -1
    for i, c in enumerate(my_string):
        if c.isdigit():
            start = i
            break
            
    end = start
    while end < len(my_string) and my_string[end].isdigit():
        end += 1
        
    return int(my_string[start:end]) + solution(my_string[end:])

# print(solution("aAb1B2cC34oOp"))
# print(solution("1a2b3c4d123Z"))
 
######################################################################

# function solution(my_string) {
#     const numbers = my_string.match(/\d+/g);

#     if (!numbers) {
#         return 0;
#     } else {
#         return numbers.reduce((acc, curr) => acc + Number(curr), 0);
#     }
# }

# 자바스크립트
 
######################################################################






























































