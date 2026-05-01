#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 500005;
int tree[4 * MAXN];
int lazy[4 * MAXN];
int A[MAXN], B[MAXN];

// 부모의 변경 사항을 자식 노드로 전파
void push(int node) {
    if (lazy[node] != 0) {
        tree[2 * node] += lazy[node];
        lazy[2 * node] += lazy[node];
        tree[2 * node + 1] += lazy[node];
        lazy[2 * node + 1] += lazy[node];
        lazy[node] = 0;
    }
}

// 트리 초기화: 각 리프 노드 x에 Count(x) - x를 계산하기 위해 -x 설정
void build(int node, int start, int end) {
    if (start == end) {
        tree[node] = -start;
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    tree[node] = max(tree[2 * node], tree[2 * node + 1]);
}

// 구간 업데이트: 증언의 범위 [l, r]에 대해 Count(x)를 갱신
void update(int node, int start, int end, int l, int r, int val) {
    if (l > r || start > end || start > r || end < l) return;
    if (start >= l && end <= r) {
        tree[node] += val;
        lazy[node] += val;
        return;
    }
    push(node);
    int mid = (start + end) / 2;
    update(2 * node, start, mid, l, r, val);
    update(2 * node + 1, mid + 1, end, l, r, val); // 인자 개수 수정 완료
    tree[node] = max(tree[2 * node], tree[2 * node + 1]);
}

// 트리 위에서의 이분 탐색: Count(x) - x >= 0을 만족하는 최대 x 탐색
int walk(int node, int start, int end) {
    if (start == end) return start;
    push(node);
    int mid = (start + end) / 2;
    // 오른쪽 구간에 조건을 만족하는 x가 있다면 오른쪽으로 이동
    if (tree[2 * node + 1] >= 0)
        return walk(2 * node + 1, mid + 1, end);
    else
        return walk(2 * node, start, mid);
}

int main() {
    int N;
    if (scanf("%d", &N) != 1) return 0;
    
    build(1, 0, N);
    for (int i = 1; i <= N; i++) {
        if (scanf("%d %d", &A[i], &B[i]) == 2) {
            update(1, 0, N, A[i], B[i], 1);
        }
    }

    // 초기 상태 결과 출력
    printf("%d", walk(1, 0, N));

    int Q;
    if (scanf("%d", &Q) != 1) return 0;
    for (int i = 0; i < Q; i++) {
        int p, l, r;
        if (scanf("%d %d %d", &p, &l, &r) == 3) {
            // 기존 증언 제거 및 새 증언 반영
            update(1, 0, N, A[p], B[p], -1);
            A[p] = l; B[p] = r;
            update(1, 0, N, A[p], B[p], 1);
            printf(" %d", walk(1, 0, N));
        }
    }
    printf("\n");

    return 0;
}


