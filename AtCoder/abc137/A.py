# coding: utf-8

if __name__ == "__main__":
    a, b = map(int, input().split(" "))
    ans = [a+b, a-b, a*b]
    print(max(ans))