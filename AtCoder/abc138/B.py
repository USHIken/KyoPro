# coding: utf-8

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1.0/a[i]
    print(1/ans)
