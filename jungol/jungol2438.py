import sys

# 세그먼트 트리 노드 인덱스 상수
MAX_LEN = 0
PRE_LEN = 1
SUF_LEN = 2
L_CHAR = 3
R_CHAR = 4

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    q = int(input_data[1])
    queries = input_data[2:]

    # 세그먼트 트리 초기화 (1: L, 0: R)
    # 초기 상태는 모두 'L'이므로 모든 길이는 1, 글자는 1(L)
    size = 1
    while size < n:
        size *= 2
    
    # [max_len, pre_len, suf_len, left_char, right_char]
    tree = [[0, 0, 0, 0, 0] for _ in range(2 * size)]
    
    def merge(node, left, right, length):
        l_node = tree[left]
        r_node = tree[right]
        
        # 기본 정보 복사
        tree[node][L_CHAR] = l_node[L_CHAR]
        tree[node][R_CHAR] = r_node[R_CHAR]
        
        m_len = max(l_node[MAX_LEN], r_node[MAX_LEN])
        p_len = l_node[PRE_LEN]
        s_len = r_node[SUF_LEN]
        
        half = length // 2
        # 경계면의 글자가 다르면 결합 가능
        if l_node[R_CHAR] != r_node[L_CHAR]:
            m_len = max(m_len, l_node[SUF_LEN] + r_node[PRE_LEN])
            # 왼쪽 자식이 통째로 교대 구간이면 오른쪽 자식의 pre_len을 합침
            if l_node[PRE_LEN] == half:
                p_len = half + r_node[PRE_LEN]
            # 오른쪽 자식이 통째로 교대 구간이면 왼쪽 자식의 suf_len을 합침
            if r_node[SUF_LEN] == (length - half):
                s_len = (length - half) + l_node[SUF_LEN]
        
        tree[node][MAX_LEN] = m_len
        tree[node][PRE_LEN] = p_len
        tree[node][SUF_LEN] = s_len

    # 트리 빌드 (초기 LLL...)
    for i in range(n):
        idx = size + i
        tree[idx] = [1, 1, 1, 1, 1]
    
    # leaf가 아닌 노드들 병합
    for i in range(size - 1, 0, -1):
        # 해당 노드가 커버하는 전체 길이 계산
        level = i.bit_length()
        node_len = size >> (level - 1)
        merge(i, 2 * i, 2 * i + 1, node_len)

    results = []
    # 쿼리 처리
    for q_idx in queries:
        pos = int(q_idx) - 1
        idx = size + pos
        
        # 글자 반전 (L:1 -> R:0 / R:0 -> L:1)
        new_char = 1 - tree[idx][L_CHAR]
        tree[idx] = [1, 1, 1, new_char, new_char]
        
        # 부모 노드 갱신
        curr = idx // 2
        node_len = 2
        while curr > 0:
            merge(curr, 2 * curr, 2 * curr + 1, node_len)
            curr //= 2
            node_len *= 2
            
        results.append(str(tree[1][MAX_LEN]))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

###################################################################

