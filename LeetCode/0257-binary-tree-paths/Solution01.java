/**
 * 257. 二叉树的所有路径 递归
 */
class Solution01 {
    
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        traversal(root, Integer.toString(root.val), result);
        return result;
    }
    
    public void traversal(TreeNode node, String path, List<String> result) {
        if (node.left == null && node.right == null) {
            result.add(path);
            return;
        }
        if (node.left != null) {
            traversal(node.left, path + "->" + Integer.toString(node.left.val), result);
        }
        if (node.right != null) {
            traversal(node.right, path + "->" + Integer.toString(node.right.val), result);
        }
    }
}
