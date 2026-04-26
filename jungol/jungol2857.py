def solve_v1():
    # 5줄의 단어 입력받기
    words = [input().strip() for _ in range(5)]
    result = ""
    
    # 최대 글자수인 15번까지 열(c)을 순회
    for c in range(15):
        # 5개의 행(r)을 순회
        for r in range(5):
            # 현재 단어(words[r])의 길이가 현재 열 번호(c)보다 크면 글자가 존재함
            if c < len(words[r]):
                result += words[r][c]
                
    print(result)

solve_v1()

##################################################################################

def solve_v2():
    words = [input().strip() for _ in range(5)]
    ans = []
    
    for c in range(15):
        for r in range(5):
            try:
                # 글자가 있으면 리스트에 추가, 없으면 IndexError 발생
                ans.append(words[r][c])
            except IndexError:
                # 글자가 없는 경우 그냥 넘어감
                continue
                
    print("".join(ans))

solve_v2()

##################################################################################

from itertools import zip_longest

def solve_v3():
    # 5줄 입력
    words = [list(input().strip()) for _ in range(5)]
    
    # zip_longest를 사용해 세로로 묶음. 빈 자리는 None으로 채움
    vertical_zip = zip_longest(*words, fillvalue=None)
    
    result = ""
    for col in vertical_zip:
        for char in col:
            if char is not None:
                result += char
                
    print(result)

solve_v3()

##################################################################################

def solve_v4():
    # 빈 공간을 의미하는 특수 기호로 채워진 5x15 배열 생성
    grid = [['' for _ in range(15)] for _ in range(5)]
    
    for r in range(5):
        line = input().strip()
        for c in range(len(line)):
            grid[r][c] = line[c]
            
    # 세로로 읽기 (열 -> 행 순서)
    for c in range(15):
        for r in range(5):
            if grid[r][c] != '':
                print(grid[r][c], end='')
    print()

solve_v4()

##################################################################################

def solve_v5():
    words = [input().strip() for _ in range(5)]
    
    # 각 인덱스 c에 대해 words의 r번째 단어에서 문자를 가져오는 제너레이터
    res = "".join(
        words[r][c]
        for c in range(15)
        for r in range(5)
        if c < len(words[r])
    )
    
    print(res)

solve_v5()

##################################################################################

