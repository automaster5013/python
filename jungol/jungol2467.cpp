#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, w;
};

bool compareEdges(const Edge& a, const Edge& b) {
    return a.w > b.w; // 내림차순 정렬
}

int parent[100001];
long long sz[100001];

int find(int i) {
    if (parent[i] == i) return i;
    return parent[i] = find(parent[i]);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<Edge> edges(M);
    for (int i = 0; i < M; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    sort(edges.begin(), edges.end(), compareEdges);

    for (int i = 1; i <= N; i++) {
        parent[i] = i;
        sz[i] = 1;
    }

    long long current_pairs = 0;
    long long total_cost = 0;
    const long long MOD = 1000000000;

    for (int i = 0; i < M; i++) {
        int root_u = find(edges[i].u);
        int root_v = find(edges[i].v);

        if (root_u != root_v) {
            current_pairs += (sz[root_u] * sz[root_v]);
            // Union
            parent[root_u] = root_v;
            sz[root_v] += sz[root_u];
        }
        
        // 현재 연결된 모든 쌍에 대해 현재 간선 가중치 w_i가 기여함
        total_cost = (total_cost + (current_pairs % MOD) * edges[i].w) % MOD;
    }

    cout << total_cost << endl;

    return 0;
}


