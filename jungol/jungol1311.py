def solve_v1():
    colors = []
    nums = []
    for _ in range(5):
        c, n = input().split()
        colors.append(c)
        nums.append(int(n))
    
    nums.sort()
    
    # 기초 정보 분석
    same_color = len(set(colors)) == 1
    continuous = all(nums[i+1] - nums[i] == 1 for i in range(4))
    
    counts = [0] * 10
    for n in nums:
        counts[n] += 1
    
    max_count = max(counts)
    
    # 규칙 적용 (높은 점수순)
    if same_color and continuous:
        return nums[4] + 900
    
    if max_count == 4:
        return counts.index(4) + 800
    
    if max_count == 3 and 2 in counts:
        return counts.index(3) * 10 + counts.index(2) + 700
    
    if same_color:
        return nums[4] + 600
    
    if continuous:
        return nums[4] + 500
    
    if max_count == 3:
        return counts.index(3) + 400
    
    if counts.count(2) == 2:
        pairs = [i for i, v in enumerate(counts) if v == 2]
        return max(pairs) * 10 + min(pairs) + 300
    
    if max_count == 2:
        return counts.index(2) + 200
    
    return nums[4] + 100

print(solve_v1())

###############################################################################

from collections import Counter

def solve_v2():
    cards = [input().split() for _ in range(5)]
    colors = [c[0] for c in cards]
    nums = sorted([int(c[1]) for c in cards])
    
    num_counts = Counter(nums)
    # 빈도순으로 정렬된 리스트: [(숫자, 빈도), ...]
    freq = num_counts.most_common()
    
    is_flush = len(set(colors)) == 1
    is_straight = all(nums[i+1] - nums[i] == 1 for i in range(4))
    
    # 규칙 체크
    if is_flush and is_straight: return nums[4] + 900
    if freq[0][1] == 4: return freq[0][0] + 800
    if freq[0][1] == 3 and freq[1][1] == 2: return freq[0][0] * 10 + freq[1][0] + 700
    if is_flush: return nums[4] + 600
    if is_straight: return nums[4] + 500
    if freq[0][1] == 3: return freq[0][0] + 400
    if freq[0][1] == 2 and freq[1][1] == 2:
        pair_nums = sorted([freq[0][0], freq[1][0]], reverse=True)
        return pair_nums[0] * 10 + pair_nums[1] + 300
    if freq[0][1] == 2: return freq[0][0] + 200
    return nums[4] + 100

print(solve_v2())

###############################################################################

import sys

def solve():
    cards = []
    for _ in range(5):
        # 입력 형식이 "B 3" 같이 들어오므로 split으로 분리
        c, n = sys.stdin.readline().split()
        cards.append((c, int(n)))

    colors = [c[0] for c in cards]
    nums = sorted([c[1] for c in cards])
    
    # 숫자별 개수 파악 (1~9까지)
    counts = [0] * 10
    for n in nums:
        counts[n] += 1
    
    # 패턴 분석
    is_flush = len(set(colors)) == 1
    is_straight = all(nums[i] + 1 == nums[i+1] for i in range(4))
    
    # 같은 숫자가 몇 개 있는지 확인
    max_c = max(counts)
    
    # 규칙 체크 (높은 점수순)
    if is_flush and is_straight: return nums[4] + 900
    if max_c == 4: return counts.index(4) + 800
    if max_c == 3 and 2 in counts:
        return counts.index(3) * 10 + counts.index(2) + 700
    if is_flush: return nums[4] + 600
    if is_straight: return nums[4] + 500
    if max_c == 3: return counts.index(3) + 400
    if counts.count(2) == 2:
        pairs = [i for i, v in enumerate(counts) if v == 2]
        return max(pairs) * 10 + min(pairs) + 300
    if max_c == 2: return counts.index(2) + 200
    return nums[4] + 100

print(solve())

###############################################################################

import sys
from collections import Counter

def solve():
    # 5줄의 입력을 리스트로 변환
    data = [sys.stdin.readline().split() for _ in range(5)]
    colors = [d[0] for d in data]
    nums = sorted([int(d[1]) for d in data])
    
    counts = Counter(nums)
    # 빈도순 정렬 (개수가 많은 순, 개수가 같으면 숫자가 큰 순)
    sorted_counts = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    is_f = len(set(colors)) == 1
    is_s = all(nums[i] + 1 == nums[i+1] for i in range(4))
    
    m_f = sorted_counts[0][1] # 가장 많이 나타난 숫자의 횟수

    if is_f and is_s: return nums[4] + 900
    if m_f == 4: return sorted_counts[0][0] + 800
    if m_f == 3 and sorted_counts[1][1] == 2:
        return sorted_counts[0][0] * 10 + sorted_counts[1][0] + 700
    if is_f: return nums[4] + 600
    if is_s: return nums[4] + 500
    if m_f == 3: return sorted_counts[0][0] + 400
    if m_f == 2 and sorted_counts[1][1] == 2:
        # 투 페어는 두 숫자 중 큰 숫자를 먼저 사용
        p1, p2 = sorted_counts[0][0], sorted_counts[1][0]
        return max(p1, p2) * 10 + min(p1, p2) + 300
    if m_f == 2: return sorted_counts[0][0] + 200
    return nums[4] + 100

