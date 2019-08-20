# coding: utf-8

if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    ab = {}
    for i in range(n):
        a, b = map(int, input().split(" "))
        try:
            ab[a].append(b)
        except:
            ab[a] =[b]

    ans = 0
    for today in range(m):
        days = m - today
        l = {}
        for i in range(days+1)[::-1]:
            try:
                l[i] = max(ab[i])
            except:
                pass
        max_item = max(l.items(), key=lambda x: x[1])
        ans += max_item[1]
        ab[max_item[0]].remove(max_item[1])
    print(ans)
