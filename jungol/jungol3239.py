import sys

def solve():
    # 입력을 한 번에 읽어와 속도를 극대화합니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr]); ptr += 1
    m = int(input_data[ptr]); ptr += 1
    
    # 충분히 큰 값 설정 (10억보다 큰 값)
    INF = 2000000001
    
    # 세그먼트 트리 크기 설정 (n보다 큰 가장 가까운 2의 거듭제곱)
    size = 1 << (n - 1).bit_length()
    # 각 노드는 (값, 인덱스)를 저장
    tree = [(INF, -1)] * (2 * size)
    
    results = []
    
    for _ in range(m):
        cmd = input_data[ptr]; ptr += 1
        
        if cmd == '1':
            k = int(input_data[ptr]); v = int(input_data[ptr+1]); ptr += 2
            # 인덱스 k에 값 v를 업데이트 (1-based index)
            idx = size + k - 1
            tree[idx] = (v, k)
            while idx > 1:
                idx //= 2
                # 두 자식 중 더 작은 (값, 인덱스) 쌍으로 부모 갱신
                tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])
                
        elif cmd == '2':
            s = int(input_data[ptr]); e = int(input_data[ptr+1]); ptr += 2
            # 구간 [s, e]에서 최소값의 인덱스 쿼리
            l, r = size + s - 1, size + e - 1
            res = (INF, -1)
            while l <= r:
                if l % 2 == 1:
                    res = min(res, tree[l])
                    l += 1
                if r % 2 == 0:
                    res = min(res, tree[r])
                    r -= 1
                l //= 2
                r //= 2
            # 유효한 인덱스가 존재할 경우에만 결과 저장
            if res[1] != -1:
                results.append(str(res[1]))
                
        elif cmd == '3':
            s = int(input_data[ptr]); e = int(input_data[ptr+1]); ptr += 2
            # 구간 [s, e]에서 최솟값을 찾아 삭제
            l, r = size + s - 1, size + e - 1
            res = (INF, -1)
            while l <= r:
                if l % 2 == 1:
                    res = min(res, tree[l])
                    l += 1
                if r % 2 == 0:
                    res = min(res, tree[r])
                    r -= 1
                l //= 2
                r //= 2
            
            # 찾은 인덱스의 값을 INF로 변경하여 삭제 처리
            if res[1] != -1:
                idx = size + res[1] - 1
                tree[idx] = (INF, -1)
                while idx > 1:
                    idx //= 2
                    tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])
                    
    # 결과 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()

###############################################################################

