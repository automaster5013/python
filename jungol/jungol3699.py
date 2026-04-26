def solve_v1():
    import sys
    # 테스트 케이스 수
    try:
        tc_str = input().strip()
        if not tc_str: return
        tc = int(tc_str)
        
        for _ in range(tc):
            n = int(input().strip())
            clothes = {}
            for _ in range(n):
                name, category = input().split()
                # 카테고리별로 개수 카운트
                clothes[category] = clothes.get(category, 0) + 1
            
            ans = 1
            for count in clothes.values():
                ans *= (count + 1)
            
            # 최소 하나는 입어야 하므로 '모두 안 입음' 1가지를 뺌
            print(ans - 1)
    except: pass

solve_v1()

##########################################################################

from collections import Counter

def solve_v2():
    try:
        tc = int(input())
        for _ in range(tc):
            n = int(input())
            # 의상 이름은 무시하고 카테고리만 수집
            categories = [input().split()[1] for _ in range(n)]
            counts = Counter(categories)
            
            ans = 1
            for c in counts.values():
                ans *= (c + 1)
            print(ans - 1)
    except: pass

solve_v2()

##########################################################################

from collections import defaultdict

def solve_v3():
    try:
        tc = int(input())
        for _ in range(tc):
            n = int(input())
            closet = defaultdict(int)
            for _ in range(n):
                _, cat = input().split()
                closet[cat] += 1
            
            res = 1
            for val in closet.values():
                res *= (val + 1)
            print(res - 1)
    except: pass

solve_v3()

##########################################################################

import math

def solve_v4():
    try:
        tc = int(input())
        for _ in range(tc):
            n = int(input())
            clothes_map = {}
            for _ in range(n):
                _, cat = input().split()
                clothes_map[cat] = clothes_map.get(cat, 0) + 1
            
            # (각 카테고리 개수 + 1)의 리스트를 만들어 모두 곱함
            total_comb = math.prod([c + 1 for c in clothes_map.values()])
            print(total_comb - 1)
    except: pass

solve_v4()

##########################################################################

def solve_v5():
    try:
        tc = int(input())
        for _ in range(tc):
            n = int(input())
            if n == 0:
                print(0)
                continue
            
            # 카테고리만 뽑아서 정렬
            cats = sorted([input().split()[1] for _ in range(n)])
            
            ans = 1
            cnt = 1
            for i in range(1, n):
                if cats[i] == cats[i-1]:
                    cnt += 1
                else:
                    ans *= (cnt + 1)
                    cnt = 1
            # 마지막 그룹 처리
            ans *= (cnt + 1)
            print(ans - 1)
    except: pass

solve_v5()

##########################################################################

