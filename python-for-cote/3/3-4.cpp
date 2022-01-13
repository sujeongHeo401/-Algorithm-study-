#include <bits/stdc++.h>

using namespace std;

int n, k;
int result;

int main(){
    //N, K 를 공백을 기준으로 구분하여 입력 받기
    cin >> n >> k;
    
    while(true){
        //N이 K로 나누어 떵러지는 수가 될 때까지만 1씩 빼기;
        int target = (n / k)  * k;

        result += (n - target);
        n = target;
        // n 이 k 보다 작을 때 (더 이상 나눌 수 없을 때) 
        if (n < k) break;
        //k 로 나누기 
        result += 1;
        n /= k;        
    }

    // 마지막으로 남은 수에 대해서 1씩 빼기 
    result += (n - 1);
}