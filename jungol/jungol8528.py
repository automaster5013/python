def solve():
    import sys
    # 입력을 빠르게 읽기 위해 sys.stdin 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    Q = int(input_data[0])
    # 데이터를 저장할 리스트 (항상 정렬된 상태 유지)
    ms = []
    
    ptr = 1
    for _ in range(Q):
        cmd = input_data[ptr]
        num = int(input_data[ptr + 1])
        ptr += 2
        
        if cmd == 'i':
            # 1. 삽입 (insert): 들어갈 위치를 이분 탐색으로 찾음
            low, high = 0, len(ms)
            while low < high:
                mid = (low + high) // 2
                if ms[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            ms.insert(low, num)
            
        elif cmd == 'r':
            # 2. 하나만 삭제 (remove one): 이분 탐색으로 값의 위치를 찾음
            low, high = 0, len(ms) - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if ms[mid] == num:
                    idx = mid
                    # 여러 개 중 하나만 찾으면 되므로 더 탐색할 필요 없음
                    break
                elif ms[mid] < num:
                    low = mid + 1
                else:
                    high = mid - 1
            
            if idx != -1:
                ms.pop(idx)
                
        elif cmd == 'e':
            # 3. 전부 삭제 (erase all): 해당 값의 시작과 끝 범위를 찾아 제거
            # 시작 위치 찾기 (lower bound)
            low, high = 0, len(ms)
            start_idx = -1
            while low < high:
                mid = (low + high) // 2
                if ms[mid] >= num:
                    high = mid
                else:
                    low = mid + 1
            start_idx = low
            
            # 값이 존재하는지 확인 후 끝 위치 찾기 (upper bound)
            if start_idx < len(ms) and ms[start_idx] == num:
                low, high = start_idx, len(ms)
                while low < high:
                    mid = (low + high) // 2
                    if ms[mid] > num:
                        high = mid
                    else:
                        low = mid + 1
                end_idx = low
                # 리스트 슬라이싱을 이용해 해당 구간을 통째로 삭제
                del ms[start_idx:end_idx]

    # 결과 출력
    print(*(ms))

if __name__ == "__main__":
    solve()

