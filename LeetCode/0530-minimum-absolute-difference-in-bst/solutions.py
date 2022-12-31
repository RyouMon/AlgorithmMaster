class Solution01:
    """二叉搜索树的最小绝对差 递归法"""

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_val = float('inf')
        self.pre = None
        self.traversal(root)
        return self.min_val
        
    def traversal(self, cur: TreeNode):
        if not cur:
            return
            
        self.traversal(cur.left)
        
        if self.pre:
            self.min_val = min(self.min_val, cur.val - self.pre.val)
        self.pre = cur

        self.traversal(cur.right)


class Solution02:
    """二叉搜索树的最小绝对差 迭代法"""

    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = deque()
        min_val = float('inf')
        pre = None
        
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    min_val = min(min_val, cur.val - pre.val)
                pre = cur
                cur = cur.right
        return min_val
