class Solution:
    """路径总和Ⅱ 递归法"""

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.result = []
        self.traversal(root, targetSum - root.val, [root.val])
        return self.result
        
    def traversal(self, cur: TreeNode, targetSum: int, path: List) -> None:
        if not (cur.left or cur.right) and (targetSum == 0):
            self.result.append(path)
            return

        if cur.left:
            self.traversal(cur.left, targetSum - cur.left.val, path + [cur.left.val])

        if cur.right:
            self.traversal(cur.right, targetSum - cur.right.val, path + [cur.right.val])
