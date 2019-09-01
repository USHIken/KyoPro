# coding: utf-8
import math

if __name__ == "__main__":
    N = int(input())
    H = list(map(int, input().split(" ")))
    c = 0
    max_c = 0
    for i in range(N-1):
        if H[i+1] <= H[i]: c += 1
        else: c = 0
        if max_c < c: max_c = c
    print(max_c)