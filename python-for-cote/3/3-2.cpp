#include <bits/stdc++.h>

using namespace std;


int n, m, k;

vector<int> v;

int main() {
	// N, M, K 를 공백을 기준으로 구분하여 입력 받기
	cin >> n >> m >> k;

	// N 개의 수를 공백을 기준으로 구분하여 입력 받기
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		v.push_back(x);
	}

	sort(v.begin(), v.end()); //입력 받은 수들 정렬하기
	int first = v[n - 1]; // 가장 큰 수 
	int second = v[n - 2]; //두 번째로 큰 수 

	// 가장 큰 수가 더해지는 연산 
	int cnt = k * (int(m / (k + 1)));
	cnt += m % (k + 1);

	int result = 0;
	result += cnt * first;
	result += second * (m - cnt);

	cout << result << '/n'; // 최종 답안 출력

}