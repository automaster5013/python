import sys
from bisect import bisect_left

def solve():
    # 대량의 데이터를 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # 원본 실력 수치 리스트
    skills = [int(input_data[i]) for i in range(1, n + 1)]
    
    # 1. 좌표 압축 (Coordinate Compression)
    # 중복 제거 후 정렬하여 순위를 매깁니다.
    sorted_skills = sorted(list(set(skills)))
    compressed_skills = [bisect_left(sorted_skills, s) + 1 for s in skills]
    
    # 2. 펜윅 트리 (Fenwick Tree) 구현
    # bit[i]는 압축된 실력 i를 가진 선수의 등장 횟수를 관리합니다.
    bit = [0] * (n + 1)
    
    def update(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += (idx & -idx)
            
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= (idx & -idx)
        return s

    results = []
    # 3. 앞에서부터 순차적으로 처리
    for i in range(n):
        curr_skill = compressed_skills[i]
        
        # 현재까지 등장한 선수 수 - (나보다 실력이 작거나 같은 선수 수) 
        # = 나보다 실력이 좋은 선수 수
        count_higher = i - query(curr_skill)
        results.append(str(count_higher + 1))
        
        # 현재 선수의 실력을 트리에 기록
        update(curr_skill, 1)
        
    # 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

######################################################################

