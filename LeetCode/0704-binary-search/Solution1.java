/**
 * 0704. 二分查找
 * 写法一：定义 target 在左闭右闭区间
 */
class Solution01 {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid;

        while (left <= right) {
            mid = (left + right + 1) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int result1 = new Solution01().search(new int[] { -1, 0, 3, 5, 9, 12 }, 9);
        assert result1 == 4;

        int result2 = new Solution01().search(new int[] { -1, 0, 3, 5, 9, 12 }, 2);
        assert result2 == -1;
    }
}
