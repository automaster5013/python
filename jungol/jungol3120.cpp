static int* sorted_data;
static int data_size;

void initUser(int nSize, int *arr) {
    data_size = nSize;
    sorted_data = arr;

    // 부호 없는 정수로 해석하여 비트 연산 속도 최적화
    unsigned int *data = (unsigned int*)arr;
    unsigned int *temp = new unsigned int[nSize];

    // 1. 음수 처리 트릭: 부호 비트(MSB)를 반전시켜 음수를 양수보다 작은 범위로 매핑
    // 이렇게 하면 전체 범위를 0 ~ 2^32-1의 양수처럼 정렬할 수 있습니다.
    for (int i = 0; i < nSize; i++) data[i] ^= 0x80000000;

    // --- Pass 1: 하위 16비트 정렬 ---
    int count[65536] = {0};
    for (int i = 0; i < nSize; i++) count[data[i] & 0xFFFF]++;
    for (int i = 1; i < 65536; i++) count[i] += count[i - 1];
    // 뒤에서부터 채워야 스테이블(Stable) 정렬이 유지됩니다.
    for (int i = nSize - 1; i >= 0; i--) temp[--count[data[i] & 0xFFFF]] = data[i];

    // --- Pass 2: 상위 16비트 정렬 ---
    for (int i = 0; i < 65536; i++) count[i] = 0;
    for (int i = 0; i < nSize; i++) count[(temp[i] >> 16) & 0xFFFF]++;
    for (int i = 1; i < 65536; i++) count[i] += count[i - 1];
    for (int i = nSize - 1; i >= 0; i--) data[--count[(temp[i] >> 16) & 0xFFFF]] = temp[i];

    // 2. 부호 비트 원상 복구
    for (int i = 0; i < nSize; i++) data[i] ^= 0x80000000;

    delete[] temp;
}

int query(int idx) {
    // 1-base 인덱스를 0-base로 변환하여 즉시 반환
    return sorted_data[idx - 1];
}

