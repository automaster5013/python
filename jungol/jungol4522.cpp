#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef __int128_t int128;

struct Point {
    ll x, h, a, b;
};

struct Line {
    ll m;
    int128 c;
    int128 eval(ll x) { return (int128)m * x + c; }
};

// CHT 교점 비교 (is_redundant): X(l1,l2) >= X(l2,l3) 확인
bool is_redundant(Line l1, Line l2, Line l3) {
    return (int128)(l2.c - l1.c) * (l2.m - l3.m) >= (int128)(l3.c - l2.c) * (l1.m - l2.m);
}

void solve() {
    int N;
    if (!(cin >> N)) return;

    vector<Point> pts(N);
    for (int i = 0; i < N; ++i) {
        cin >> pts[i].x >> pts[i].h;
        pts[i].a = pts[i].h - pts[i].x;
        pts[i].b = pts[i].h + pts[i].x;
    }

    // a 내림차순, b 내림차순 정렬 후 불필요한 점 제거
    sort(pts.begin(), pts.end(), [](const Point& p1, const Point& p2) {
        if (p1.a != p2.a) return p1.a > p2.a;
        return p1.b > p2.b;
    });

    vector<Point> filtered;
    ll max_b = -1e18; 
    for (int i = 0; i < N; ++i) {
        if (pts[i].b > max_b) {
            filtered.push_back(pts[i]);
            max_b = pts[i].b;
        }
    }

    int M = filtered.size();
    vector<int128> dp(M + 1, 0);
    vector<Line> dq;
    int head = 0;

    // 초기 직선 추가 (j=0)
    dq.push_back({2 * filtered[0].a, (int128)filtered[0].a * filtered[0].a});

    for (int i = 1; i <= M; ++i) {
        ll cur_x = filtered[i - 1].b;
        
        // 최적의 직선을 찾아 DP 값 계산
        while (dq.size() - head >= 2 && dq[head].eval(cur_x) >= dq[head + 1].eval(cur_x)) head++;
        dp[i] = (int128)cur_x * cur_x + dq[head].eval(cur_x);

        if (i < M) {
            Line next_line = {2 * filtered[i].a, dp[i] + (int128)filtered[i].a * filtered[i].a};
            while (dq.size() - head >= 2 && is_redundant(dq[dq.size() - 2], dq.back(), next_line)) dq.pop_back();
            dq.push_back(next_line);
        }
    }

    // 정밀도 유지를 위해 정수/소수부 직접 출력
    ll integer_part = (ll)(dp[M] / 4);
    int frac = (int)(dp[M] % 4);
    string frac_str[] = {"00", "25", "50", "75"};
    cout << integer_part << "." << frac_str[frac] << "\n";
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int T; cin >> T;
    while (T--) solve();
    return 0;
}





