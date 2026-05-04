T_case = input()
if T_case:
    T = int(T_case)
    # print(T)
    for t in range(1, T + 1):
        N = int(input())
        
        nums = list(map(int, input().split()))
        
        max_val = nums[0]
        min_val = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]

            if nums[i] < min_val:
                min_val = nums[i]
        
        result = max_val - min_val
        print(f"#{t} {result}")

########################################################(방법01)

def get_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        return (max(arr[low], arr[high]), min(arr[low], arr[high]))
    
    mid = (low + high) // 2
    max1, min1 = get_min_max(arr, low, mid)
    max2, min2 = get_min_max(arr, mid + 1, high)
    
    return max(max1, max2), min(min1, min2)

max_val, min_val = get_min_max(nums, 0, len(nums) - 1)
result = max_val - min_val

########################################################(방법02)




























































# 1. 테스트 케이스의 수 T 입력
T_str = input()
if T_str:
    T = int(T_str)

    for t in range(1, T + 1):
        # 2. 양수의 개수 N 입력 (이 문제에서는 입력을 위해 사용되지만 로직상 필수는 아님)
        N = int(input())
        
        # 3. N개의 양수를 입력받아 리스트로 변환
        # input().split()은 공백을 기준으로 문자열을 잘라 리스트로 만듭니다.
        nums = list(map(int, input().split()))
        
        # 4. 최댓값과 최솟값을 직접 찾기 위한 초기화
        # 리스트의 첫 번째 원소를 초기 기준으로 설정합니다.
        max_val = nums[0]
        min_val = nums[0]
        
        # 5. 반복문을 돌며 최댓값과 최솟값 갱신 (직접 비교 방식)
        for i in range(1, len(nums)):
            # 현재 숫자가 기준 최댓값보다 크면 갱신
            if nums[i] > max_val:
                max_val = nums[i]
            # 현재 숫자가 기준 최솟값보다 작으면 갱신
            if nums[i] < min_val:
                min_val = nums[i]
        
        # 6. 차이 계산 및 출력
        result = max_val - min_val
        print(f"#{t} {result}")