import sys

def solve_v1():
    # 고속 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.read().split()
    if not input: return
    
    n = int(input[0])
    pairs = {}
    count = 0
    
    for i in range(n):
        city_name = input[2*i + 1]
        state_code = input[2*i + 2]
        
        prefix = city_name[:2]
        
        # 조건: 도시 앞글자와 주 코드가 같으면 '특별한 관계'가 될 수 없음 (예제 3번)
        if prefix == state_code:
            continue
            
        # 현재 도시의 상태: (앞글자, 주코드)
        # 우리가 찾는 파트너의 상태: (주코드, 앞글자)
        current_key = prefix + state_code
        partner_key = state_code + prefix
        
        # 딕셔너리에 파트너가 있다면 그 수만큼 정답에 추가
        if partner_key in pairs:
            count += pairs[partner_key]
            
        # 현재 도시 정보를 딕셔너리에 기록
        pairs[current_key] = pairs.get(current_key, 0) + 1
        
    print(count)

solve_v1()

#######################################################################################

from collections import Counter
import sys

def solve_v2():
    data = sys.stdin.read().split()
    n = int(data[0])
    
    # 모든 (도시앞2글자, 주코드) 조합을 리스트에 담음
    city_list = []
    for i in range(n):
        p, st = data[2*i+1][:2], data[2*i+2]
        if p != st: # 같은 주 제외
            city_list.append(p + st)
            
    # 각 키의 출현 빈도 계산
    counts = Counter(city_list)
    ans = 0
    
    # 딕셔너리를 돌면서 짝이 맞는 키가 있는지 확인
    for key in counts:
        partner = key[2:] + key[:2]
        if partner in counts:
            ans += counts[key] * counts[partner]
            
    # (A, B)와 (B, A)가 중복 계산되므로 2로 나눔
    print(ans // 2)

solve_v2()

#######################################################################################

from collections import defaultdict
import sys

def solve_v3():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    
    # 기본값이 0인 딕셔너리
    db = defaultdict(int)
    total_pairs = 0
    
    for _ in range(n):
        city, state = next(it), next(it)
        pre = city[:2]
        
        if pre != state:
            # 파트너(state+pre)가 이미 들어와 있다면 그 개수만큼 더함
            total_pairs += db[state + pre]
            # 나중에 올 파트너를 위해 현재 정보 저장
            db[pre + state] += 1
            
    print(total_pairs)

solve_v3()

#######################################################################################

def solve_v4():
    import sys
    lines = sys.stdin.read().splitlines()
    n = int(lines[0])
    
    # mapping[state][prefix] = count
    mapping = {}
    ans = 0
    
    for i in range(1, n + 1):
        name, state = lines[i].split()
        pre = name[:2]
        
        if pre == state: continue
        
        # 파트너 찾기: mapping[pre][state] 가 있는지 확인
        if pre in mapping and state in mapping[pre]:
            ans += mapping[pre][state]
            
        # 현재 정보 저장
        if state not in mapping: mapping[state] = {}
        mapping[state][pre] = mapping[state].get(pre, 0) + 1
        
    print(ans)

solve_v4()

#######################################################################################

import sys

def get_input():
    for line in sys.stdin:
        for word in line.split():
            yield word

def solve_v5():
    gen = get_input()
    try:
        n = int(next(gen))
    except StopIteration:
        return
        
    storage = {}
    ans = 0
    
    for _ in range(n):
        city = next(gen)
        state = next(gen)
        pre = city[:2]
        
        if pre != state:
            k = pre + state
            pk = state + pre
            ans += storage.get(pk, 0)
            storage[k] = storage.get(k, 0) + 1
            
    print(ans)

solve_v5()

#######################################################################################


