/**
 * 209. 长度最小的子数组 滑动窗口
 * 时间复杂度O(n) 空间复杂度O(1)
 */
class Solution02 {
    public int minSubArrayLen(int target, int[] nums) {
        int result = Integer.MAX_VALUE;
        int start = 0;
        int sum = 0;

        for (int end = 0; end < nums.length; end++) {
            sum += nums[end];
            while (sum >= target) {
                int length = end - start + 1;
                result = length < result ? length : result;
                sum -= nums[start++];
            }
        }
        
        return result == Integer.MAX_VALUE ? 0 : result;
    }
}
