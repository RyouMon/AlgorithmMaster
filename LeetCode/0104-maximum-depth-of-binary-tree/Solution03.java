/**
 * 104. 二叉树的最大深度 递归前序遍历
 */
class Solution03 {

    private int result = 0;

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return result;
        }
        getDepth(root, 1);
        return result;
    }

    private void getDepth(TreeNode node, int depth) {
        result = depth > result ? depth : result;
        if (node.left == null && node.right == null) {
            return;
        }
        if (node.left != null) {
            getDepth(node.left, depth + 1);
        }
        if (node.right != null) {
            getDepth(node.right, depth + 1);
        }
    }
}
