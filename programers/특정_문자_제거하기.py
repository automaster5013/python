def solution(my_string, letter):
    return my_string.replace(letter, "")


my_string1 = "abcdef"
letter1 = "f"

my_string2 = "BCBdbe"
letter2 = "B"

print(solution(my_string1, letter1))
print(solution(my_string2, letter2))

#####################################################################

def solution(my_string, letter):
    return "".join([char for char in my_string if char != letter])


my_string1 = "abcdef"
letter1 = "f"

my_string2 = "BCBdbe"
letter2 = "B"

print(solution(my_string1, letter1))
print(solution(my_string2, letter2))

#####################################################################

def solution(my_string, letter):
    answer = ''
    for char in my_string:
        if char != letter:
            answer += char
            
    return answer


my_string1 = "abcdef"
letter1 = "f"

my_string2 = "BCBdbe"
letter2 = "B"

print(solution(my_string1, letter1))
print(solution(my_string2, letter2))

#####################################################################

def solution(my_string, letter):
    posting = my_string.split(letter)
    
    return "".join(posting)


my_string1 = "abcdef"
letter1 = "f"

my_string2 = "BCBdbe"
letter2 = "B"

print(solution(my_string1, letter1))
print(solution(my_string2, letter2))

#####################################################################

# function solution(my_string, letter) {
#     return [...my_string].filter(char => char !== letter).join('');
# } 
# 자바스크립트

#####################################################################




























