#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

const int MAXN = 100005;
const int OFFSET = 100000; // 음수 인덱스 방지용 오프셋

vector<pair<int, int>> adj[MAXN];
int sz[MAXN];
bool removed[MAXN];
int cnt[2 * MAXN][2]; // [거리][타입: 0은 중간0 없음, 1은 중간0 있음]
int seen[2 * MAXN];   // DFS 중 현재 경로에서 나타난 거리 빈도
int N;
ll ans = 0;

// 서브트리 크기 계산
void get_sz(int u, int p) {
    sz[u] = 1;
    for (auto& edge : adj[u]) {
        int v = edge.first;
        if (v != p && !removed[v]) {
            get_sz(v, u);
            sz[u] += sz[v];
        }
    }
}

// 무게 중심(Centroid) 찾기
int get_centroid(int u, int p, int total) {
    for (auto& edge : adj[u]) {
        int v = edge.first;
        if (v != p && !removed[v] && sz[v] > total / 2) {
            return get_centroid(v, u, total);
        }
    }
    return u;
}

struct NodeData {
    int dist;
    bool type;
};

// 현재 Centroid로부터의 거리와 중간에 합이 0이 되는 지점이 있는지 수집
void collect(int u, int p, int d, vector<NodeData>& nodes) {
    bool t = (seen[d + OFFSET] > 0);
    nodes.push_back({d, t});

    seen[d + OFFSET]++;
    for (auto& edge : adj[u]) {
        int v = edge.first;
        int w = (edge.second == 1 ? 1 : -1);
        if (v != p && !removed[v]) {
            collect(v, u, d + w, nodes);
        }
    }
    seen[d + OFFSET]--;
}

void decompose(int u) {
    get_sz(u, -1);
    if (sz[u] < 3 && u == 1 && N < 3) return; // 노드가 너무 적으면 종료
    int c = get_centroid(u, -1, sz[u]);
    removed[c] = true;

    vector<int> active_dists; // 리셋할 거리 목록

    for (auto& edge : adj[c]) {
        int v = edge.first;
        int w = (edge.second == 1 ? 1 : -1);
        if (!removed[v]) {
            vector<NodeData> subtree_nodes;
            collect(v, c, w, subtree_nodes);
            
            for (auto& node : subtree_nodes) {
                int target = -node.dist;
                if (node.dist == 0) {
                    // Centroid가 중간 지점인 경우 (u-C-v)
                    ans += cnt[OFFSET][0] + cnt[OFFSET][1];
                    // Centroid가 도달하기 전 중간 지점이 있었던 경우 (u-M-C)
                    if (node.type) ans++;
                } else {
                    // 일반적인 경우: u쪽이나 v쪽 서브트리에 중간 지점이 있어야 함
                    if (node.type) {
                        ans += cnt[target + OFFSET][0] + cnt[target + OFFSET][1];
                    } else {
                        ans += cnt[target + OFFSET][1];
                    }
                }
            }

            for (auto& node : subtree_nodes) {
                cnt[node.dist + OFFSET][node.type]++;
                active_dists.push_back(node.dist);
            }
        }
    }

    // 다음 Centroid를 위해 카운트 배열 초기화
    for (int d : active_dists) {
        cnt[d + OFFSET][0] = 0;
        cnt[d + OFFSET][1] = 0;
    }
    cnt[OFFSET][0] = 0;
    cnt[OFFSET][1] = 0;

    for (auto& edge : adj[c]) {
        if (!removed[edge.first]) {
            decompose(edge.first);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;
    for (int i = 0; i < N - 1; i++) {
        int u, v, c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    decompose(1);

    cout << ans << endl;

    return 0;
}

