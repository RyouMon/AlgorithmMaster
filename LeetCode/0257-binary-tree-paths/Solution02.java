/**
 * 257. 二叉树的所有路径 迭代
 */
class Solution02 {
    
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        Stack<String> paths = new Stack<>();
        Stack<TreeNode> stack = new Stack<>();
        paths.add(Integer.toString(root.val));
        stack.add(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            String path = paths.pop();

            if (node.right != null) {
                stack.add(node.right);
                paths.add(path + "->" + Integer.toString(node.right.val));
            }
            if (node.left != null) {
                stack.add(node.left);
                paths.add(path + "->" + Integer.toString(node.left.val));
            }

            if (node.left == null && node.right == null) {
                result.add(path);
            }
        }
        return result;
    }
}
