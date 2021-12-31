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
    public int maxAncestorDiff(TreeNode root) {
        return minMax(root, Integer.MAX_VALUE, Integer.MIN_VALUE, 0);
    }
    
    public int minMax(TreeNode node, int mini, int maxi, int curRes) {
        if (null == node) return curRes;
        int mini2 = Math.min(mini, node.val);
        int maxi2 = Math.max(maxi, node.val);
        int res = Math.max(curRes, Math.abs(mini2 - maxi2));
        int leftRes = minMax(node.left, mini2, maxi2, res);
        int rightRes = minMax(node.right, mini2, maxi2, res);
        // System.out.println(String.format("node: %d, mini: %d, maxi: %d, mini2: %d, maxi2: %d, res: %d, leftRes: %d, rightRes: %d", node.val, mini, maxi, mini2, maxi2, res, leftRes, rightRes));
        return Math.max(leftRes, rightRes);
    }
}