#include <cstdio>

const int MAX_N = 50;
int a[MAX_N];
int n, k;

bool dfs(int i, int sum) {
    if (i==n) return sum == k;

    if (dfs(i+1, sum)) return true;

    if (dfs(i+1, sum+a[i])) return true;

    return false;
}

void solve() {
    if (dfs(0, 0)) printf("Yes\n");
    else printf("No\n");
}

int main() {
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%d", &a[i]);
    }
    scanf("%d", &k);
    solve();
}