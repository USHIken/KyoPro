# coding: utf-8

if __name__ == "__main__":
    s = input()
    ud = set(['U', 'D'])
    o = list(set(s[0::2]) - ud)
    e = list(set(s[1::2]) - ud)
    if 'L' in o or 'R' in e: print("No")
    else: print("Yes")