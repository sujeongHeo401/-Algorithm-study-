from collections import deque
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

#BFS 소스코드 구현 
def bfs(x, y):
    # 큐 (Q) 구혀능ㄹ 위해 dequq 라이브러리 사용 
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny <= m:
                continue
            # 벽인 경우 무시 
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리를 기록 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

        # 가장 오른쪽 아래까지의 최단 거리 반환 
    return graph[n - 1][m - 1]
    
print(bfs(0, 0))
            # 미로 찾기 공가