class Solution01:
    """翻转二叉树 递归前序遍历解法"""

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
            
        # 交换左右孩子
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Solution02:
    """翻转二叉树 迭代前序遍历解法"""

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        from collections import deque
        stack = deque([root])
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return root


class Solution03:
    """翻转二叉树 层序遍历解法"""

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        from collections import deque
        que = deque([root])

        while que:
            for _ in range(len(que)):
                cur = que.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)

        return root
