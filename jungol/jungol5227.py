import sys

# 반복문을 이용한 세그먼트 트리 (Iterative Segment Tree)
def solve():
    # 빠른 입출력 설정
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    s_chars = list(input_data[0])
    n = len(s_chars)
    q = int(input_data[1])
    
    # 전체 R 개수 초기화
    total_r = s_chars.count('R')
    
    # 배열 d 초기화
    d = [0] * n
    d[0] = 1 if s_chars[0] == 'L' else 0
    for i in range(1, n):
        val_l = 1 if s_chars[i] == 'L' else 0
        val_r_prev = 1 if s_chars[i-1] == 'R' else 0
        d[i] = val_l - val_r_prev
        
    # 세그먼트 트리 크기 설정
    m = 1
    while m < n:
        m *= 2
    
    sums = [0] * (2 * m)
    max_prefs = [-float('inf')] * (2 * m)
    
    # 리프 노드 채우기
    for i in range(n):
        sums[m + i] = d[i]
        max_prefs[m + i] = d[i]
        
    # 트리 빌드
    for i in range(m - 1, 0, -1):
        sums[i] = sums[2 * i] + sums[2 * i + 1]
        max_prefs[i] = max(max_prefs[2 * i], sums[2 * i] + max_prefs[2 * i + 1])
        
    # 포인트 업데이트 함수
    def update_node(idx, val):
        node_idx = idx + m
        sums[node_idx] = val
        max_prefs[node_idx] = val
        node_idx //= 2
        while node_idx >= 1:
            left = 2 * node_idx
            right = 2 * node_idx + 1
            sums[node_idx] = sums[left] + sums[right]
            max_prefs[node_idx] = max(max_prefs[left], sums[left] + max_prefs[right])
            node_idx //= 2

    ptr = 2
    results = []
    for _ in range(q):
        p = int(input_data[ptr])
        c = input_data[ptr+1]
        ptr += 2
        
        idx = p - 1 # 0-indexed 변환
        
        old_char = s_chars[idx]
        if old_char != c:
            # 전체 R 개수 업데이트
            if old_char == 'R': total_r -= 1
            if c == 'R': total_r += 1
            
            s_chars[idx] = c
            
            # d[idx] 업데이트
            if idx == 0:
                d[0] = 1 if s_chars[0] == 'L' else 0
            else:
                d[idx] = (1 if s_chars[idx] == 'L' else 0) - (1 if s_chars[idx-1] == 'R' else 0)
            update_node(idx, d[idx])
            
            # d[idx+1] 업데이트 (S[idx]의 변화가 d[idx+1]에 영향을 줌)
            if idx + 1 < n:
                d[idx+1] = (1 if s_chars[idx+1] == 'L' else 0) - (1 if s_chars[idx] == 'R' else 0)
                update_node(idx + 1, d[idx+1])
        
        # 결과값 계산: 전체 R 개수 + 최대 누적 합
        results.append(str(total_r + max_prefs[1]))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

######################################################################################################

