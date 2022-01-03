class Solution {
    public int maxSubArray(int[] nums) {
        int maxSubArray = Integer.MIN_VALUE;
        for(int i = 0; i < nums.length; i++){
            int currentSubarray = 0;
            for(int j = i; j < nums.length; j++){
                currentSubarray += nums[j];
                maxSubArray = Math.max(maxSubArray, currentSubarray);
            }
        }
        
        return maxSubArray;
        
    }
}