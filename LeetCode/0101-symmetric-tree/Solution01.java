/**
 * 0101. 对称二叉树 递归法
 */
class Solution01 {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return compare(root.left, root.right);
    }

    private boolean compare(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        } else if (left == null && right != null) {
            return false;
        } else if (right == null && left != null) {
            return false;
        } else if (left.val != right.val) {
            return false;
        }
        boolean isInSideSymmetric = compare(left.right, right.left);
        boolean isOutSideSymmetirc = compare(left.left, right.right);
        return isInSideSymmetric && isOutSideSymmetirc;
    }
}
