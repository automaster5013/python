import sys

def solve():
    # 입력을 읽어 정수로 변환합니다.
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            return
        n = int(input_data)
        
        # 1. 각 바이트를 추출합니다. (8비트씩 마스킹)
        # 0x12345678 기준:
        byte0 = (n >> 0) & 0xFF   # 0x78 (가장 낮은 바이트)
        byte1 = (n >> 8) & 0xFF   # 0x56
        byte2 = (n >> 16) & 0xFF  # 0x34
        byte3 = (n >> 24) & 0xFF  # 0x12 (가장 높은 바이트)
        
        # 2. 바이트 순서를 역순으로 조립합니다.
        # 낮은 자리에 있던 byte0을 가장 높은 자리(24비트 왼쪽)로 보냅니다.
        restored = (byte0 << 24) | (byte1 << 16) | (byte2 << 8) | byte3
        
        # 결과 출력
        print(restored)
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()

############################################################################


