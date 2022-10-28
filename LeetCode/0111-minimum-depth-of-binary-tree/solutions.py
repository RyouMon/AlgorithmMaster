class Solution:
    """二叉树的最小深度 层序遍历解法"""

    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return depth

        from collections import deque
        que = deque([root])

        while que:
            depth += 1
            for _ in range(len(que)):
                cur = que.popleft()
                if not (cur.left or cur.right):
                    return depth
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)

        return depth
