from typing import List 
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArray = -math.inf
        for i in range(len(nums)):
            cur_sub_arr = 0
            for j in range(i, len(nums)):
                cur_sub_arr += nums[j]
                maxSubArray = max(maxSubArray, cur_sub_arr)
        return maxSubArray
