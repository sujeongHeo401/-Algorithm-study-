#include <stdio.h>
#include <vector.h>
#include <algorithm>
#include <queue>

using namespace std;

vector<pair<int, int>> v;

bool startTime(const pair<int, int> &a, const pair<int, int> &b){
    if (a.first == b.first){
        return a.second < b.second;
    }
    return a.first < b.first;
}

struct compare {
    bool operator()(const pair<int, int> &a, const pair<int, int> &b){
        if (a.second == b.second){
            // 끝나는 시간이 같으면 시작 시간인 빠른 순
            return a.first > b.first;
        }

        return a.second > b.second;
    }
};

priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;

int find_room_count(int n){
    int cnt = 1;
    sort(v.begin(), v.end(), startTime);
    // 정렬된 첫번째 원소 삽입 (시작 시간 빠른 순)
    pq.push(v.at(0));

    for(int i = 1; i < n; i++){
        if(pq.top().second > v.at(i).first){
            pq.push(v.at(i));
            cnt++;
        } else {
            pq.pop();
            pq.push(v.at(i));
        }
    }

    return cnt;
}
int main(){
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        int start, end;
        scanf("%d %d", &start, &end);
        v.push_back(make_pair(start,end));
    }

    int count = find_room_count(n);
    print("%d", count);

    return 0;
}