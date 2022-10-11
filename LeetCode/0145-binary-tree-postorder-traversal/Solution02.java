/**
 * 145. 二叉树的后序遍历 迭代写法
 */
class Solution02 {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.empty()) {
            TreeNode cur = stack.pop();
            if (cur == null) {
                continue;
            }
            result.add(cur.val);
            stack.push(cur.left);
            stack.push(cur.right);
        }
        Collections.reverse(result);
        return result;
    }
}
