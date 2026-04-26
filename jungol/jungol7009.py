import sys

def solve_v1():
    # 모든 입력을 한 번에 읽어와 토큰화 (고속 IO)
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    q = int(input_data[1])
    
    # 주민 번호를 세트(set)로 저장 (중복 제거 및 O(1) 탐색 보장)
    residents = set(input_data[2 : 2+n])
    # 용의자 명단 리스트
    suspects = input_data[2+n : 2+n+q]
    
    non_residents = []
    
    for s in suspects:
        # 해당 용의자가 주민 세트에 없는지 확인
        if s not in residents:
            non_residents.append(s)
            
    # 결과 출력
    if not non_residents:
        print("-1")
    else:
        print(" ".join(non_residents))

if __name__ == "__main__":

    solve_v1()

#################################################################

import sys

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def solve_v2():
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    q = int(next(it))
    
    # 주민 명단은 정렬이 필요함
    residents = sorted([int(next(it)) for _ in range(n)])
    
    results = []
    for _ in range(q):
        suspect = int(next(it))
        if not binary_search(residents, suspect):
            results.append(str(suspect))
            
    if not results:
        print("-1")
    else:
        sys.stdout.write(" ".join(results) + "\n")

    solve_v2()

#################################################################

class InvestigationUnit:
    def __init__(self, resident_list):
        # 생성 시점에 해시 셋 구축
        self.resident_db = set(resident_list)

    def find_outsiders(self, suspect_list):
        outsiders = [s for s in suspect_list if s not in self.resident_db]
        return outsiders if outsiders else None

def solve_v3():
    import sys
    tokens = sys.stdin.read().split()
    n, q = int(tokens[0]), int(tokens[1])
    
    # 수사대 생성
    unit = InvestigationUnit(tokens[2:2+n])
    # 결과 도출
    result = unit.find_outsiders(tokens[2+n:])
    
    if result:
        print(" ".join(result))
    else:
        print("-1")

    solve_v3()

#################################################################


