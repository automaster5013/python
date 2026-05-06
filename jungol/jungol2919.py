import sys

def solve():
    # 빠른 입출력 처리를 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    W = int(input_data[1])
    
    raw_pieces = []
    idx = 2
    for _ in range(N):
        P = int(input_data[idx])
        L = int(input_data[idx+1])
        R = int(input_data[idx+2])
        H = int(input_data[idx+3])
        K = int(input_data[idx+4])
        raw_pieces.append((L, R, H, K, P))
        idx += 5
        
    # 1. 모든 조각을 왼쪽 끝점(L) 기준으로 오름차순 정렬
    raw_pieces.sort(key=lambda x: x[0])
    
    # 더미 조각 (초기 상태를 위해 L=0, R=0 인 빈 조각을 0번 인덱스에 삽입)
    pieces = [(0, 0, 0, 0, -1)] + raw_pieces
    
    # 2. 좌표 압축 (L과 R 좌표들을 모아 인덱스화)
    coords = {0}
    for L, R, H, K, P in raw_pieces:
        coords.add(L)
        coords.add(R)
        
    sorted_coords = sorted(list(coords))
    coord_to_idx = {x: i for i, x in enumerate(sorted_coords)}
    M = len(sorted_coords)
    
    # 각 좌표에서 처리할 '지연 활성화' 이벤트 리스트
    top_events = [[] for _ in range(M)]
    bot_events = [[] for _ in range(M)]
    
    # 0 위치에서 시작하는 초기화 이벤트
    top_events[coord_to_idx[0]].append((0, 0))
    bot_events[coord_to_idx[0]].append((0, 0))
    
    # 각 L 좌표별로 속한 조각들을 분류
    pieces_by_L = [[] for _ in range(M)]
    for k in range(1, N + 1):
        L = pieces[k][0]
        pieces_by_L[coord_to_idx[L]].append(k)
        
    # max_T[j]: 마지막 아랫변 조각이 j일 때, 새로운 윗변 조각을 붙일 수 있는 최대 이익
    max_T = [-1] * (N + 1)
    # max_B[i]: 마지막 윗변 조각이 i일 때, 새로운 아랫변 조각을 붙일 수 있는 최대 이익
    max_B = [-1] * (N + 1)
    ans = 0
    
    # 3. 좌표평면을 0부터 M-1까지 스위핑 (Sweeping)
    for c_idx in range(M):
        # [STEP A] 현재 좌표에 도달하여 활성화된 상태들을 갱신
        for j, val in top_events[c_idx]:
            if val > max_T[j]: max_T[j] = val
        for i, val in bot_events[c_idx]:
            if val > max_B[i]: max_B[i] = val
            
        # [STEP B] 현재 좌표(L)에서 시작하는 조각들을 처리
        for k in pieces_by_L[c_idx]:
            pk_L, pk_R, pk_H, pk_K, pk_type = pieces[k]
            pk_R_idx = coord_to_idx[pk_R]
            
            if pk_type == 0:  # 현재 조각이 윗변(Top)인 경우
                for j in range(k):
                    if max_T[j] != -1:
                        if j != 0:
                            pj_L, pj_R, pj_H, pj_K, pj_type = pieces[j]
                            # 가로로 겹치는데(변만 겹치는건 제외), 세로 길이 합이 W 초과면 추가 불가
                            if pk_L < pj_R and pj_L < pk_R and pk_H + pj_H > W:
                                continue
                        else:
                            pj_R = 0
                            
                        # 조각을 이어나간 새로운 이익
                        val = max_T[j] + pk_K
                        if val > ans: ans = val
                        
                        # 새로운 윗변 조각을 다 썼을 때(pk_R) 미래의 윗변 확장을 예약
                        top_events[pk_R_idx].append((j, val))
                        
                        # 아랫변 확장의 경우, 이전 아랫변(j)이 이미 끝났다면 즉시 갱신
                        if pj_R <= pk_L:
                            if val > max_B[k]: max_B[k] = val
                        else:
                            # 아직 안끝났다면 이전 아랫변이 끝나는 시점(pj_R)에 예약
                            bot_events[coord_to_idx[pj_R]].append((k, val))
                            
            else:  # 현재 조각이 아랫변(Bottom)인 경우
                for i in range(k):
                    if max_B[i] != -1:
                        if i != 0:
                            pi_L, pi_R, pi_H, pi_K, pi_type = pieces[i]
                            if pk_L < pi_R and pi_L < pk_R and pk_H + pi_H > W:
                                continue
                        else:
                            pi_R = 0
                            
                        val = max_B[i] + pk_K
                        if val > ans: ans = val
                        
                        bot_events[pk_R_idx].append((i, val))
                        
                        if pi_R <= pk_L:
                            if val > max_T[k]: max_T[k] = val
                        else:
                            top_events[coord_to_idx[pi_R]].append((k, val))
                            
    print(ans)

if __name__ == '__main__':
    solve()

######################################################################################





