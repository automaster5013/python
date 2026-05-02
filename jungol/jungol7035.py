import sys

# 빠른 입력을 위한 설정
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    Q = int(data[1])
    
    # 초기 점수 리스트 (1번 학생부터 시작하므로 인덱스 조정)
    scores = [0] * (N + 1)
    for i in range(1, N + 1):
        scores[i] = int(data[1 + i])
        
    MAX_SCORE = 100000
    # 펜윅 트리 (각 점수대별 인원수 저장)
    bit = [0] * (MAX_SCORE + 1)
    
    def update(idx, val):
        while idx <= MAX_SCORE:
            bit[idx] += val
            idx += (idx & -idx)
            
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= (idx & -idx)
        return s

    # 초기 상태를 트리에 반영
    for i in range(1, N + 1):
        update(scores[i], 1)
        
    ptr = N + 2
    results = []
    
    for _ in range(Q):
        type = data[ptr]
        if type == '1':
            x = int(data[ptr + 1])
            ptr += 2
            curr_score = scores[x]
            # 나보다 높은 점수를 가진 사람 수 = 전체 인원 - (나와 같거나 낮은 점수 인원)
            # 등수 = (전체 인원 - query(curr_score)) + 1
            rank = (N - query(curr_score)) + 1
            results.append(str(rank))
        else:
            x = int(data[ptr + 1])
            y = int(data[ptr + 2])
            ptr += 3
            # 기존 점수 제거 후 새 점수 추가
            old_score = scores[x]
            update(old_score, -1)
            scores[x] = y
            update(y, 1)
            
    # 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

#######################################################################################


