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
    public int maxLevelSum(TreeNode root) {
       int level = 0;
        int totalSum = Integer.MIN_VALUE;
        int resLevel = 0;

        Queue<TreeNode> q = new LinkedList<>();

        if(root != null)
            q.offer(root);

        while(!q.isEmpty()) {

            int size = q.size();
            int sum = 0;
            level++;

            for(int i = 0; i < size; i++) {

                TreeNode node = q.poll(); // remove current node

                sum += node.val;

                if(node.left != null)
                    q.offer(node.left);

                if(node.right != null)
                    q.offer(node.right);
            }

            if(sum > totalSum) {
                totalSum = sum;
                resLevel = level;
            }
        }

        return resLevel;
    }
    
}