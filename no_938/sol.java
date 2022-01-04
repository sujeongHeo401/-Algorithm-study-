/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int sum;
    public int rangeSumBST(TreeNode root, int low, int high) {
        sum = 0;
        dfs(root, low, high);
        return sum;
        
    }
    
    private void dfs(TreeNode root, int low, int high){
        if(root==null){return;}
        if(low <= root.val && root.val <= high){
            sum += root.val;
        }
        
        //Approach1
        // dfs(root.left, low, high);
        // dfs(root.right, low, high);
        
       //Approach2
        if (low < root.val){
            dfs(root.left, low, high);
        }
        if (high > root.val){
            dfs(root.right, low,high);
        }

        //Time :ON
        // SPACE : ON
    }
}