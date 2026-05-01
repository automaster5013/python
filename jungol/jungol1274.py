import sys

def solve():
    # 8자리 2진수를 입력받습니다.
    binary_str = sys.stdin.readline().strip()
    
    # 최상위 비트(MSB)가 0이면 양수입니다.
    if binary_str[0] == '0':
        print(int(binary_str, 2))
    else:
        # 최상위 비트가 1이면 음수입니다. 2의 보수 역산을 수행합니다.
        
        # 1. 모든 비트를 반전시킵니다 (1의 보수 과정)
        flipped = ""
        for bit in binary_str:
            flipped += '1' if bit == '0' else '0'
        
        # 2. 반전시킨 값을 10진수로 바꾼 뒤 1을 더합니다 (2의 보수 완성)
        # 3. 음수이므로 마이너스(-) 부호를 붙여 출력합니다.
        decimal_val = int(flipped, 2) + 1
        print(-decimal_val)

if __name__ == "__main__":
    solve()

########################################################################

import sys

def solve():
    binary_str = sys.stdin.readline().strip()
    
    n = int(binary_str, 2)
    print(n if binary_str[0] == '0' else n - 256)

if __name__ == "__main__":
    solve()

########################################################################


