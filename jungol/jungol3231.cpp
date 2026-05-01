#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Node {
    int h, r, c;
    bool operator>(const Node& other) const { return h > other.h; }
};

int N, M, H;
int dist[1005][1005];
int row_holes[1005][1005]; // 가로 벽 구멍 (상하 연결)
int col_holes[1005][1005]; // 세로 벽 구멍 (좌우 연결)

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> M >> H)) return 0;

    // 가로 벽 입력 (N+1개)
    for (int i = 0; i <= N; ++i) {
        for (int j = 0; j < M; ++j) cin >> row_holes[i][j];
    }
    // 세로 벽 입력 (N개)
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j <= M; ++j) cin >> col_holes[i][j];
    }

    priority_queue<Node, vector<Node>, greater<Node>> pq;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) dist[i][j] = H;
    }

    // 외곽 벽 구멍 초기화
    for (int j = 0; j < M; ++j) {
        if (row_holes[0][j] != -1) { // 맨 위쪽
            dist[0][j] = min(dist[0][j], row_holes[0][j]);
            pq.push({dist[0][j], 0, j});
        }
        if (row_holes[N][j] != -1) { // 맨 아래쪽
            dist[N - 1][j] = min(dist[N - 1][j], row_holes[N][j]);
            pq.push({dist[N - 1][j], N - 1, j});
        }
    }
    for (int i = 0; i < N; ++i) {
        if (col_holes[i][0] != -1) { // 맨 왼쪽
            dist[i][0] = min(dist[i][0], col_holes[i][0]);
            pq.push({dist[i][0], i, 0});
        }
        if (col_holes[i][M] != -1) { // 맨 오른쪽
            dist[i][M - 1] = min(dist[i][M - 1], col_holes[i][M]);
            pq.push({dist[i][M - 1], i, M - 1});
        }
    }

    // 다익스트라 전파
    while (!pq.empty()) {
        Node cur = pq.top(); pq.pop();
        if (cur.h > dist[cur.r][cur.c]) continue;

        int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
        for (int i = 0; i < 4; ++i) {
            int nr = cur.r + dr[i], nc = cur.c + dc[i];
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

            int hole_h = -1;
            if (i == 0) hole_h = row_holes[cur.r][cur.c];      // 상
            else if (i == 1) hole_h = row_holes[cur.r + 1][cur.c]; // 하
            else if (i == 2) hole_h = col_holes[cur.r][cur.c];      // 좌
            else if (i == 3) hole_h = col_holes[cur.r][cur.c + 1];  // 우

            if (hole_h != -1) {
                int next_h = max(cur.h, hole_h);
                if (next_h < dist[nr][nc]) {
                    dist[nr][nc] = next_h;
                    pq.push({next_h, nr, nc});
                }
            }
        }
    }

    long long total_volume = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) total_volume += dist[i][j];
    }
    cout << total_volume << endl;

    return 0;
}



