#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // 입출력 속도 극한 최적화
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, P, V;
    if (!(cin >> N >> P >> V)) return 0;

    // 1명일 때는 투표할 필요가 없으므로 0분 소요
    if (N <= 1) {
        cout << 0 << "\n";
        return 0;
    }

    // f[i] : i분 동안 최대로 처리할 수 있는 국회의원 수
    vector<long long> f;
    f.push_back(1); // 0분일 때 처리가능한 최대 인원은 1명

    // k(그룹 수)의 상한선 지정 (수학적 증명을 통한 탐색 범위 최적화)
    int max_k = 10 + 2 * V / P;

    // 1분부터 시작하여 최대 인원수가 N 이상이 될 때까지 증가
    for (int i = 1; ; ++i) {
        long long cur = f.back(); // 1분을 아무것도 안하고 기다릴 경우
        
        for (int k = 2; k <= max_k; ++k) {
            int prev_t = i - k * P - V;
            
            // 더 이상 이전 시간이 존재하지 않으면 k를 늘려도 음수이므로 탐색 종료
            if (prev_t < 0) break; 
            
            long long val = k * f[prev_t];
            if (val > cur) {
                cur = val;
            }
        }
        
        // 시간 i에 처리가능한 최대 인원이 N명 이상이 되면 바로 해당 시간 출력 후 종료
        if (cur >= N) {
            cout << i << "\n";
            return 0;
        }
        
        f.push_back(cur);
    }

    return 0;
}





