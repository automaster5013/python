#include <iostream>

using namespace std;

int main() {
    // 입출력 속도 극한 최적화
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    // XOR 연산을 위해 0-based 인덱스로 변환
    int start_m = M - 1; 

    // N개의 방을 2개씩 짝지어서 출력 (O(N) 탐색)
    for (int i = 0; i < N / 2; ++i) {
        // 기본 뼈대 수열 생성: 왼쪽 끝(i)과 오른쪽 끝(N - 1 - i)을 번갈아 선택
        int first = i;
        int second = N - 1 - i;

        // 선택된 기본 수열에 목표 시작점(start_m)을 XOR하여 변환 후 1-based로 복구하여 출력
        cout << (first ^ start_m) + 1 << " ";
        cout << (second ^ start_m) + 1 << " ";
    }
    
    cout << "\n";

    return 0;
}




