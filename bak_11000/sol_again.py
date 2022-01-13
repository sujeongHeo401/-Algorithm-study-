import heapq
n = int(input()) # 입력
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))####### 배열 입력
arr.sort()
room = []
heapq.heappush(room, arr[0][1])
for i in range(1, n):
    if room and room[0] <= arr[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, arr[i][1])
print(len(room))
