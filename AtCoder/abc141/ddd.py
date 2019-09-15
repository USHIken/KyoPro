import random
n = 10**5
m = 10**4
print("{} {}".format(n, m))
a = " ".join([str(random.randrange(10**9)) for _ in range(n)])
print(a)
