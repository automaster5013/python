#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

// 최대 가능한 총점 계산: (150 * 151 / 2) * 100 = 1,132,500
const int MAX_SCORE = 1132501;

// 메모리 사용량을 고려하여 전역 변수(또는 static)로 선언
static bitset<MAX_SCORE> dp[155];

int main() {
    // 빠른 입출력 설정
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> S(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> S[i];
    }

    long long K;
    cin >> K;

    // 1. 연속 정답 스트릭 점수 v[j][i] 미리 계산
    // v[j][i]는 j번부터 i번 문항까지 모두 맞았을 때의 해당 구간 점수 합
    vector<vector<int>> v(N + 1, vector<int>(N + 1, 0));
    for (int j = 1; j <= N; ++j) {
        int streak_score = 0;
        int current_sum = 0;
        for (int i = j; i <= N; ++i) {
            current_sum += S[i];
            streak_score += current_sum;
            v[j][i] = streak_score;
        }
    }

    // 2. DP 수행
    // dp[i]는 i번째 문항이 '틀림(X)'일 때 가능한 총점 집합
    dp[0][0] = 1; // 0번 문항(가상)을 틀렸을 때 초기 점수는 0점

    for (int i = 1; i <= N + 1; ++i) {
        // i번 문항이 X이고, i-1번 문항도 X인 경우
        dp[i] = dp[i - 1];
        
        // i번 문항이 X이고, j번부터 i-1번까지 ○ 스트릭인 경우
        for (int j = 1; j < i; ++j) {
            // j-1번 문항은 반드시 X였어야 함
            dp[i] |= (dp[j - 1] << v[j][i - 1]);
        }
    }

    // 3. K 이상의 값 중 불가능한 가장 작은 점수 M 찾기
    for (long long m = K; ; ++m) {
        // 최대 점수를 초과하거나, dp[N+1] 비트가 꺼져 있으면 불가능한 점수
        if (m >= MAX_SCORE || !dp[N + 1][m]) {
            cout << m << "\n";
            break;
        }
    }

    return 0;
}



