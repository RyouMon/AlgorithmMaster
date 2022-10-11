/**
 * 144. 二叉树的前序遍历
 * 递归法
 */
class Solution01 {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        this.traversal(root, result);
        return result;
    }

    private void traversal(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        result.add(node.val);
        this.traversal(node.left, result);
        this.traversal(node.right, result);
    }
}
