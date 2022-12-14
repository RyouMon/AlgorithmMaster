class Solution01:
    """验证二叉搜索树 递归法，判断中序遍历是否为递增序列"""

    def isValidBST(self, root: TreeNode) -> bool:
        self.seq = []
        self.traversal(root)
        for i in range(1, len(self.seq)):
            if self.seq[i] <= self.seq[i-1]:
                return False
        return True

    def traversal(self, root: TreeNode) -> None:
        if not root:
            return

        self.traversal(root.left)
        self.seq.append(root.val)
        self.traversal(root.right)


class Solution02:
    """验证二叉搜索树 递归法，遍历的同时判断"""

    def __init__(self):
        self.max_val = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        left = self.isValidBST(root.left)

        if self.max_val >= root.val:
            return False
        self.max_val = root.val

        right = self.isValidBST(root.right)

        return left and right


class Solution03:
    """验证二叉搜索树 迭代法"""

    def isValidBST(self, root: TreeNode) -> bool:
        stack = deque()
        max_val = float('-inf')

        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if max_val >= cur.val:
                    return False
                max_val = cur.val
                cur = cur.right

        return True
