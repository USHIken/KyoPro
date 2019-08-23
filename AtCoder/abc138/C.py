# coding: utf-8

if __name__ == "__main__":
    n = int(input())
    v = sorted(list(map(int, input().split())))
    while len(v)!=1:
        v[0] = (v[0]+v.pop(1))/2
    print(v[0])
