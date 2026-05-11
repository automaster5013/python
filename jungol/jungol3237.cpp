#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

const int MAXN = 300005;

int N1, N2, K;

int p_S[MAXN], p_T[MAXN];
set<int> children_S[MAXN], children_T[MAXN];
int leaf_count_S[MAXN], leaf_count_T[MAXN];
map<int, int> parent_freq_S[MAXN], parent_freq_T[MAXN];

bool in_Q_S[MAXN], in_Q_T[MAXN];
queue<pair<int, int>> Q; // {0: S, 1: T}, node_id

int active_leaves;

// S 트리 압축 (자식이 1명인 노드 제거)
void compress_initial(int N, set<int>* children, int* parent) {
    vector<int> order;
    queue<int> q;
    for (int i = 1; i <= N; ++i) {
        if (parent[i] == 0) q.push(i);
    }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int c : children[u]) q.push(c);
    }
    for (int i = order.size() - 1; i >= 0; --i) {
        int u = order[i];
        if (children[u].size() == 1 && u > K) {
            int c = *children[u].begin();
            int p = parent[u];
            if (p != 0) {
                children[p].erase(u);
                children[p].insert(c);
                parent[c] = p;
            } else {
                parent[c] = 0;
            }
            children[u].clear();
        }
    }
}

void check_ready_S(int u) {
    if (u == 0 || children_S[u].empty() || in_Q_S[u]) return;
    if (leaf_count_S[u] == children_S[u].size() && parent_freq_S[u].size() == 1) {
        in_Q_S[u] = true;
        Q.push({0, u});
    }
}

void check_ready_T(int v) {
    if (v == 0 || children_T[v].empty() || in_Q_T[v]) return;
    if (leaf_count_T[v] == children_T[v].size() && parent_freq_T[v].size() == 1) {
        in_Q_T[v] = true;
        Q.push({1, v});
    }
}

void change_p_S(int leaf, int new_p) {
    int old_p = p_S[leaf];
    int v = p_T[leaf];
    if (v != 0) {
        parent_freq_T[v][old_p]--;
        if (parent_freq_T[v][old_p] == 0) parent_freq_T[v].erase(old_p);
        parent_freq_T[v][new_p]++;
        if (parent_freq_T[v].size() == 1) check_ready_T(v);
    }
    p_S[leaf] = new_p;
}

void change_p_T(int leaf, int new_p) {
    int old_p = p_T[leaf];
    int u = p_S[leaf];
    if (u != 0) {
        parent_freq_S[u][old_p]--;
        if (parent_freq_S[u][old_p] == 0) parent_freq_S[u].erase(old_p);
        parent_freq_S[u][new_p]++;
        if (parent_freq_S[u].size() == 1) check_ready_S(u);
    }
    p_T[leaf] = new_p;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N1 >> N2 >> K)) return 0;
    active_leaves = K;

    for (int i = 1; i <= N1; ++i) {
        cin >> p_S[i];
        if (p_S[i] != 0) children_S[p_S[i]].insert(i);
    }
    for (int i = 1; i <= N2; ++i) {
        cin >> p_T[i];
        if (p_T[i] != 0) children_T[p_T[i]].insert(i);
    }

    compress_initial(N1, children_S, p_S);
    compress_initial(N2, children_T, p_T);

    for (int u = K + 1; u <= N1; ++u) {
        for (int c : children_S[u]) {
            if (c <= K) {
                leaf_count_S[u]++;
                parent_freq_S[u][p_T[c]]++;
            }
        }
    }
    for (int v = K + 1; v <= N2; ++v) {
        for (int c : children_T[v]) {
            if (c <= K) {
                leaf_count_T[v]++;
                parent_freq_T[v][p_S[c]]++;
            }
        }
    }

    for (int u = K + 1; u <= N1; ++u) check_ready_S(u);
    for (int v = K + 1; v <= N2; ++v) check_ready_T(v);

    while (!Q.empty()) {
        auto [type, node] = Q.front(); Q.pop();

        if (type == 0) {
            int u = node;
            in_Q_S[u] = false;
            if (children_S[u].empty() || leaf_count_S[u] != children_S[u].size() || parent_freq_S[u].size() != 1) continue;

            int c_rep = *children_S[u].begin();
            int v = p_T[c_rep];

            vector<int> to_remove;
            for (int c : children_S[u]) if (c != c_rep) to_remove.push_back(c);

            for (int c : to_remove) {
                p_S[c] = 0;
                children_T[v].erase(c);
                leaf_count_T[v]--;
                parent_freq_T[v][u]--;
                if (parent_freq_T[v][u] == 0) parent_freq_T[v].erase(u);
            }
            active_leaves -= to_remove.size();
            children_S[u].clear(); 

            int p_u = p_S[u];
            if (p_u != 0) {
                children_S[p_u].erase(u);
                children_S[p_u].insert(c_rep);
                leaf_count_S[p_u]++;
                parent_freq_S[p_u][v]++;
                change_p_S(c_rep, p_u);
                check_ready_S(p_u);
            } else {
                change_p_S(c_rep, 0);
            }

            if (children_T[v].size() == 1) {
                int p_v = p_T[v];
                if (p_v != 0) {
                    children_T[p_v].erase(v);
                    children_T[p_v].insert(c_rep);
                    leaf_count_T[p_v]++;
                    parent_freq_T[p_v][p_S[c_rep]]++;
                    change_p_T(c_rep, p_v);
                    check_ready_T(p_v);
                } else {
                    change_p_T(c_rep, 0);
                }
                children_T[v].clear();
            } else if (children_T[v].size() > 1) {
                check_ready_T(v);
            }

        } else {
            int v = node;
            in_Q_T[v] = false;
            if (children_T[v].empty() || leaf_count_T[v] != children_T[v].size() || parent_freq_T[v].size() != 1) continue;

            int c_rep = *children_T[v].begin();
            int u = p_S[c_rep];

            vector<int> to_remove;
            for (int c : children_T[v]) if (c != c_rep) to_remove.push_back(c);

            for (int c : to_remove) {
                p_T[c] = 0;
                children_S[u].erase(c);
                leaf_count_S[u]--;
                parent_freq_S[u][v]--;
                if (parent_freq_S[u][v] == 0) parent_freq_S[u].erase(v);
            }
            active_leaves -= to_remove.size();
            children_T[v].clear();

            int p_v = p_T[v];
            if (p_v != 0) {
                children_T[p_v].erase(v);
                children_T[p_v].insert(c_rep);
                leaf_count_T[p_v]++;
                parent_freq_T[p_v][u]++;
                change_p_T(c_rep, p_v);
                check_ready_T(p_v);
            } else {
                change_p_T(c_rep, 0);
            }

            if (children_S[u].size() == 1) {
                int p_u = p_S[u];
                if (p_u != 0) {
                    children_S[p_u].erase(u);
                    children_S[p_u].insert(c_rep);
                    leaf_count_S[p_u]++;
                    parent_freq_S[p_u][p_T[c_rep]]++;
                    change_p_S(c_rep, p_u);
                    check_ready_S(p_u);
                } else {
                    change_p_S(c_rep, 0);
                }
                children_S[u].clear();
            } else if (children_S[u].size() > 1) {
                check_ready_S(u);
            }
        }
    }

    if (active_leaves == 1) cout << "YES\n";
    else cout << "NO\n";

    return 0;
}




