def solve():
    # 4개의 테스트 케이스 처리
    for _ in range(4):
        try:
            line1 = input().split()
            if not line1: break
            N, M = int(line1[0]), int(line1[1])
            weather = input().split()
        except EOFError:
            break

        # 1. 0(비 안 오는 날)의 위치만 따로 추출
        zeros = []
        for i in range(M):
            if weather[i] == '0':
                zeros.append(i)
        
        num_zeros = len(zeros)
        # 참견스가 마실 호수 번호 기록 (0으로 초기화)
        ans = [0] * num_zeros
        
        # 2. 가용 날짜 관리 (사용한 0의 인덱스를 건너뛰기 위한 포인터 배열)
        # next_idx[i]는 i번째 '0'이 사용되었을 때 다음에 확인해야 할 '0'의 위치
        next_idx = list(range(num_zeros + 1))
        
        last_rain = {} # 각 호수에 마지막으로 비가 온 날의 인덱스
        is_possible = True
        
        for i in range(M):
            p = int(weather[i])
            if p == 0:
                continue
            
            # 이 호수에 마지막으로 비가 온 날(초기 상태는 -1)
            prev_time = last_rain.get(p, -1)
            
            # 3. 이진 탐색: prev_time 이후에 처음 나타나는 '0'의 인덱스(k) 찾기
            low = 0
            high = num_zeros - 1
            target_k = -1
            while low <= high:
                mid = (low + high) // 2
                if zeros[mid] > prev_time:
                    target_k = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            # 4. 실제 가용한(사용되지 않은) '0' 찾기
            if target_k != -1:
                # 사용된 날짜를 건너뛰는 경로 압축 (반복문 버전)
                curr = target_k
                path = []
                while curr < num_zeros and next_idx[curr] != curr:
                    path.append(curr)
                    curr = next_idx[curr]
                
                # 경로 업데이트 (다음에 바로 찾을 수 있도록)
                for node in path:
                    next_idx[node] = curr
                
                # 가용한 '0'의 인덱스가 weather 전체 범위를 벗어나지 않고 i(현재 비오는 날)보다 앞서야 함
                if curr < num_zeros and zeros[curr] < i:
                    ans[curr] = p
                    next_idx[curr] = curr + 1 # 현재 칸 사용 완료 처리
                    last_rain[p] = i
                else:
                    is_possible = False
                    break
            else:
                is_possible = False
                break

        # 결과 출력
        if is_possible:
            print("YES")
            # 대량의 리스트를 빠르게 출력하는 방식
            print(*(ans))
        else:
            print("NO")

solve()

###########################################################################################

