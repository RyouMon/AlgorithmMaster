/**
 * 209. 长度最小的子数组 暴力解法（超出时间限制）
 * 时间复杂度O(n^2) 空间复杂度O(1)
 */
class Solution01 {
    public int minSubArrayLen(int target, int[] nums) {
        int result = Integer.MAX_VALUE;
        
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            
            for (int j = i; j < nums.length; j++) {
                int length = j - i + 1;
                if (length > result) {
                    break;
                }

                sum += nums[j];
                if (sum >= target) {
                    result = length;
                    break;
                }
            }
        }
        
        return result == Integer.MAX_VALUE ? 0 : result;
    }
}
