/**
 * 106. 从中序与后序遍历序列构造二叉树
 */
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // 空的树
        if (postorder.length == 0) {
            return null;
        }
        
        // 取出后序遍历最后一个节点作为根节点
        TreeNode root = new TreeNode(postorder[postorder.length - 1]);
        
        // 叶子节点
        if (postorder.length == 1) {
            return root;
        }
        
        // 根据后序数组的最后一个元素的值寻找中序数组的切割点
        int delimiterIndex = 0;
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == postorder[postorder.length - 1]) {
                delimiterIndex = i;
            }
        }
        
        // 切割中序数组
        int[] leftInorder = Arrays.copyOfRange(inorder, 0, delimiterIndex);
        int[] rightInorder = Arrays.copyOfRange(inorder, delimiterIndex + 1, inorder.length);

        // 切割后序数组
        int[] leftPostorder = Arrays.copyOfRange(postorder, 0, leftInorder.length);
        int[] rightPostorder = Arrays.copyOfRange(postorder, leftInorder.length, postorder.length - 1);

        root.left = buildTree(leftInorder, leftPostorder);
        root.right = buildTree(rightInorder, rightPostorder);

        return root;
    }
}
