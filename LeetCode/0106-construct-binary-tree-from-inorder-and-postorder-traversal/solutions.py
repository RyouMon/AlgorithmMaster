nclass Solution01:
    """从中序与后序遍历序列构造二叉树，好理解但性能差"""

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
         # 如果列表长度为0，为空节点
         if not len(inorder):
             return None
         
         # 后序列表中最后一个元素的值为当前节点的值
         root = TreeNode(postorder[-1])
         if len(inorder) == 1:
             return root
         
         # 切割中序列表
         delimiter = inorder.index(postorder[-1])
         left_inorder = inorder[:delimiter]
         right_inorder = inorder[delimiter + 1:]
         
         # 切割后序列表
         left_postorder = postorder[:len(left_inorder)]
         right_postorder = postorder[len(left_inorder):-1]
         
         # 递归创建左右子树
         root.left = self.buildTree(left_inorder, left_postorder)
         root.right = self.buildTree(right_inorder, right_postorder)

         return root


class Solution:
    """从中序与后序遍历序列构造二叉树，性能优化过的代码"""
    
    def traversal(
        self, inorder: List[int], inorder_begin: int, inorder_end: int,
        postorder: List[int], postorder_begin: int, postorder_end: int,
    ) -> TreeNode:
         # 如果列表长度为0，为空节点
         if inorder_begin == inorder_end:
             return None
         
         # 后序列表中最后一个元素的值为当前节点的值
         root = TreeNode(postorder[postorder_end-1])
         if inorder_end - inorder_begin == 1:
             return root
         
         # 中序列表的分割索引
         delimiter = inorder.index(postorder[postorder_end-1])
         
         # 得到左右中序列表的起止索引
         left_inorder_begin = inorder_begin
         left_inorder_end = delimiter
         right_inorder_begin = delimiter + 1
         right_inorder_end = inorder_end
         
         # 得到左右后序列表的起止索引
         left_postorder_begin = postorder_begin
         left_postorder_end = postorder_begin + (left_inorder_end - left_inorder_begin)
         right_postorder_begin = postorder_begin + (left_inorder_end - left_inorder_begin)
         right_postorder_end = postorder_end - 1

         # 递归创建左右子树
         root.left = self.traversal(
             inorder, left_inorder_begin, left_inorder_end, 
             postorder, left_postorder_begin, left_postorder_end
         )
         root.right = self.traversal(
             inorder, right_inorder_begin, right_inorder_end,
             postorder, right_postorder_begin, right_postorder_end
         )

         return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not len(inorder):
            return None

        return self.traversal(inorder, 0, len(inorder), postorder, 0, len(postorder))
