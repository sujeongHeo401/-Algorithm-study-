from typing import List 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSubarray = nums[0] 
        maxSubarray = nums[0]

        for num in nums[1:]:
            currentSubarray = max(num, currentSubarray + num)
            maxSubarray = max(maxSubarray, currentSubarray)

        return maxSubarray