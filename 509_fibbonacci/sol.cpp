class Solution {
public:
    int fib(int n) {
        int fibNum = 0;
        if(n < 2) return n;
        int fibo[30] = {};
        fibo[0] = 1;
        fibo[1] = 1;
        for(int i=2; i<n; i++){
            fibo[i] = fibo[i-1] + fibo[i-2];
        }
        fibNum = fibo[n-1]; 
        return fibNum;
        
    }
};