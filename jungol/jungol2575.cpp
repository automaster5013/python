#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    // 입출력 속도 극한 최적화
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k, p;
    if (!(cin >> n >> k >> p)) return 0;

    // 2차원 vector 대신 1차원 배열(CSR)을 사용하여 메모리 할당 오버헤드 완벽 제거
    vector<int> head(k, -1), to(p), nxt(p);
    vector<int> r_head(k, -1), r_to(p), r_nxt(p);
    
    vector<int> in_deg(k, 0);
    vector<int> out_deg(k, 0);

    for (int i = 0; i < p; ++i) {
        int a, b;
        cin >> a >> b;
        
        // 순방향 간선 추가 (a -> b)
        to[i] = b;
        nxt[i] = head[a];
        head[a] = i;
        in_deg[b]++;

        // 역방향 간선 추가 (b -> a)
        r_to[i] = a;
        r_nxt[i] = r_head[b];
        r_head[b] = i;
        out_deg[a]++;
    }

    // =========================================================
    // 1. 최댓값을 만드는 카드 배열 구하기
    // =========================================================
    vector<int> max_C(k);
    priority_queue<int, vector<int>, greater<int>> min_heap_max;

    for (int i = 0; i < k; ++i) {
        if (out_deg[i] == 0) {
            min_heap_max.push(i);
        }
    }

    int val_max = n - k; 
    while (!min_heap_max.empty()) {
        int u = min_heap_max.top();
        min_heap_max.pop();
        max_C[u] = val_max++;
        
        // CSR 구조를 이용한 초고속 역방향 인접 노드 탐색
        for (int e = r_head[u]; e != -1; e = r_nxt[e]) {
            int parent = r_to[e];
            if (--out_deg[parent] == 0) {
                min_heap_max.push(parent);
            }
        }
    }

    // =========================================================
    // 2. 최솟값을 만드는 카드 배열 구하기
    // =========================================================
    vector<int> min_C(k);
    priority_queue<int, vector<int>, greater<int>> min_heap_min;

    for (int i = 0; i < k; ++i) {
        if (in_deg[i] == 0) {
            min_heap_min.push(i);
        }
    }

    int val_min = k - 1; 
    while (!min_heap_min.empty()) {
        int u = min_heap_min.top();
        min_heap_min.pop();
        min_C[u] = val_min--; 
        
        // CSR 구조를 이용한 초고속 순방향 인접 노드 탐색
        for (int e = head[u]; e != -1; e = nxt[e]) {
            int child = to[e];
            if (--in_deg[child] == 0) {
                min_heap_min.push(child);
            }
        }
    }

    // =========================================================
    // 3. 진법 변환 및 정답 계산 (모듈러 연산)
    // =========================================================
    long long MOD = 1000000007;
    long long max_ans = 0;
    long long min_ans = 0;
    long long power = 1;

    for (int i = 0; i < k; ++i) {
        max_ans = (max_ans + 1LL * max_C[i] * power) % MOD;
        min_ans = (min_ans + 1LL * min_C[i] * power) % MOD;
        power = (power * n) % MOD;
    }

    long long diff = (max_ans - min_ans + MOD) % MOD;
    
    cout << diff << "\n";

    return 0;
}





