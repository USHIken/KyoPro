from heapq import heappop,heappush
 
N, M = map(int, input().split())
A = list(map(int, input().split()))
 
H = []
 
for i in A:
    heappush(H, -i)
 
for _ in range(M):
    heappush(H, -((-heappop(H)//2)) )
 
print(-sum(H))

# submission
#   #7546961
#   https://atcoder.jp/contests/abc141/submissions/7546961