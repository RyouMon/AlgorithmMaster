/**
 * 27. 移除元素
 * 双指针法，时间复杂度O(n)，空间复杂度O(1)
 */
class Solution02 {
    public int removeElement(int[] nums, int val) {
        int fast = 0;
        int slow = 0;

        while (fast < nums.length) {
            // 如果快指针指向的元素属于新数组，则将其拷贝到slow指针处
            if (nums[fast] != val) {
                nums[slow] = nums[fast];
                slow++;  // 慢指针移动到下一个要更新的位置
            }
            // 快指针向前移动，寻找下一个数组成员
            fast++;
        }

        return slow;
    }
}