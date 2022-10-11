/**
 * 94. 二叉树的中序遍历 递归写法
 */
class Solution01 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        this.traversal(root, result);
        return result;
    }

    private void traversal(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        this.traversal(node.left, result);
        result.add(node.val);
        this.traversal(node.right, result);
    }
}
