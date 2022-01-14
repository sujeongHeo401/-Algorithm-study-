#include <bits/stdc++.h>

using namespace std;

int n, m;
int graph[100][100];

bool dfs(int x, int y){
    // 주어진 범위를 벗어나는 경우에는 즉시 종료
    if (x < 0 || x >= n || y < 0 || y >=m){
        return false;
    }

    if(graph[x][y] == 0){
        // 해당 노드 방문 처리 
        graph[x][y] = 1;
        dfs(x-1, y);
        dfs(x, y-1);
        dfs(x+1, y);
        dfs(x, y+1);
        return true;
    }
    return false;
}

int main(){
    // N, M을 공백 기준으로 구분하여 입력 받기
    cin >> n >> m;
    // 2차원 리스트의 맵 정보 입력 받기
    for(int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            scanf("%1d", &graph[i][j]);
        }
    }
    // 모든 노드에 대해서 음료수 채우기

    int result = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            // 현재 위치에서 DFS 수행 
            if (dfs(i, j)){
                result += 1;
            }
        }
    }

    cout << result << '\n';
}