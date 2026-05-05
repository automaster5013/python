#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

/**
 * dp[slot_idx][torque][weights_mask]
 * slot_idx: 0-9 (L5, L4, L3, L2, L1, R1, R2, R3, R4, R5)
 * torque: -135 to 135 (offset 150 사용)
 * weights_mask: 추 사용 여부 (최대 2^9)
 */
long long dp[11][301][512];
int P[] = {5, 4, 3, 2, 1, -1, -2, -3, -4, -5};
int offset = 150;

int main() {
    // 입출력 속도 향상
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> weights(n);
    for (int i = 0; i < n; ++i) cin >> weights[i];
    long long k;
    cin >> k;

    // DP 테이블 초기화 (뒤쪽부터 계산)
    // 모든 눈금을 다 확인했을 때 토크 합이 0(offset)이면 1가지 성공 케이스
    for (int m = 0; m < (1 << n); ++m) {
        dp[10][offset][m] = 1;
    }

    // DP 진행: i번째 눈금에서 가능한 선택(0 또는 무게)을 모두 합산
    for (int i = 9; i >= 0; --i) {
        for (int t = 0; t <= 300; ++t) {
            for (int m = 0; m < (1 << n); ++m) {
                // 현재 눈금을 비워두는 경우 (0)
                dp[i][t][m] += dp[i + 1][t][m];
                
                // 현재 눈금에 추를 놓는 경우
                for (int j = 0; j < n; ++j) {
                    if (!(m & (1 << j))) {
                        int nt = t + weights[j] * P[i];
                        if (nt >= 0 && nt <= 300) {
                            dp[i][t][m] += dp[i + 1][nt][m | (1 << j)];
                        }
                    }
                }
            }
        }
    }

    // 총 가능한 평형정수 개수 확인 및 k값 보정
    long long total = dp[0][offset][0];
    if (k >= total) k = total - 1;

    // k번째 평형정수 구성 복원
    int cur_t = offset;
    int cur_m = 0;
    string res = "";

    for (int i = 0; i < 10; ++i) {
        // 평형정수를 작게 유지하기 위해 '0'을 먼저 시도
        long long cnt = dp[i + 1][cur_t][cur_m];
        if (k < cnt) {
            res += '0';
        } else {
            k -= cnt;
            bool found = false;
            // '0'이 아니면 무게가 작은 추부터 순서대로 시도
            for (int j = 0; j < n; ++j) {
                if (!(cur_m & (1 << j))) {
                    int nt = cur_t + weights[j] * P[i];
                    if (nt >= 0 && nt <= 300) {
                        long long ways = dp[i + 1][nt][cur_m | (1 << j)];
                        if (k < ways) {
                            res += (char)('0' + weights[j]);
                            cur_t = nt;
                            cur_m |= (1 << j);
                            found = true;
                            break;
                        }
                        k -= ways;
                    }
                }
            }
        }
    }

    // 앞부분의 불필요한 0 제거 및 출력
    size_t first = res.find_first_not_of('0');
    if (first == string::npos) {
        cout << "0\n";
    } else {
        cout << res.substr(first) << "\n";
    }

    return 0;
}


