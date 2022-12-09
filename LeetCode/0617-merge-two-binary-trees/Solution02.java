/**
 * 617. 合并二叉树
 * 迭代解法
 */
class Solution02 {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) {
            return null;
        } else if (root1 == null) {
            return root2;
        } else if (root2 == null) {
            return root1;
        }

        Queue<TreeNode> que = new LinkedList<>();
        que.add(root1);
        que.add(root2);
        while (!que.isEmpty()) {
            TreeNode node1 = que.remove();
            TreeNode node2 = que.remove();
            node1.val += node2.val;

            if (node1.right != null && node2.right != null) {
                que.add(node1.right);
                que.add(node2.right);
            }
            if (node1.left != null && node2.left != null) {
                que.add(node1.left);
                que.add(node2.left);
            }

            if (node1.left == null && node2.left != null) {
                node1.left = node2.left;
            }
            if (node1.right == null && node2.right != null) {
                node1.right = node2.right;
            }
        }
        return root1;
    }
}
