# coding: utf-8

if __name__ == "__main__":
    n, k, q = map(int, input().split(" "))
    scores = [0 for _ in range(n)]
    for _ in range(q): scores[int(input())-1] += 1
    for i in range(n):
        d = k-q+scores[i]>0
        print("Yes" if d else "No")