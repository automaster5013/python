
import sys

def solve():
    # 모든 입력을 한꺼번에 읽어와 처리 속도를 높입니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t_cases = int(input_data[ptr])
    ptr += 1
    
    for _ in range(t_cases):
        n_ops = int(input_data[ptr])
        ptr += 1
        
        # 각 그룹(접두사)의 개수를 저장할 딕셔너리
        prefix_counts = {}
        # 'O' 명령의 결과를 저장할 리스트
        query_results = []
        
        for _ in range(n_ops):
            command = input_data[ptr]
            species = input_data[ptr + 1]
            ptr += 2
            
            if command == 'I':
                # 새로운 생명체 발견 시 모든 접두사의 카운트 증가
                for i in range(1, len(species) + 1):
                    prefix = species[:i]
                    prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
            
            elif command == 'O':
                # 특정 그룹의 개수 확인
                query_results.append(str(prefix_counts.get(species, 0)))
        
        # 각 테스트케이스 결과를 공백으로 구분하여 출력
        print(" ".join(query_results))

if __name__ == "__main__":
    solve()

###############################################################################


