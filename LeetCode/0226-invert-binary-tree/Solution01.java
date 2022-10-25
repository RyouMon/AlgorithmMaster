/**
 * 0226. 翻转二叉树 递归前序遍历
 */
class Solution01 {
    public TreeNode invertTree(TreeNode root) {
        this.invert(root);
        return root;
    }

    private void invert(TreeNode node) {
        if (node == null) {
            return;
        }
        TreeNode tmp = node.left;
        node.left = node.right;
        node.right = tmp;

        this.invert(node.left);
        this.invert(node.right);
    }
}
