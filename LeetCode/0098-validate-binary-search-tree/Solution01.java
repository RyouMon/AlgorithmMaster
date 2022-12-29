/**
 * 98. 验证二叉搜索树 递归遍历后比较
 */
class Solution01 {
    public boolean isValidBST(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        traversal(root, result);
        for (int i = 1; i < result.size(); i++) {
            if (result.get(i) <= result.get(i - 1)) {
                return false;
            }
        }
        return true;
    }

    private void traversal(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        traversal(node.left, result);
        result.add(node.val);
        traversal(node.right, result);
    }
}
