public class Solution {}

// 线性扫描
class Solution01 {
	public boolean isOneBitCharacter(int[] bits) {
		int i = 0;
		while (i < bits.length - 1) {
			i += bits[i] + 1;
		}
		return i == bits.length - 1;
	}
}