/**
 * 112. 路径总和 递归解法
 */
class Solution01 {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }
        return traversal(root, targetSum - root.val);
    }

    public boolean traversal(TreeNode root, int counter) {
        if (root.left == null && root.right == null) {
            if (counter == 0){
                return true;
            }
            return false;
        }
        if (root.left != null && traversal(root.left, counter - root.left.val)) {
            return true;
        }
        if (root.right != null && traversal(root.right, counter - root.right.val)) {
            return true;
        }
        return false;
    }    
}
