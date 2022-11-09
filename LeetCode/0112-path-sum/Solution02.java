/**
 * 112. 路径总和 迭代解法
 */
class Solution02 {

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }

        Stack<TreeNode> stack1 = new Stack<>();
        Stack<Integer> stack2 = new Stack<>();
        stack1.add(root);
        stack2.add(targetSum - root.val);
        while (!stack1.isEmpty()) {
            TreeNode node = stack1.pop();
            int val = stack2.pop();
            if (node.right != null) {
                stack1.add(node.right);
                stack2.add(val - node.right.val);
            }
            if (node.left != null) {
                stack1.add(node.left);
                stack2.add(val - node.left.val);
            }
            if (node.left == null && node.right == null && val == 0) {
                return true;
            }
        }
        return false;
    }
}
