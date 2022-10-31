/**
 * 110. 平衡二叉树 递归后序遍历
 */
class Solution01 {
    public boolean isBalanced(TreeNode root) {
        int height = getHeight(root);
        return height != -1;
    }

    public int getHeight(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftHeight = getHeight(node.left);
        int rightHeight = getHeight(node.right);
        if (leftHeight == -1 || rightHeight == -1) {
            return -1;
        }
        if (Math.abs(leftHeight - rightHeight) > 1) {
            return -1;
        }
        return Math.max(leftHeight, rightHeight) + 1;
    }
}
