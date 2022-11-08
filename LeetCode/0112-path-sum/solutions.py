class Solution01:
    """路径总和 递归解法"""

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right) and (targetSum - root.val == 0):
            return True
        if self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val):
            return True
        return False


class Solution02:
    """路径总和 迭代解法"""

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = deque([(root, targetSum - root.val)])
        while stack:
            cur, targetSum = stack.pop()
            if not (cur.left or cur.right) and (targetSum == 0):
                return True
            if cur.right:
                stack.append((cur.right, targetSum - cur.right.val))
            if cur.left:
                stack.append((cur.left, targetSum - cur.left.val))

        return False
