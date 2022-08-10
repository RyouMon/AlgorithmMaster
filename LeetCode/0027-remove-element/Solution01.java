/**
 * 27. 移除元素
 * 暴力解法，时间复杂度O(n^2)，空间复杂度O(1)
 */
class Solution01 {
    public int removeElement(int[] nums, int val) {
        int length = nums.length;

        for (int i = 0; i < length; i++) {
            if (nums[i] != val) {
                continue;
            }
            for (int j = i + 1; j < length; j++) {
                nums[j - 1] = nums[j];
            }
            length--;
            i--;
        }

        return length;
    }
}