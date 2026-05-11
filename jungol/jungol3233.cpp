#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    int id;
};

// CCW 연산
long long CCW(Point a, Point b, Point c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

// 각도 정렬을 위한 사분면 판별
int quad(long long dx, long long dy) {
    if (dy >= 0 && dx > 0) return 1;
    if (dy > 0 && dx <= 0) return 2;
    if (dy <= 0 && dx < 0) return 3;
    if (dy < 0 && dx >= 0) return 4;
    return 0;
}

// 정렬 속도 극한 향상을 위한 사전 계산 구조체
struct VecInfo {
    int id;
    long long dx, dy;
    int q;
};

// 캐시 친화적(Cache-Friendly) 메모리 배치
short dpT_in[3005][3005];
short dpV_in[3005][3005];
short prevT[3005][3005];
short prevV[3005][3005];

Point P[3005];
int grp[3005]; // 일직선 관통 방지용 각도 그룹
VecInfo vec[3005];

int A_prime[6005];
long long dx_s[6005];
long long dy_s[6005];

int mq_L[6005];
int mq_R[6005];

// 1차원 캐싱된 배열만을 사용하여 O(1) 초고속 외적
inline long long cross_prod(int u, int v) {
    return dx_s[u] * dy_s[v] - dy_s[u] * dx_s[v];
}

int main() {
    // 입출력 속도 극한 최적화
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    int min_idx = 0;
    for (int i = 0; i < N; ++i) {
        cin >> P[i].x >> P[i].y;
        P[i].id = i;
        if (i > 0) {
            // 가장 남쪽(발뒤꿈치) 찾기
            if (P[i].y < P[min_idx].y || (P[i].y == P[min_idx].y && P[i].x < P[min_idx].x)) {
                min_idx = i;
            }
        }
    }

    swap(P[0], P[min_idx]);

    // 반시계 방향 각도 정렬
    sort(P + 1, P + N, [&](const Point& a, const Point& b) {
        long long cr = CCW(P[0], a, b);
        if (cr != 0) return cr > 0;
        long long distA = (a.x - P[0].x) * (a.x - P[0].x) + (a.y - P[0].y) * (a.y - P[0].y);
        long long distB = (b.x - P[0].x) * (b.x - P[0].x) + (b.y - P[0].y) * (b.y - P[0].y);
        return distA < distB;
    });

    // 일직선(Collinear)상에 있는 점들을 같은 그룹으로 묶음
    grp[0] = 0;
    if (N > 1) grp[1] = 1;
    for (int i = 2; i < N; ++i) {
        if (CCW(P[0], P[i - 1], P[i]) == 0) grp[i] = grp[i - 1];
        else grp[i] = grp[i - 1] + 1;
    }

    // DP 배열 초기화
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            dpT_in[i][j] = -1;
            dpV_in[i][j] = -1;
        }
    }

    // 시작점 세팅: 발뒤꿈치(0)에서 첫 발가락(j)으로
    for (int j = 1; j < N; ++j) {
        dpT_in[j][0] = 1;
    }

    for (int j = 1; j < N; ++j) {
        int M = 0;
        for (int i = 0; i < N; ++i) {
            if (i != j) {
                vec[M].id = i;
                vec[M].dx = P[i].x - P[j].x;
                vec[M].dy = P[i].y - P[j].y;
                vec[M].q = quad(vec[M].dx, vec[M].dy);
                M++;
            }
        }

        sort(vec, vec + M, [](const VecInfo& a, const VecInfo& b) {
            if (a.q != b.q) return a.q < b.q;
            long long cr = a.dx * b.dy - a.dy * b.dx;
            return cr > 0;
        });

        // 1차원 캐싱 배열 복사 (원형 스위핑 처리용 2배 확장)
        for (int i = 0; i < M; ++i) {
            A_prime[i] = vec[i].id;
            A_prime[i + M] = vec[i].id;
            dx_s[i] = vec[i].dx;
            dy_s[i] = vec[i].dy;
            dx_s[i + M] = vec[i].dx;
            dy_s[i + M] = vec[i].dy;
        }

        int L1 = 0, L2 = 0;
        int head_L = 0, tail_L = 0, added_L = 0;
        int head_R = 0, tail_R = 0;

        for (int q = 0; q < 2 * M; ++q) {
            // L1: 처음으로 CCW >= 0 이 되는 지점
            L1 = max(L1, q - M + 1);
            while (L1 < q && cross_prod(L1, q) < 0) {
                L1++;
            }
            
            // L2: 처음으로 CCW > 0 이 되는 지점
            L2 = max(L2, L1);
            while (L2 < q && cross_prod(L2, q) <= 0) {
                L2++;
            }

            // --- MQ_Left (좌회전 구간) 유지 ---
            while (added_L < L1) {
                int x = A_prime[added_L];
                if (x < j && dpT_in[j][x] != -1) {
                    short val = dpT_in[j][x];
                    while (tail_L > head_L && dpT_in[j][A_prime[mq_L[tail_L - 1]]] <= val) tail_L--;
                    mq_L[tail_L++] = added_L;
                }
                added_L++;
            }
            while (head_L < tail_L && mq_L[head_L] < q - M + 1) head_L++;

            // --- MQ_Right (우회전 구간) 유지 ---
            if (q > 0) {
                int added_R = q - 1;
                int x = A_prime[added_R];
                if (x < j && dpV_in[j][x] != -1) {
                    short val = dpV_in[j][x];
                    while (tail_R > head_R && dpV_in[j][A_prime[mq_R[tail_R - 1]]] <= val) tail_R--;
                    mq_R[tail_R++] = added_R;
                }
            }
            while (head_R < tail_R && mq_R[head_R] < L2) head_R++;

            // --- DP 전이 (일직선 관통 방지 규칙 적용) ---
            int k = A_prime[q];
            if (k > j && grp[k] > grp[j]) { 
                
                // 1. 발가락(Toe) -> 골(Valley) : 좌회전(MQ_L)
                if (head_L < tail_L) {
                    int best_x = A_prime[mq_L[head_L]];
                    if (dpT_in[j][best_x] > dpV_in[k][j]) {
                        dpV_in[k][j] = dpT_in[j][best_x];
                        prevV[j][k] = best_x;
                    }
                }

                // 2. 골(Valley) -> 발가락(Toe) : 우회전(MQ_R)
                if (head_R < tail_R) {
                    int best_x = A_prime[mq_R[head_R]];
                    if (dpV_in[j][best_x] != -1 && dpV_in[j][best_x] + 1 > dpT_in[k][j]) {
                        dpT_in[k][j] = dpV_in[j][best_x] + 1;
                        prevT[j][k] = best_x;
                    }
                }
            }
        }
    }

    int max_toes = 0;
    int best_cT = -1, best_cV = -1;

    for (int i = 1; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (dpT_in[i][j] > max_toes) {
                max_toes = dpT_in[i][j];
                best_cT = i;
                best_cV = j;
            }
        }
    }

    // 조건: 최소 발가락 2개 이상
    if (max_toes < 2) {
        cout << 0 << "\n";
        return 0;
    }

    // 역추적(Backtracking)을 통한 경로 복원
    vector<int> path;
    int cT = best_cT, cV = best_cV;
    while (cV != 0) {
        path.push_back(cT);
        path.push_back(cV);
        int pT = prevT[cV][cT]; // 현재 Valley의 원인이 된 이전 Toe
        int pV = prevV[pT][cV]; // 이전 Toe의 원인이 된 이전 Valley
        cT = pT; cV = pV;
    }
    path.push_back(cT);
    path.push_back(0); // 시작점 발뒤꿈치

    reverse(path.begin(), path.end());

    cout << path.size() << "\n";
    for (size_t i = 0; i < path.size(); ++i) {
        cout << P[path[i]].x << " " << P[path[i]].y << "\n";
    }

    return 0;
}





