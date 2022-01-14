#include <bits/stdc++.h>

using namespace std;

int factorial_iterative(int n){
    int result = 1;

    for (int i = 1; i <= n; i++){
        result *= i;
    }

    return result;
}

int factorial_recursive(int n){
    if (n <= 1) return 1
    // n! = n * (n - 1)! 을 그대로 이용하기 
    return n * factorial_recursive(n-1);
}

int main(void){
    cout << "반복적으로 구현:" << factorial_iterative(5) << '\n';
    cout << "재귀적으로 구현:" << factorial_recursive(5) << '\n';
}