class Solution:
    def fib(self, n:int) -> int:
        fibNum = 0
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n >= 3:
            fibo = [0] * n
            fibo[0] = 1
            fibo[1] = 1
            for i in range(2, n):
                fibo[i] = fibo[i-1] + fibo[i-2]
            fibNum = fibo[n-1]
        return fibNum

p = Solution()
print(p.fib(6))

# link https://leetcode.com/problems/fibonacci-number/