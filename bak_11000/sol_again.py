import heapq
n = int(input()) # 입력
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))####### 배열 입력
room = []
heapq.heappush(room, arr[0][1])

for i in range(1, len(arr)):
    if room[0] > arr[i][0]: # 빨리 시작하면 
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop()
        heapq.heappush(room, arr[i][1])
print("len(room) : ", len(room))
