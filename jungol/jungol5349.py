def solve_v1():
    try:
        # 1. 문장 입력 및 단어 분리
        s = input().strip()
        if not s: return
        words = s.split()
        
        # 2. 짝수 번째 단어 추출 (인덱스 1, 3, 5...)
        # words[1::2] -> 인덱스 1부터 끝까지 2씩 건너뜀
        even_words = words[1::2]
        
        # 3. 역순으로 뒤집어서 공백으로 합쳐 출력
        print(*(even_words[::-1]))
    except EOFError:
        pass

solve_v1()

############################################################

def solve_v2():
    try:
        words = input().split()
        
        # 인덱스 i가 홀수일 때(즉, 단어 순서는 짝수일 때) 필터링
        result = [words[i] for i in range(len(words)) if (i + 1) % 2 == 0]
        
        # 뒤집어서 출력
        print(" ".join(result[::-1]))
    except: pass

solve_v2()

############################################################

def solve_v3():
    try:
        words = input().split()
        n = len(words)
        res = []
        
        # 뒤에서부터 앞으로 이동
        for i in range(n - 1, -1, -1):
            # 순서가 짝수(인덱스+1 % 2 == 0)인 것만 담기
            if (i + 1) % 2 == 0:
                res.append(words[i])
                
        print(*(res))
    except: pass

solve_v3()

############################################################

def solve_v4():
    try:
        words = input().split()
        # 짝수 번째 단어가 마지막에 위치할 수도 있으므로 뒤에서부터 확인
        ans = []
        while words:
            # 현재 단어의 순서(개수)
            order = len(words)
            word = words.pop() # 뒤에서부터 하나씩 꺼냄
            
            if order % 2 == 0:
                ans.append(word)
                
        print(" ".join(ans))
    except: pass

solve_v4()

############################################################

def solve_v5():
    try:
        words = input().split()
        
        # (인덱스, 단어) 쌍으로 만들고 짝수 번째만 필터링
        # x[0]은 인덱스이므로 x[0]+1 이 짝수인 것만 남김
        even_only = filter(lambda x: (x[0] + 1) % 2 == 0, enumerate(words))
        
        # 단어만 추출하여 리스트로 만든 뒤 뒤집기
        res = [item[1] for item in even_only]
        print(*(res[::-1]))
    except: pass

solve_v5()

############################################################

