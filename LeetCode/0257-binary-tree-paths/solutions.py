from collections import deque


class Solution01:
    """二叉树的所有路径 递归法"""

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path, result = [], []
        self.traversal(root, path, result)
        return result

    def traversal(self, cur: TreeNode, path: List, result: List):
        path.append(str(cur.val))
        # 如果当前节点为叶子节点，添加路径到结果中
        if (not cur.left) and (not cur.right):
            result.append('->'.join(path))
            return

        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()  # 回溯

        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()  # 回溯


class Solution02:
    """二叉树的所有路径 递归法"""

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        path, result = '', []
        self.traversal(root, path, result)
        return result

    def traversal(self, cur: TreeNode, path: List, result: List):
        path += str(cur.val)
        # 如果当前节点为叶子节点，添加路径到结果中
        if not (cur.left or cur.right):
            result.append(path)
            return

        if cur.left:
            # 使用path + "->"调用traversal，调用完后path的值没有改变，由此达到回溯的效果。
            self.traversal(cur.left, path + '->', result)

        if cur.right:
            self.traversal(cur.right, path + '->', result)


class Solution:
    """二叉树的所有路径 迭代法"""

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 题目中节点数至少为1
        stack, path_st, result = deque([root]), deque(), []
        path_st.append(str(root.val))

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            # 如果当前节点为叶子节点，添加路径到结果中
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))

        return result
