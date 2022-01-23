n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(map(int, input().split()))


# DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문 
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 확인 
    if x < 0 or x > n or y > m or y < 0:
        return False
    # 현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리 
        graph[x][y] = 1 
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출 
        dfs(x - 1, y) # 상 
        dfs(x + 1, y) # 하 
        dfs(x, y - 1) # 좌 
        dfs(x, y + 1) # 우
        return True 
    return False   

# 모든 노드(위치)에 대하여 음료수 채우기 
result = 0 
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행 
        if dfs(i, j) == True:
            result += 1 
print(result)