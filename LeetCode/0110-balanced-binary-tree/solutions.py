from collections import deque


class Solution01:
    """平衡二叉树 递归解法"""

    def isBalanced(self, root: TreeNode) -> bool:
        depth = self.get_depth(root)
        return False if depth == -1 else True

    def get_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 左子树不是平衡二叉树，说明整棵树不是平衡二叉树
        left_depth = self.get_depth(root.left)
        if left_depth == -1:
            return -1

        # 右子树不是平衡二叉树，说明整棵树不是平衡二叉树
        right_depth = self.get_depth(root.right)
        if right_depth == -1:
            return -1

        # 左右子树的高度差超过1，说明不是平衡二叉树
        if abs(left_depth - right_depth) > 1:
            return -1

        return 1 + max(left_depth, right_depth) 


class Solution02:
    """平衡二叉树 迭代解法"""

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        que = deque([root])
        while que:
            cur = que.pop()
            # 左右子树的高度差超过1，说明不是平衡二叉树
            if abs(self.get_depth(cur.left) - self.get_depth(cur.right)) > 1:
                return False
            if cur.right:
                que.append(cur.right)
            if cur.left:
                que.append(cur.left)

        return True

    def get_depth(self, root: TreeNode) -> bool:
        """层序遍历求树的深度"""
        if not root:
            return 0

        depth = 0
        que = deque([root])
        while que:
            depth += 1
            for _ in range(len(que)):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return depth
