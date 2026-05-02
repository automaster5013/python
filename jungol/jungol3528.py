import sys
import math
from functools import lru_cache

def solve():
    # 입력을 빠르게 읽어옵니다. (HP OMEN 16의 성능을 위해 split 사용)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    s = input_data[0]
    n = len(s)
    
    # 1. 문자별 빈도수를 구합니다.
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # 2. 팩토리얼 미리 계산
    fact = [math.factorial(i) for i in range(n + 1)]
    
    # 3. 알파벳 순서대로 고정하여 튜플로 변환 (메모이제이션을 위해)
    keys = sorted(char_counts.keys())
    initial_counts = tuple(char_counts[k] for k in keys)

    @lru_cache(None)
    def count_permutations(counts, last_idx):
        # 모든 문자를 다 사용한 경우
        if sum(counts) == 0:
            return 1
        
        # [최적화] 남은 문자들이 모두 서로 다르고, 
        # 마지막으로 놓은 문자가 남은 것 중에 없다면 바로 팩토리얼 반환
        if max(counts) <= 1:
            total_rem = sum(counts)
            # 마지막으로 놓은 문자가 남은 pool에 포함되어 있는지 확인
            if last_idx == -1 or counts[last_idx] == 0:
                return fact[total_rem]

        res = 0
        for i in range(len(keys)):
            # 남은 개수가 있고, 직전 문자와 다른 경우만 선택
            if counts[i] > 0 and i != last_idx:
                # 튜플은 불변 객체이므로 새로운 상태를 만들어 전달
                new_counts = list(counts)
                new_counts[i] -= 1
                res += count_permutations(tuple(new_counts), i)
        
        return res

    # 결과 출력
    print(count_permutations(initial_counts, -1))

if __name__ == "__main__":
    # 재귀 깊이 설정 (10자이므로 기본값으로도 충분하지만 안전을 위해 설정)
    sys.setrecursionlimit(2000)
    solve()

################################################################################



