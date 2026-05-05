#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

// 역추적을 위한 정보 저장 구조체
struct Result {
    char k;     // 분할 지점
    short x, y; // 왼쪽, 오른쪽 구간의 결과값
};

bool dp[35][35][905];       // dp[시작][끝][값]
Result back[35][35][905];   // 경로 역추적용
vector<int> vals[35][35];   // 각 구간에서 가능한 값 목록 (최적화용)
int a[35];                  // 입력 수열

// 축소 연산 순서를 출력하는 재귀 함수
void printOps(int i, int j, int val, int offset) {
    if (i == j) return;
    Result b = back[i][j][val];
    
    // 1. 오른쪽 구간을 먼저 하나의 값으로 축소 (인덱스 안정성 확보)
    printOps(b.k + 1, j, b.y, offset + (b.k - i + 1));
    
    // 2. 왼쪽 구간을 하나의 값으로 축소
    printOps(i, b.k, b.x, offset);
    
    // 3. 두 구간의 결과값을 합치는 연산 출력
    // offset은 현재 구간이 전체 수열에서 시작되는 위치를 보정함
    printf("%d\n", offset + 1);
}

int main() {
    int N, T;
    // N과 최종값 T 입력
    if (scanf("%d %d", &N, &T) != 2) return 0;
    
    for (int i = 1; i <= N; ++i) {
        scanf("%d", &a[i]);
        dp[i][i][a[i]] = true;
        vals[i][i].push_back(a[i]);
    }

    // DP: 구간 길이를 2부터 N까지 늘려가며 탐색
    for (int len = 2; len <= N; ++len) {
        for (int i = 1; i <= N - len + 1; ++i) {
            int j = i + len - 1;
            for (int k = i; k < j; ++k) {
                // 가능한 x(왼쪽)와 y(오른쪽) 조합 탐색
                for (int x : vals[i][k]) {
                    for (int y : vals[k + 1][j]) {
                        int v = abs(x - y);
                        if (!dp[i][j][v]) {
                            dp[i][j][v] = true;
                            back[i][j][v] = {(char)k, (short)x, (short)y};
                            vals[i][j].push_back(v);
                        }
                    }
                }
            }
        }
    }

    // 최종값을 얻을 수 있는지 확인
    if (T < 0 || T > 900 || !dp[1][N][T]) {
        printf("0\n"); // 불가능한 경우 0 출력
    } else {
        printOps(1, N, T, 0); // 연산 순서 출력
    }

    return 0;
}




