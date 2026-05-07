def solution(numbers):
    # 영단어와 숫자를 매칭한 딕셔너리
    data = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    # 딕셔너리를 돌며 문자열 내의 단어를 숫자로 교체
    for word, digit in data.items():
        numbers = numbers.replace(word, digit)
    
    # 마지막에 정수(int)로 변환하여 반환
    return int(numbers)

############################################################################(방법01)

def solution(numbers):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result_str = ""
    current_word = ""
    
    for char in numbers:
        current_word += char
        # 지금까지 쌓인 단어가 words 리스트 안에 있는지 확인
        for i in range(len(words)):
            if current_word == words[i]:
                result_str += str(i)
                current_word = "" # 단어를 찾았으니 초기화
                break
                
    return int(result_str)

############################################################################(방법02)

def solution(numbers):
    res = ""
    i = 0
    while i < len(numbers):
        char = numbers[i]
        # 첫 글자에 따라 건너뛸 길이를 결정
        if char == 'z': res += '0'; i += 4 # zero
        elif char == 'o': res += '1'; i += 3 # one
        elif char == 't':
            if numbers[i+1] == 'w': res += '2'; i += 3 # two
            else: res += '3'; i += 5 # three
        elif char == 'f':
            if numbers[i+1] == 'o': res += '4'; i += 4 # four
            else: res += '5'; i += 4 # five
        elif char == 's':
            if numbers[i+1] == 'i': res += '6'; i += 3 # six
            else: res += '7'; i += 5 # seven
        elif char == 'e': res += '8'; i += 5 # eight
        elif char == 'n': res += '9'; i += 4 # nine
            
    return int(res)

############################################################################(방법03)

def solution(numbers):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, word in enumerate(words):
        # 단어를 해당 인덱스(숫자) 문자열로 강제 분리 후 재결합
        if word in numbers:
            # 직접 split과 join을 구현하는 효과
            temp_list = numbers.split(word)
            numbers = str(i).join(temp_list)
            
    return int(numbers)

############################################################################(방법04)

def solution(numbers):
    word_map = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    answer = 0
    current = ""
    
    for char in numbers:
        current += char
        if current in word_map:
            # 자릿수 올림: 기존 값에 10을 곱하고 새로 찾은 숫자를 더함
            answer = (answer * 10) + word_map[current]
            current = ""
            
    return answer

############################################################################(방법05)

# function solution(numbers) {
#     const Num_str = {
#         one: 1,
#         two: 2,
#         three: 3,
#         four: 4,
#         five: 5,
#         six: 6,
#         seven: 7,
#         eight: 8,
#         nine: 9,
#         zero: 0,
#     };

#     for (let word in Num_str) {
#     numbers = numbers.replaceAll(word, Num_str[word]);
# }

#     return Number(numbers);
# }

# 자바스크립트

############################################################################(방법06)

