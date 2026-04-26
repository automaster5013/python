def solve_v1():
    while True:
        try:
            line = input().strip()
            if line == "END":
                break
            
            # 1. 단어 분리 및 빈도 계산
            words = line.split()
            word_count = {}
            for w in words:
                if w in word_count:
                    word_count[w] += 1
                else:
                    word_count[w] = 1
            
            # 2. 키(단어)를 기준으로 아스키코드 정렬 후 출력
            sorted_keys = sorted(word_count.keys())
            for key in sorted_keys:
                print(f"{key} : {word_count[key]}")
        except EOFError:
            break

solve_v1()

###############################################################

from collections import Counter

def solve_v2():
    while True:
        line = input().strip()
        if line == "END": break
        
        # Counter가 단어의 개수를 즉시 계산함
        counts = Counter(line.split())
        
        # 키를 정렬하여 출력
        for word in sorted(counts.keys()):
            print(f"{word} : {counts[word]}")

solve_v2()

###############################################################

from collections import defaultdict

def solve_v3():
    while True:
        line = input().strip()
        if line == "END": break
        
        # 기본값이 0인 딕셔너리 생성
        counts = defaultdict(int)
        for word in line.split():
            counts[word] += 1
            
        # 정렬된 키-값 쌍(items)을 순회
        for word, freq in sorted(counts.items()):
            print(f"{word} : {freq}")

solve_v3()

###############################################################

def solve_v4():
    while True:
        line = input().strip()
        if line == "END": break
        
        words = line.split()
        # 중복을 제거한 고유 단어 목록을 만들고 즉시 정렬
        unique_words = sorted(list(set(words)))
        
        for word in unique_words:
            # 원본 리스트에서 해당 단어가 몇 개인지 직접 세기
            print(f"{word} : {words.count(word)}")

solve_v4()

###############################################################

def solve_v5():
    while True:
        try:
            line = input().strip()
            if line == "END": break
            
            words = line.split()
            # 딕셔너리 컴프리헨션을 사용하여 고유 단어별 빈도 생성
            word_map = {w: words.count(w) for w in set(words)}
            
            # 아스키코드 순서로 정렬된 결과 출력
            for k in sorted(word_map):
                print(f"{k} : {word_map[k]}")
        except: break

solve_v5()

###############################################################

