from collections import deque

#bfs 정의
def bfs(graph, start, visited):
    print("오빠야")
    # 큐 : 구현을 위해 deque 라이브러리 사용
    print("start: ", start)
    queue = deque([start])
    print("queue: " , queue)
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]  = True
# 각 노드가 연결된 정보를 리스트 자료형으로 표현 
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5], 
    [3, 5], 
    [3, 4],
    [7], 
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# 정의된 DFS 함수 호출 
bfs(graph, 1, visited)
