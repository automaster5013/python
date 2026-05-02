import sys

def solve():
    # 대량의 데이터를 효율적으로 읽기 위해 전체를 읽어들입니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # S[i]: 학생 i 뒤에 있는 학생 중 더 작은 카드 번호를 가진 학생의 수
    S = [0] * (N + 1)
    pairs = []
    
    ptr = 2
    for _ in range(M):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        S[u] += 1
        pairs.append((u, v))
        ptr += 2
    
    # 펜윅 트리 초기화: 사용 가능한 카드 번호 관리 (모두 1로 설정)
    bit = [0] * (N + 1)
    def update(i, delta):
        while i <= N:
            bit[i] += delta
            i += (i & -i)
            
    for i in range(1, N + 1):
        update(i, 1)
        
    # k번째 사용 가능한 카드 번호를 찾는 함수 (Binary Lifting)
    def find_kth(k):
        pos = 0
        current_sum = 0
        # N=100,000이므로 2^16 (65536)부터 2^0까지 탐색
        for i in range(16, -1, -1):
            next_pos = pos + (1 << i)
            if next_pos <= N:
                if current_sum + bit[next_pos] < k:
                    pos = next_pos
                    current_sum += bit[pos]
        return pos + 1

    # 학생들의 카드 번호 복원
    cards = [0] * (N + 1)
    for i in range(1, N + 1):
        # i번 학생의 카드는 남은 카드 중 (S[i] + 1)번째로 작은 카드
        k = S[i] + 1
        # 만약 S[i]가 남은 학생 수보다 많다면 논리적으로 모순 (입력 보장 범위 체크)
        if k > (N - i + 1):
            print("-1")
            return
            
        val = find_kth(k)
        cards[i] = val
        update(val, -1) # 사용한 카드 제거

    # 검증: 입력된 명단이 실제 복원된 카드와 일치하는지 확인
    # 총 역전 수 M과 복원된 순열의 역전 수가 같으므로, 
    # 입력된 모든 쌍이 역전인지만 확인하면 충분합니다.
    for u, v in pairs:
        if cards[u] < cards[v]:
            print("-1")
            return
            
    # 결과 출력
    print(*(cards[1:]))

if __name__ == "__main__":
    solve()

##################################################################################

