#include <bits/stdc++.h>

using namespace std;

stack<int> s;

int main(void){
    // 삽(5)= 삽(2) = 삽(3) = 삽(7) = 삭제 - 삽(1) - 삽(4) - 삭제()
    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop();
    s.push(1);
    s.push(4);
    s.pop();
    // 스택의 최상단 원소부터 출력 
    while (!s.empty()){
        cout << s.top() << ' ';
        s.pop();
    }
}