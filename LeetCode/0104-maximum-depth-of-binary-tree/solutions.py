class Solution:
    """二叉树的最大深度 层序遍历解法"""

    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return depth

        from collections import deque
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
