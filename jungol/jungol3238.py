import sys

def solve():
    # 대량의 데이터를 빠르게 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # 충분히 작은 값 (수열 범위 밖의 값)
    SENTINEL = -2000000001
    
    # 세그먼트 트리 크기 설정
    size = 1
    while size < N:
        size *= 2
        
    tree = [SENTINEL] * (2 * size)
    
    ptr = 2
    output = []
    
    for _ in range(M):
        cmd = input_data[ptr]
        
        if cmd == '1':
            k = int(input_data[ptr + 1])
            val = int(input_data[ptr + 2])
            ptr += 3
            
            # 리프 노드 업데이트 (1-indexed k를 0-indexed로 변환)
            idx = size + k - 1
            tree[idx] = val
            while idx > 1:
                idx //= 2
                new_max = tree[2 * idx] if tree[2 * idx] > tree[2 * idx + 1] else tree[2 * idx + 1]
                if tree[idx] == new_max:
                    break
                tree[idx] = new_max
                
        elif cmd == '2':
            s = int(input_data[ptr + 1])
            e = int(input_data[ptr + 2])
            ptr += 3
            
            # 구간 최댓값 쿼리
            l = size + s - 1
            r = size + e - 1
            max_val = SENTINEL
            
            while l <= r:
                if l % 2 == 1:
                    if tree[l] > max_val:
                        max_val = tree[l]
                    l += 1
                if r % 2 == 0:
                    if tree[r] > max_val:
                        max_val = tree[r]
                    r -= 1
                l //= 2
                r //= 2
            
            # 유효한 값이 존재할 때만 결과에 추가
            if max_val != SENTINEL:
                output.append(str(max_val))
                
        elif cmd == '3':
            k = int(input_data[ptr + 1])
            ptr += 2
            
            idx = size + k - 1
            # 삭제는 초기값(SENTINEL)으로 되돌리는 것과 같습니다.
            if tree[idx] != SENTINEL:
                tree[idx] = SENTINEL
                while idx > 1:
                    idx //= 2
                    new_max = tree[2 * idx] if tree[2 * idx] > tree[2 * idx + 1] else tree[2 * idx + 1]
                    tree[idx] = new_max
                    
    # 모든 결과 출력
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    solve()

###########################################################################################################

