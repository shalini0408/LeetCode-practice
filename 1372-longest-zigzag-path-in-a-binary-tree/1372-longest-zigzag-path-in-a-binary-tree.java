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
    private int maxLen = 0;

    public int longestZigZag(TreeNode root) {
        if (root == null) {
            return 0;
        }
        rightHelper(root, 0);
        leftHelper(root, 0);
        return maxLen;
    }

    public void leftHelper(TreeNode root, int sum) {
        if (root == null) {
            return;
        }
        maxLen = Math.max(maxLen, sum);
        if (root.left != null) {
            rightHelper(root.left, sum + 1);
        }
        if (root.right != null) {
            leftHelper(root.right, 1);
        }
    }

    public void rightHelper(TreeNode root, int sum) {
        if (root == null) {
            return;
        }
        maxLen = Math.max(maxLen, sum);
        if (root.right != null) {
            leftHelper(root.right, sum + 1);
        }
        if (root.left != null) {
            rightHelper(root.left, 1);
        }
    }
}