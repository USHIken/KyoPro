# coding: utf-8

if __name__ == "__main__":
    S = input()  
    T = input()
    c = 0  
    for s,t in zip(S,T):
        if s == t: c += 1
    print(c)