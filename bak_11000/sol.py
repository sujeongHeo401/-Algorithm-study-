n = int(input()) # 입력
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))####### 배열 입력

# 3
# 1 3
# 2 4
# 3 5
print("arr: ", arr)
arr.sort()
print("arr: ", arr)

import heapq
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])
q.sort()

room = []
heapq.heapqpush(room, q[0][1]) # 종료 시간을 넣어줘 

for i in range(1, n):
    if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면 
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop 후 새 시간 push
        heapq.heappush(room, q[i][1])
print(len(room))

