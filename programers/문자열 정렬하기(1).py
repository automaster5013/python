def solution(my_string):
    numbers = []
    for char in my_string:
        if '0' <= char <= '9':  # 65(A) ~ 97(a)
            numbers.append(int(char))
    
    n = len(numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

########################################################################(방법01)

def solution(my_string):
    counts = [0] * 10
    for char in my_string:
        if '0' <= char <= '9':
            counts[int(char)] += 1
            
    result = []
    for num in range(10):
        for _ in range(counts[num]):
            result.append(num)
    return result

########################################################################(방법02)

# function solution(my_string) {
#     return my_string.match(/\d/g).map(Number).sort((a, b) => a - b);
# }
# 자바스크립트

########################################################################(방법03)

def solution_1(my_string):
    # 1. 숫자만 추출하기
    numbers = []
    for char in my_string:
        if '0' <= char <= '9':  # 아스키 코드 범위를 이용한 숫자 판별
            numbers.append(int(char))
    
    # 2. 버블 정렬 (가장 큰 값을 뒤로 보내기)
    n = len(numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

########################################################################(방법04)

def solution_2(my_string):
    # 0~9까지 숫자의 등장 횟수를 저장할 리스트 (인덱스가 곧 숫자)
    counts = [0] * 10
    
    for char in my_string:
        if '0' <= char <= '9':
            counts[int(char)] += 1
            
    # 등장한 횟수만큼 순서대로 결과 리스트에 담기
    result = []
    for num in range(10):
        for _ in range(counts[num]):
            result.append(num)
    return result

########################################################################(방법05)

def solution_3(my_string):
    result = []
    # 숫자의 기준이 되는 문자열을 정의
    digits = "0123456789"
    
    # 0부터 9까지 순서대로 my_string에 몇 개 있는지 확인
    for d in digits:
        for char in my_string:
            if char == d:
                result.append(int(d))
    return result

########################################################################(방법06)

def solution_4(my_string):
    # 리스트로 변환 및 숫자 필터링
    nums = [int(x) for x in my_string if '0' <= x <= '9']
    
    def get_sorted(arr):
        if not arr:
            return []
        # 현재 리스트에서 최소값 찾기
        min_val = arr[0]
        for x in arr:
            if x < min_val:
                min_val = x
        
        # 최소값을 제외한 나머지 리스트 생성 (중복 제거 주의)
        arr.remove(min_val)
        return [min_val] + get_sorted(arr)
        
    return get_sorted(nums)

########################################################################(방법07)

def solution_5(my_string):
    # 알파벳 소문자들을 모두 제거하기 위한 준비
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    temp_str = my_string
    for a in alphabet:
        temp_str = temp_str.replace(a, "")
    
    # 숫자로 변환
    nums = [int(n) for n in temp_str]
    
    # 선택 정렬로 마무리
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

########################################################################(방법08)


