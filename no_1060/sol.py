# [4, 7, 9, 10]
#
#     1
# 7 - 4 - 1 == 2

# [4, 7, 9, 10]
#        |
#        2
# 9 - 4 - 2 = 3 num_missing between0 and i is: nums[i] - nums[0] = i
class Solution:
    def missingElement(self, num: List[int], k: int) -> int:
        #Return how many numbers are missing until nums[idx]
        # num[x] = num[0] + idx
        missing = lambda x : num[x] - num[0] - x
        n = len(num)
        
        if k > missing(n-1):
            return num[n-1] -missing(n-1) + k
        
        left, right = 0, n - 1
        
        while left != right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            
            else:
                right = pivot
        return num[left - 1] + k - missing(left - 1)
