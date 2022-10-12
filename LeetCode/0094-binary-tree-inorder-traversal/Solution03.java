/**
 * 94. 二叉树的中序遍历 迭代写法（统一写法）
 */
class Solution03 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.empty()) {
            if (stack.peek() != null) {
                TreeNode cur = stack.pop();
                if (cur.right != null) {
                    stack.push(cur.right);
                }
                stack.push(cur);
                stack.push(null);
                if (cur.left != null) {
                    stack.push(cur.left);
                }
            } else {
                stack.pop();
                TreeNode cur = stack.pop();
                result.add(cur.val);
            }
        }
        return result;
    }
}
