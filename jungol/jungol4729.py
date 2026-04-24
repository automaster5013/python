import sys
import heapq

# 빠른 입력을 위해 sys.stdin 사용
def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N = int(input_data[0])
    K = int(input_data[1])
    
    # 초기값 A0, B0, C0, D0
    vals = {
        'A': int(input_data[2]),
        'B': int(input_data[3]),
        'C': int(input_data[4]),
        'D': int(input_data[5])
    }
    
    # 카드 분류
    cards_by_type = {'A': [], 'B': [], 'C': [], 'D': []}
    idx = 6
    for _ in range(N):
        t = input_data[idx]
        u = int(input_data[idx+1])
        cards_by_type[t].append(u)
        idx += 2
        
    # 각 타입별로 큰 값부터 정렬
    for t in cards_by_type:
        cards_by_type[t].sort(reverse=True)
        
    # 우선순위 큐 구성을 위한 클래스 (최대 힙 효과)
    class Multiplier:
        def __init__(self, u, t_name, current_val, card_idx):
            self.u = u
            self.t_name = t_name
            self.current_val = current_val
            self.card_idx = card_idx
            
        def __lt__(self, other):
            # 배율 비교: (v + u1)/v > (o_v + u2)/o_v => u1/v > u2/o_v => u1 * o_v > u2 * v
            # heapq는 최소 힙이므로, 큰 배율이 우선순위가 높도록 반대로 비교
            return self.u * other.current_val > other.u * self.current_val

    pq = []
    # 각 변수별 첫 번째(가장 큰 U) 카드를 큐에 삽입
    for t in ['A', 'B', 'C', 'D']:
        if cards_by_type[t]:
            heapq.heappush(pq, Multiplier(cards_by_type[t][0], t, vals[t], 0))
            
    # K번 추출
    results = []
    for _ in range(K):
        best = heapq.heappop(pq)
        results.append(f"{best.t_name} {best.u}")
        
        # 변수 값 업데이트
        vals[best.t_name] += best.u
        
        # 해당 변수의 다음 카드 삽입
        next_card_idx = best.card_idx + 1
        if next_card_idx < len(cards_by_type[best.t_name]):
            next_u = cards_by_type[best.t_name][next_card_idx]
            heapq.heappush(pq, Multiplier(next_u, best.t_name, vals[best.t_name], next_card_idx))
            
    # 결과 출력
    print('\n'.join(results))

if __name__ == "__main__":
    solve()


