/**
 * 0113. 路径总和Ⅱ
 */
class Solution {

    private List<List<Integer>> result = new ArrayList<>();
    
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return result;
        }

        Stack<Integer> path = new Stack<>();
        path.push(root.val);
        traversal(root, targetSum - root.val, path);
        return result;
    }

    public void traversal(TreeNode node, int targetSum, Stack<Integer> path) {
        if (node.left == null && node.right == null) {
            if (targetSum == 0) {
                result.add(new ArrayList(path));
            }
            return;
        }
        if (node.left != null) {
            path.push(node.left.val);
            traversal(node.left, targetSum - node.left.val, path);
            path.pop();
        }
        if (node.right != null) {
            path.push(node.right.val);
            traversal(node.right, targetSum - node.right.val, path);
            path.pop();
        }
    }
}
