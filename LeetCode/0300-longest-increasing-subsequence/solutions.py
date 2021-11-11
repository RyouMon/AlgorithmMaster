from typing import List


class Solution:
    """最长递增子序列 动态规划
    时间复杂度O(n!) 空间复杂度O(n)
    """
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.lengthOfLIS([0, 1, 0, 3, 2, 3])
    assert result == 4

    result = solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])
    assert result == 6
