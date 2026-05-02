import sys

# 대량의 데이터를 효율적으로 읽기 위한 토큰 생성기
def get_tokens():
    for line in sys.stdin:
        for token in line.split():
            yield token

def solve():
    tokens = get_tokens()
    
    try:
        token = next(tokens)
        if not token: return
        n = int(token)
        q = int(next(tokens))
    except StopIteration:
        return

    # 건초 더미 방어력 정보 읽기
    d = [int(next(tokens)) for _ in range(n)]

    # 쿼리 정보 읽기 및 원본 인덱스 저장
    queries = []
    for i in range(q):
        x = int(next(tokens))
        p = int(next(tokens))
        queries.append((x, p, i))
    
    # 위치 X 기준 정렬 (오프라인 처리)
    queries.sort()

    # 방어력 값 좌표 압축
    u = sorted(list(set(d)))
    k = len(u)
    val_to_rank = {v: i for i, v in enumerate(u)}

    # 세그먼트 트리 크기 설정 (2의 거듭제곱)
    size = 1
    while size < k:
        size *= 2

    # cnt: 건초 더미 개수, sm: 방어력 총합
    cnt = [0] * (2 * size)
    sm = [0] * (2 * size)

    ans = [0] * q
    curr_x = 0

    # 건초 더미를 하나씩 추가하며 쿼리 해결
    for x, p, q_id in queries:
        while curr_x < x:
            val = d[curr_x]
            rank = val_to_rank[val]
            node = rank + size
            while node >= 1:
                cnt[node] += 1
                sm[node] += val
                node //= 2
            curr_x += 1
        
        # 전체 합이 P보다 작으면 멈출 수 없음
        if sm[1] < p:
            ans[q_id] = -1
        else:
            curr_p = p
            res_k = 0
            node = 1
            # 큰 값(오른쪽 자식)부터 탐색하여 필요한 최소 개수 계산
            while node < size:
                right = 2 * node + 1
                if sm[right] >= curr_p:
                    node = right
                else:
                    res_k += cnt[right]
                    curr_p -= sm[right]
                    node = 2 * node
            
            # 리프 노드에서 남은 p를 채우기 위해 필요한 개수 산출
            rank = node - size
            if rank < k:
                val = u[rank]
                needed = (curr_p + val - 1) // val
                ans[q_id] = res_k + needed
            else:
                ans[q_id] = -1

    # 결과 출력
    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

if __name__ == "__main__":
    solve()

######################################################################

