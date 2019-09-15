# coding: utf-8
import math
import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    a = np.array(list(map(int, input().split(" "))))
    for _ in range(m):
        idx = np.argmax(np.ceil(a/2))
        a[idx] = int(a[idx]/2)
    print(a.sum())