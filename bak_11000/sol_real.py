import heapq
import sys
N = int(input())
C = []
h = []

for i in range(N):
    C.append(list(map(int, sys.stdin.readline().split())))

C.sorted(C, key = lambda x : x[0])
for i in range(N):
    if len(h) != 0 and h[0] <= C[i][0]:
        heapq.heappop(h)
    heapq.heappush(h, C[i][1])

print(len(h))
