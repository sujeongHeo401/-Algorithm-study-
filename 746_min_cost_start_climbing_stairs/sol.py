from typing import List 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def minimum_cost(i):
            if i <= 1:
                return 0
            # if i in memo:
            #     return memo[i]

            down_one = cost[i-1] + minimum_cost(i-1)
            down_two = cost[i-2] + minimum_cost(i-2)
            return min(down_one, down_two)
        # memo = {}
        return minimum_cost(len(cost))

p = Solution()
print(p.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))