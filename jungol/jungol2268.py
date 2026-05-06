import sys
import random

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    M = int(input_data[0])
    K = int(input_data[1])
    
    constraints = []
    idx = 2
    for _ in range(K):
        u = int(input_data[idx], 2)
        v = int(input_data[idx+1], 2)
        diff = u ^ v
        bp = (diff & -diff).bit_length() - 1
        constraints.append((u, v, bp))
        idx += 2

    num_nodes = 1 << M
    # 변화 비트 순서 미리 계산
    steps = [(i & -i).bit_length() - 1 for i in range(1, num_nodes)]
    
    # 5초 제한 시간을 고려하여 최대 시도 횟수 설정
    for attempt in range(100):
        bit_map = list(range(M))
        random.shuffle(bit_map) # 무작위 비트 매핑으로 탐색 범위 확장
        
        # 제약 조건의 비트들을 bit_map의 앞부분에 우선 배치해볼 수 있음
        if attempt == 0: # 첫 시도는 정석대로
            for i, (_, _, bp) in enumerate(constraints):
                target_idx = bit_map.index(bp)
                bit_map[i], bit_map[target_idx] = bit_map[target_idx], bit_map[i]

        # 경로 생성
        res = [0] * num_nodes
        curr = 0
        for i in range(num_nodes - 1):
            curr ^= (1 << bit_map[steps[i]])
            res[i+1] = curr
        
        # 간선 세트 구성
        edges_set = set()
        for i in range(num_nodes):
            edges_set.add(tuple(sorted((res[i], res[(i+1)%num_nodes]))))
            
        # 제약 조건을 만족하는 XOR 값 찾기
        for c_u, c_v, _ in constraints:
            # 첫 번째 제약 조건을 기준으로 xor_val 후보 탐색
            u_target, v_target = constraints[0][0], constraints[0][1]
            
            # res의 모든 간선 j에 대해 xor_val을 적용해봄
            for j in range(num_nodes):
                xor_val = u_target ^ res[j]
                
                # 모든 제약 조건이 만족되는지 확인
                match_all = True
                for cu, cv, _ in constraints:
                    if tuple(sorted((cu ^ xor_val, cv ^ xor_val))) not in edges_set:
                        match_all = False
                        break
                
                if match_all:
                    # 000...0으로 시작하도록 회전
                    start_xor_node = xor_val ^ 0 # 0이 될 원래 노드
                    try:
                        z_idx = res.index(start_xor_node)
                        rotated = res[z_idx:] + res[:z_idx]
                        final_path = [(x ^ start_xor_node) for x in rotated]
                        
                        # 출력 및 종료
                        for row in range(0, num_nodes, 8):
                            print(*(bin(x)[2:].zfill(M) for x in final_path[row:row+8]))
                        return
                    except: continue
            break # 첫 번째 제약 조건으로 안 되면 이 bit_map은 실패

    print("-1")

if __name__ == "__main__":
    solve()

#####################################################################################################


