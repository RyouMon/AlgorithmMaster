
/**
 * 0102. 二叉树的层序遍历 递归法
 */
class Solution02 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        this.recursion(root, result, 0);
        return result;
    }

    private void recursion(TreeNode node, List<List<Integer>> result, int depth) {
        if (node == null) {
            return;
        }
        if (depth == result.size()) {
            result.add(new ArrayList());
        }
        
        result.get(depth).add(node.val);
        
        this.recursion(node.left, result, depth + 1);
        this.recursion(node.right, result, depth + 1);
    }
}
