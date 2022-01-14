import sys
n ,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))####### 배열 입력

print("graph", graph)
### 풀이 가이드
# 1. 특정 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0' 이면서 아직
# 1-1방문하지 않은 지점이 있다면 해당 지점을 방문한다

# 2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 다시 진행하면 연결된 모든 지점을 방문하지 않은 지점의 수를 센다


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
            # wrong
    if graph[x][y] == 0: # 방문 안했으면 
        graph[x][y] = 1  # 방문처리 
        dfs(x-1, y) # 하
        dfs(x+1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True 
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
