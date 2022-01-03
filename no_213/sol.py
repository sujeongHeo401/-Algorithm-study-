class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        max1 = self.rob_simple(nums[1:])
        max2 = self.rob_simple(nums[:-1])        
        return max(max1, max2)
    
    def rob_simple(self, nums: List[int]) -> int:
        t1=0
        t2=0
        for cur in nums:
            temp = t1
            t1 = max(t2+cur, t1)
            t2 = temp
            
        return t1
            