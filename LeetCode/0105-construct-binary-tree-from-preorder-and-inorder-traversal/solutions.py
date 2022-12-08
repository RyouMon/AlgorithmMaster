class Solution:
    """从前序与中序遍历序列构造二叉树 递归法"""
    
    def traversal(
        self, preorder: List[int], preorder_begin: int, preorder_end: int,
        inorder: List[int], inorder_begin: int, inorder_end: int,
    ) -> TreeNode:
        # 如果列表长度为0，返回空节点
        if preorder_begin == preorder_end:
            return None
        
        # 前序列表的第一个元素为当前节点的值
        root = TreeNode(preorder[preorder_begin])
        
        # 如果列表长度为1，当前节点为叶子节点，直接返回
        if preorder_end - preorder_begin == 1:
            return root
        
        delimiter = inorder.index(preorder[preorder_begin])
        
        # 得到左右中序列表的起止索引
        left_inorder_begin = inorder_begin
        left_inorder_end = delimiter
        right_inorder_begin = delimiter + 1
        right_inorder_end = inorder_end
        
        left_inorder_size = left_inorder_end - left_inorder_begin
        
        # 得到左右前序列表的起止索引
        left_preorder_begin = preorder_begin + 1
        left_preorder_end = preorder_begin + 1 + left_inorder_size
        right_preorder_begin = preorder_begin + 1 + left_inorder_size
        right_preorder_end = preorder_end
        
        # 递归构建左右子树
        root.left = self.traversal(
            preorder, left_preorder_begin, left_preorder_end,
            inorder, left_inorder_begin, left_inorder_end,
        )
        root.right = self.traversal(
            preorder, right_preorder_begin, right_preorder_end,
            inorder, right_inorder_begin, right_inorder_end,
        )
        
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not len(preorder):
            return None
            
        return self.traversal(preorder, 0, len(preorder), inorder, 0, len(inorder))
