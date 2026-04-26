def solve_v1():
    # 전체 단어 목록을 담을 리스트 (함수 실행 중 계속 유지)
    word_list = []
    
    while True:
        line = input().strip()
        if line == "END":
            break
            
        # 공백을 기준으로 단어 분리
        words = line.split()
        
        for word in words:
            # 목록에 없는 단어만 가장 뒤에 추가
            if word not in word_list:
                word_list.append(word)
        
        # 현재까지의 단어 목록 출력
        print(*(word_list))

solve_v1()

#################################################################

def solve_v2():
    word_list = []
    
    while True:
        line = input().strip()
        if line == "END": break
        
        new_words = line.split()
        for w in new_words:
            if w not in word_list:
                word_list.append(w)
        
        # 순서가 유지된 유니크 리스트 출력
        print(" ".join(word_list))

solve_v2()

#################################################################

def solve_v3():
    word_list = []
    word_set = set() # 빠른 검색을 위한 집합
    
    while True:
        line = input().strip()
        if line == "END": break
        
        for word in line.split():
            if word not in word_set:
                word_list.append(word)
                word_set.add(word) # 집합에도 추가하여 다음 검색 최적화
                
        print(*(word_list))

solve_v3()

#################################################################

class WordManager:
    def __init__(self):
        self.vocabulary = []

    def add_line(self, line):
        for word in line.split():
            if word not in self.vocabulary:
                self.vocabulary.append(word)
        return " ".join(self.vocabulary)

def solve_v4():
    manager = WordManager()
    while True:
        line = input().strip()
        if line == "END": break
        print(manager.add_line(line))

solve_v4()

#################################################################

def solve_v5():
    storage = []
    while True:
        try:
            line = input().strip()
            if line == "END": break
            
            incoming = line.split()
            for word in incoming:
                # 여기서 storage는 매 단어 처리 시마다 업데이트된 상태입니다.
                if word not in storage:
                    storage.append(word)
            
            # 리스트 전체를 공백 구분자로 출력
            print(*(storage))
        except: break

solve_v5()

#################################################################

