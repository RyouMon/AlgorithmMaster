/**
 * 111. 二叉树的最小深度 后序递归遍历
 */
class Solution01 {
    public int minDepth(TreeNode root) {
        return getDepth(root);
    }

    private int getDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftDepth = getDepth(node.left);
        int rightDepth = getDepth(node.right);
        if (node.left == null && node.right != null) {
            return rightDepth + 1;
        }
        if (node.right == null && node.left != null) {
            return leftDepth + 1;
        }
        return Math.min(leftDepth, rightDepth) + 1;
    }
}
