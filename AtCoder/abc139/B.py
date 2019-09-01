# coding: utf-8
import math

if __name__ == "__main__":
    A, B = map(int, input().split(" "))
    print(math.ceil(((B-A)/(A-1))+1))