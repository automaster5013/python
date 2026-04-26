from itertools import permutations

def solve_v1():
    n = int(input())
    queries = [input().split() for _ in range(n)]
    
    # 1~9 숫자로 만든 모든 서로 다른 3자리 수 후보 (504개)
    candidates = list(permutations(range(1, 10), 3))
    
    possible_count = 0
    
    for cand in candidates:
        is_match = True
        for q_num, q_s, q_b in queries:
            s_count, b_count = 0, 0
            # 질문 숫자를 튜플 형태로 변환 (비교 편의성)
            q_list = [int(d) for d in q_num]
            
            # 스트라이크 & 볼 판정 로직
            for i in range(3):
                if cand[i] == q_list[i]:
                    s_count += 1
                elif q_list[i] in cand:
                    b_count += 1
            
            # 입력된 결과와 다르면 이 후보는 탈락
            if s_count != int(q_s) or b_count != int(q_b):
                is_match = False
                break
        
        if is_match:
            possible_count += 1
            
    print(possible_count)

solve_v1()

##################################################################################################

def solve_v2():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for i in range(1, 10): # 첫째 자리
        for j in range(1, 10): # 둘째 자리
            for k in range(1, 10): # 셋째 자리
                if i == j or j == k or i == k: continue # 중복 제거
                
                cand = [i, j, k]
                is_ok = True
                
                for num, s, b in data:
                    s_cnt, b_cnt = 0, 0
                    q = [int(d) for d in str(num)]
                    
                    for idx in range(3):
                        if cand[idx] == q[idx]: s_cnt += 1
                        elif q[idx] in cand: b_cnt += 1
                    
                    if s_cnt != s or b_cnt != b:
                        is_ok = False
                        break
                if is_ok: ans += 1
    print(ans)

solve_v2()

##################################################################################################

def solve_v3():
    from itertools import permutations
    
    n = int(input())
    nums = list(permutations('123456789', 3))
    
    for _ in range(n):
        q_num, s, b = input().split()
        s, b = int(s), int(b)
        new_nums = []
        
        for cand in nums:
            cur_s, cur_b = 0, 0
            for i in range(3):
                if cand[i] == q_num[i]:
                    cur_s += 1
                elif q_num[i] in cand:
                    cur_b += 1
            
            if cur_s == s and cur_b == b:
                new_nums.append(cand)
        nums = new_nums # 살아남은 후보들로 갱신
        
    print(len(nums))

solve_v3()

##################################################################################################

def check_score(cand, query):
    s, b = 0, 0
    for i in range(3):
        if cand[i] == query[i]: s += 1
        elif query[i] in cand: b += 1
    return s, b

def solve_v4():
    n = int(input())
    hints = [input().split() for _ in range(n)]
    count = 0
    
    for i in range(123, 988):
        s_i = str(i)
        if '0' in s_i or len(set(s_i)) < 3: continue
        
        if all(check_score(s_i, h[0]) == (int(h[1]), int(h[2])) for h in hints):
            count += 1
    print(count)

solve_v4()

##################################################################################################

from itertools import permutations

def solve_v5():
    n = int(input())
    tests = [input().split() for _ in range(n)]
    
    def is_valid(cand):
        for q, s, b in tests:
            strike = sum(1 for i in range(3) if cand[i] == q[i])
            ball = sum(1 for i in range(3) if q[i] in cand) - strike
            if strike != int(s) or ball != int(b):
                return False
        return True

    # 1~9 숫자로 만든 3자리 순열 중 유효한 것만 필터링하여 합산
    print(sum(1 for p in permutations('123456789', 3) if is_valid(p)))

solve_v5()

##################################################################################################

