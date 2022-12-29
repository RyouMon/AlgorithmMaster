/**
 * 98. 验证二叉搜索树 递归中序遍历的同时判断
 */
class Solution02 {
    TreeNode pre;

    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        boolean leftIsValid = isValidBST(root.left);
        
        if (pre != null && root.val <= pre.val) {
            return false;
        }
        pre = root;
        
        boolean rightIsValid = isValidBST(root.right);
        return leftIsValid && rightIsValid;
    }
}
