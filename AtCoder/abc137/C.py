# coding: utf-8

def fact(n, m):
    ans = 1
    for i in range(n-m+1, n+1):
        ans *= i
    return ans

if __name__ == "__main__":
    N = int(input())
    s = []
    c = {}
    for i in range(N):
        a = "".join(sorted(input()))
        s.append(a)
        try:
            c[a] += 1
        except KeyError:
            c[a] = 1
    
    ans = 0
    for k,v in c.items():
        ans += fact(v,2)/2
    
    print(int(ans))