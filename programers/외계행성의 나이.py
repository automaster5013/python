def solution(age):
    answer = ''
    alphabet = "abcdefghij"
    
    for digit in str(age):
        answer += alphabet[int(digit)]
        
    return answer

################################################(방법01)

def solution(age):
    answer = ''
    for digit in str(age):
        answer += chr(ord('a') + int(digit))
    return answer

################################################(방법02)

def solution(age):
    mapping = {
        '0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e',
        '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'
    }

    answer = ''
    for digit in str(age):
        answer += mapping[digit]
    return answer

################################################(방법03)

def solution(age):
    return "".join(["abcdefghij"[int(i)] for i in str(age)])

################################################(방법04)

