#include <cstdio>

const int MAX_N = 50;
int L, n;
int x[MAX_N];

int max(int a, int b) {
    return a>b ? a : b;
}

int min(int a, int b) {
    return a<b ? a : b;
}

void solve() {
    int minT = 0;
    for (int i=0; i<n; i++) {
        minT = max(minT, min(x[i], L-x[i]));
    }

    int maxT = 0;
    for (int i=0; i<n; i++) {
        maxT = max(maxT, max(x[i], L-x[i]));
    }

    printf("%d %d\n", minT, maxT);
}

int main() {
    scanf("%d %d", &L, &n);
    for (int i=0; i<n; i++) {
        scanf("%d", &x[i]);
    }
    solve();
}