/**
 * 105. 从前序与中序遍历序列构造二叉树
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // 空节点
        if (preorder.length == 0) {
            return null;
        }
        
        // 取出前序数组第一个节点作为根节点
        TreeNode root = new TreeNode(preorder[0]);
        
        // 叶子节点
        if (preorder.length == 1) {
            return root;
        }

        // 根据前序数组第一个节点的值找出切割点
        int delimiterIndex = 0;
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == preorder[0]) {
                delimiterIndex = i;
            }
        }
        
        // 切割中序数组
        int[] leftInorder = Arrays.copyOfRange(inorder, 0, delimiterIndex);
        int[] rightInorder = Arrays.copyOfRange(inorder, delimiterIndex + 1, inorder.length);

        // 切割前序数组
        int[] leftPreorder = Arrays.copyOfRange(preorder, 1, delimiterIndex + 1);
        int[] rightPreorder = Arrays.copyOfRange(preorder, delimiterIndex + 1, preorder.length);

        root.left = buildTree(leftPreorder, leftInorder);
        root.right = buildTree(rightPreorder, rightInorder);

        return root;
    } 
}
