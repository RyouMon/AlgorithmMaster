from collections import deque


class Solution01:
    """对称二叉树 递归解法"""

    def compare(self, left: TreeNode, right: TreeNode) -> bool:
        if not (left or right):
            return True
        if (not left) or (not right) or (left.val != right.val):
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        return inside and outside

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    

class Solution02:
    """对称二叉树 队列遍历"""

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        que = deque([root.left, root.right])
        while que:
            left = que.popleft()
            right = que.popleft()

            if not (left or right):
                continue

            if (not left) or (not right) or (left.val != right.val):
                return False

            que.extend([left.left, right.right, left.right, right.left])

        return True


class Solution03:
    """对称二叉树 栈遍历"""

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        que = deque([root.left, root.right])
        while que:
            right = que.pop()
            left = que.pop()

            if not (left or right):
                continue

            if (not left) or (not right) or (left.val != right.val):
                return False

            que.extend([left.left, right.right, left.right, right.left])

        return True
