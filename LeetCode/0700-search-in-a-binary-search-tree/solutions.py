class Solution01:
    """二叉树搜索树中的搜索 递归法"""

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
            
        if root.val > val:
            return self.searchBST(root.left, val)
            
        if root.val < val:
            return self.searchBST(root.right, val)


class Solution02:
    """二叉树搜索树中的搜索 迭代法"""

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
            else:
                return root
