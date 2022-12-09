class Solution01:
    """合并二叉树 递归法"""

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1


class Solution02:
    """合并二叉树 迭代法"""

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        que = deque([root1, root2])
        while que:
            t1 = que.popleft()
            t2 = que.popleft()
            t1.val += t2.val
            
            # 如果t1、t2的左孩子都不为空，将它们加入到队列中
            if t1.left and t2.left:
                que.append(t1.left)
                que.append(t2.left)
            
            # 如果t1、t2的右孩子都不为空，将它们加入到队列中
            if t1.right and t2.right:
                que.append(t1.right)
                que.append(t2.right)
            
            # 如果t1的左孩子为空，t2的左孩子不为空，将t2的左孩子赋值给t1
            if not t1.left and t2.left:
                t1.left = t2.left
            
            # 如果t1的右孩子为空，t2的右孩子不为空，将t2的右孩子赋值给t1
            if not t1.right and t2.right:
                t1.right = t2.right
        
        return root1
