import sys
n ,m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0: # 방문 안했으면 
        graph[x][y] = 1 # 방문 처리 
        dfs(x-1, y) # 하
        dfs(x+1, y) # 상 
        dfs(x, y-1) # 좌
        dfs(x, x+1) # 우
        return True
    return False 

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)