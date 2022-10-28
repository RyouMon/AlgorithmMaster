/**
 * 104. 二叉树的最大深度 后序递归遍历
 */
class Solution01 {
    public int maxDepth(TreeNode root) {
        return getDepth(root);
    }
    
    private int getDepth(TreeNode node) {
        if (node == null) {
             return 0;
        }
        int leftDepth = getDepth(node.left);
        int rightDepth = getDepth(node.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