print(solve())

###############################################################################

def solve():
    c_list, n_list = [], []
    for _ in range(5):
        c, n = input().split()
        c_list.append(c)
        n_list.append(int(n))
    n_list.sort()

    # 수동 딕셔너리 카운팅
    freq = {}
    for n in n_list:
        freq[n] = freq.get(n, 0) + 1
    
    # 개수와 숫자 정보를 리스트로 정리
    stats = sorted([(v, k) for k, v in freq.items()], reverse=True)
    # stats 예: [(4, 3), (1, 7)] -> 3이 4번 나옴

    f = len(set(c_list)) == 1
    s = (n_list[4] - n_list[0] == 4) and len(set(n_list)) == 5

    if f and s: return n_list[4] + 900
    if stats[0][0] == 4: return stats[0][1] + 800
    if stats[0][0] == 3 and len(stats) > 1 and stats[1][0] == 2:
        return stats[0][1] * 10 + stats[1][1] + 700
    if f: return n_list[4] + 600
    if s: return n_list[4] + 500
    if stats[0][0] == 3: return stats[0][1] + 400
    if len(stats) > 1 and stats[0][0] == 2 and stats[1][0] == 2:
        return max(stats[0][1], stats[1][1]) * 10 + min(stats[0][1], stats[1][1]) + 300
    if stats[0][0] == 2: return stats[0][1] + 200
    return n_list[4] + 100

print(solve())

###############################################################################

import sys

def solve():
    raw = [sys.stdin.readline().split() for _ in range(5)]
    c = [x[0] for x in raw]
    n = sorted([int(x[1]) for x in raw])
    
    counts = {i: n.count(i) for i in set(n)}
    vals = sorted(counts.values(), reverse=True)
    
    is_f = len(set(c)) == 1
    is_s = all(n[i]+1 == n[i+1] for i in range(4))
    
    # 각 빈도별 숫자 찾기
    def get_num(freq):
        return [k for k, v in counts.items() if v == freq]

    if is_f and is_s: return n[4] + 900
    if 4 in vals: return get_num(4)[0] + 800
    if 3 in vals and 2 in vals: return get_num(3)[0] * 10 + get_num(2)[0] + 700
    if is_f: return n[4] + 600
    if is_s: return n[4] + 500
    if 3 in vals: return get_num(3)[0] + 400
    if vals.count(2) == 2:
        p = sorted(get_num(2))
        return p[1] * 10 + p[0] + 300
    if 2 in vals: return get_num(2)[0] + 200
    return n[4] + 100

print(solve())

###############################################################################

import sys

def check():
    cards = [sys.stdin.readline().split() for _ in range(5)]
    colors = [x[0] for x in cards]
    nums = sorted([int(x[1]) for x in cards])
    
    cnt = {i: nums.count(i) for i in range(1, 10)}
    num_list = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    
    flush = len(set(colors)) == 1
    straight = all(nums[i] + 1 == nums[i+1] for i in range(4))
    
    # 1. 스트레이트 플러시
    if flush and straight: return nums[4] + 900
    # 2. 포카드
    if num_list[0][1] == 4: return num_list[0][0] + 800
    # 3. 풀하우스
    if num_list[0][1] == 3 and num_list[1][1] == 2:
        return num_list[0][0] * 10 + num_list[1][0] + 700
    # 4. 플러시
    if flush: return nums[4] + 600
    # 5. 스트레이트
    if straight: return nums[4] + 500
    # 6. 트리플
    if num_list[0][1] == 3: return num_list[0][0] + 400
    # 7. 투 페어
    if num_list[0][1] == 2 and num_list[1][1] == 2:
        a, b = num_list[0][0], num_list[1][0]
        return max(a, b) * 10 + min(a, b) + 300
    # 8. 원 페어
    if num_list[0][1] == 2: return num_list[0][0] + 200
    # 9. 탑
    return nums[4] + 100

print(check())

###############################################################################

