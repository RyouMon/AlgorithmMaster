import java.util.Arrays;

public class Solution {
	public static void main(String[] args) {
		int[] arr = {1, 4, 3, 2};
		Solution01 s1 = new Solution01();
		System.out.println(s1.arrayPairSum(arr));  // 4
	}
}

class Solution01 {
	public int arrayPairSum(int[] nums) {
		Arrays.sort(nums);
		int sum = 0;
		for (int i = 0; i < nums.length; i += 2) {
			sum += nums[i];
		}
		return sum;
	}
}