def solution(my_str, n):
    result = []
    for i in range(0, len(my_str), n):
        result.append(my_str[i : i + n])
    return result

#################################################(방법01)

def solution(my_str, n):
    result = []
    total_length = len(my_str)
    num_chunks = (total_length + n - 1) // n
    
    for i in range(num_chunks):
        chunk = ""
        for j in range(i * n, (i + 1) * n):
            if j < total_length: 
                chunk += my_str[j]
        result.append(chunk)
    return result

#################################################(방법02)

def solution(my_str, n):
    result = []
    temp = ""
    for char in my_str:
        temp += char
        if len(temp) == n:
            result.append(temp)
            temp = ""
    
    if temp:
        result.append(temp)
    return result

#################################################(방법03)

def solution(my_str, n):
    result = []
    target = my_str
    while len(target) > 0:
        result.append(target[:n])
        target = target[n:]
    return result

#################################################(방법04)

def solution(my_str, n):
    return [my_str[i : i + n] for i in range(0, len(my_str), n)]

#################################################(방법05)

def solution_1(my_str, n):
    result = []
    # 0부터 문자열 끝까지 n만큼 건너뛰며 반복
    for i in range(0, len(my_str), n):
        # i부터 i+n까지 슬라이싱하여 리스트에 추가
        result.append(my_str[i : i + n])
    return result

#################################################(방법06)

def solution_2(my_str, n):
    result = []
    temp = ""
    for char in my_str:
        temp += char
        # 쌓인 글자가 n개가 되면 결과 리스트에 추가하고 비움
        if len(temp) == n:
            result.append(temp)
            temp = ""
    
    # 마지막에 남은 글자가 있다면(n보다 작을 때) 마저 추가
    if temp:
        result.append(temp)
    return result

#################################################(방법07)

def solution_3(my_str, n):
    result = []
    # 문자열의 복사본을 생성하여 작업
    target = my_str
    while len(target) > 0:
        # 앞의 n글자를 결과에 담기
        result.append(target[:n])
        # 담은 만큼은 잘라내고 남은 부분으로 갱신
        target = target[n:]
    return result

#################################################(방법08)

def solution_4(my_str, n):
    result = []
    # 전체 묶음이 몇 개 나올지 계산 (올림 계산 원리)
    total_length = len(my_str)
    num_chunks = (total_length + n - 1) // n
    
    for i in range(num_chunks):
        chunk = ""
        # 각 묶음의 시작(i*n)부터 끝((i+1)*n)까지 직접 글자 추출
        for j in range(i * n, (i + 1) * n):
            if j < total_length: # 문자열 범위를 벗어나지 않을 때만
                chunk += my_str[j]
        result.append(chunk)
    return result

#################################################(방법09)

def solution_5(my_str, n):
    # i는 0, n, 2n... 순으로 증가하며 그 구간만큼 슬라이싱
    return [my_str[i : i + n] for i in range(0, len(my_str), n)]

#################################################(방법10)


