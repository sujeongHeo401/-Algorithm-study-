class Solution{
    
    public int rob(int[] nums){
        int N = nums.length;    
        
        //Special handling for empty array case
        if(N == 0){
            return 0;
        }
        
        int robNext, robNextPlusOne;
        
        robNextPlusOne = 0;
        robNext = nums[N-1];
        
        for (int i = N - 2; i >= 0; i--){
            
            int current = Math.max(robNext, robNextPlusOne + nums[i]);
            
            //Update the variables
            robNextPlusOne = robNext;
            robNext= current;
        }
        return robNext;

    }
  
}