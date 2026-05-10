#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

// 최대 수위 1000 + 여유분
const int SZ = 1005;

// 구간 넓이 계산을 O(log H)에 처리하기 위한 5개의 펜윅 트리
long double count_tree[SZ];
long double sum_y_tree[SZ];
long double A_tree[SZ];
long double B_tree[SZ];
long double C_tree[SZ];

// 펜윅 트리 업데이트 (점 추가)
void add_bit(long double* tree, int i, long double delta) {
    for (; i < SZ; i += i & -i) {
        tree[i] += delta;
    }
}

// 펜윅 트리 쿼리 (누적합)
long double query_bit(const long double* tree, int i) {
    long double sum = 0;
    for (; i > 0; i -= i & -i) {
        sum += tree[i];
    }
    return sum;
}

// 구간의 높이가 변할 때 트리를 갱신하는 함수
void update_segment(int y1, int y2, long double sign) {
    int ymin = min(y1, y2);
    int ymax = max(y1, y2);

    // 1. 완전히 잠긴 구간 (h >= ymax)
    // 인덱스는 h + 1이므로 ymax + 1부터 끝까지 적용
    add_bit(count_tree, ymax + 1, sign * 1.0);
    add_bit(sum_y_tree, ymax + 1, sign * (y1 + y2) / 2.0);

    // 2. 부분적으로 잠긴 구간 (ymin < h < ymax)
    if (ymax > ymin) {
        long double D = ymax - ymin;
        
        // 이차 방정식 계수 도출: Area = A*h^2 + B*h + C
        long double A = sign / (2.0 * D);
        long double B = -sign * ymin / D;
        long double C = sign * (long double)ymin * ymin / (2.0 * D);

        // h의 범위: [ymin + 1, ymax - 1]
        // 펜윅 트리 인덱스 (h + 1): [ymin + 2, ymax]
        add_bit(A_tree, ymin + 2, A);
        add_bit(A_tree, ymax + 1, -A);

        add_bit(B_tree, ymin + 2, B);
        add_bit(B_tree, ymax + 1, -B);

        add_bit(C_tree, ymin + 2, C);
        add_bit(C_tree, ymax + 1, -C);
    }
}

int main() {
    // 입출력 속도 극한 최적화
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<int> H(N);
    for (int i = 0; i < N; ++i) {
        cin >> H[i];
    }

    // 1. 초기 바닥 상태 갱신
    for (int i = 0; i < N - 1; ++i) {
        update_segment(H[i], H[i+1], 1.0);
    }

    // 소수점 셋째 자리까지 고정 출력 설정
    cout << fixed << setprecision(3);

    for (int i = 0; i < M; ++i) {
        char cmd;
        cin >> cmd;
        
        if (cmd == 'Q') {
            int h;
            cin >> h;

            int q_idx = h + 1;
            
            // 각 트리의 누적값 조회
            long double c = query_bit(count_tree, q_idx);
            long double sy = query_bit(sum_y_tree, q_idx);
            long double a = query_bit(A_tree, q_idx);
            long double b = query_bit(B_tree, q_idx);
            long double const_c = query_bit(C_tree, q_idx);

            // 전체 넓이 계산 (완전히 잠긴 영역 + 부분적으로 잠긴 다항식 영역)
            long double ans = (c * h - sy) + (a * h * h + b * h + const_c);
            
            // 음수 0(-0.000) 출력 방지
            if (ans < 0.0) ans = 0.0;

            cout << ans << "\n";
            
        } else if (cmd == 'U') {
            int k, new_h;
            cin >> k >> new_h;

            // 기존 높이가 미치던 영향 제거
            if (k > 0) update_segment(H[k-1], H[k], -1.0);
            if (k < N - 1) update_segment(H[k], H[k+1], -1.0);

            // 높이 업데이트
            H[k] = new_h;

            // 새로운 높이의 영향 추가
            if (k > 0) update_segment(H[k-1], H[k], 1.0);
            if (k < N - 1) update_segment(H[k], H[k+1], 1.0);
        }
    }

    return 0;
}





