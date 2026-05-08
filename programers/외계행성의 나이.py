def solution(age):
    answer = ''
    # 0부터 9까지 매칭되는 알파벳 문자열
    alphabet = "abcdefghij"
    
    # 숫자를 문자열로 바꾸어 한 글자씩 순회
    for digit in str(age):
        # 숫자를 인덱스로 사용하여 알파벳 추출
        answer += alphabet[int(digit)]
        
    return answer

################################################(방법01)

def solution(age):
    answer = ''
    for digit in str(age):
        # 'a'의 아스키 코드(97)에 숫자를 더함
        # chr() 함수는 코드 번호를 문자로 바꿔줍니다.
        answer += chr(ord('a') + int(digit))
    return answer

################################################(방법02)

def solution(age):
    # 숫자와 알파벳 매핑 테이블 생성
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
    answer = ""
    alphabet = "abcdefghij"
    
    # 숫자가 0이 될 때까지 반복
    if age == 0: return "a" # age가 0인 경우 예외 처리
    
    while age > 0:
        # 마지막 자릿수를 구함 (예: 23 % 10 = 3)
        digit = age % 10
        # 앞에 붙여넣기 (순서 주의)
        answer = alphabet[digit] + answer
        # 마지막 자릿수 제거 (예: 23 // 10 = 2)
        age //= 10
        
    return answer

################################################(방법04)

def solution(age):
    # 1. 숫자를 문자열로 변환 후 리스트로 쪼개기
    # 2. 각 숫자를 알파벳으로 변환
    # 3. "".join()으로 리스트를 다시 문자열로 합치기
    return "".join(["abcdefghij"[int(i)] for i in str(age)])

################################################(방법05)

