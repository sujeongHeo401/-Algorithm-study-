#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int IsPrime(unsigned long long n)
{
    unsigned long long c;
    if(n < 2) return 0;
    for (c = 2; c * c <= n; c++)
    {
        if(!(n % c)) return 0;
    }
    return 1;
}
int solution(int n, int k) {
    int answer = 0;
    unsigned long long c,t,r;
    for(r = 1,t = 0; n || t;)
    {
        c = n % k;
        if (!c) {
            answer += IsPrime(t);
            t = 0;
            r= 1;
        } else {
            t += c * r;
            r *= 10;
        }
        n /= k;
    }
    return answer;
}