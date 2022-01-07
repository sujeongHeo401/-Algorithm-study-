class Solution {
    public int maximizeSweetness(int[] sweetness, int k) {
        int low = 1, high = Arrays.stream(sweetness).sum() / (k + 1);
        System.out.println("high: "+high);
        while (low < high){
            int mid = (low + high + 1) / 2;
            if (canSplit(sweetness, k, mid)) low = mid;
            else high = mid - 1;
        }
        return low;     
    }
                
    private boolean canSplit(int[] sweetness, int k, int mid) {
        int chunks = 0, sum = 0;
        for (int i = 0; i < sweetness.length; i++){
            sum += sweetness[i];
            if (sum >= mid){
                ++chunks;
                sum = 0;
            }
        }
        return chunks >= k + 1;
    }
}
