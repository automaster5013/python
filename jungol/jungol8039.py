import sys

def solve():
    # 빠른 입력을 위해 전체를 읽어들임
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    # 후보자별 현재 점수 (초기값 0)
    score = [0] * (N + 1)
    
    # 점수별 후보자 세트 (0점인 후보자들 초기화)
    # 0점 후보자를 처음부터 set에 넣으면 메모리가 많이 들 수 있으므로 
    # 투표가 발생할 때마다 유동적으로 관리합니다.
    groups = {}
    groups[0] = set(range(1, N + 1))
    
    ptr = 2
    output = []
    
    for _ in range(Q):
        query_type = int(input_data[ptr])
        
        if query_type == 0:
            n = int(input_data[ptr + 1])
            k = int(input_data[ptr + 2])
            ptr += 3
            
            old_s = score[n]
            new_s = old_s + k
            score[n] = new_s
            
            # 기존 점수 그룹에서 제거
            if old_s in groups:
                groups[old_s].discard(n)
            
            # 새로운 점수 그룹에 추가
            if new_s not in groups:
                groups[new_s] = set()
            groups[new_s].add(n)
            
        else:
            x = int(input_data[ptr + 1])
            ptr += 2
            
            if x in groups and groups[x]:
                # 오름차순 정렬 후 문자열로 변환
                sorted_candidates = sorted(list(groups[x]))
                output.append(" ".join(map(str, sorted_candidates)))
            else:
                output.append("None")
                
    # 결과 일괄 출력
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()


