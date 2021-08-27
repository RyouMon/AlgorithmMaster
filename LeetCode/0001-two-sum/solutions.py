from typing import List


class Solution01:
    """暴力枚举
    时间复杂度O(n^2)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution02:
    """哈希法"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in hashmap:
                return [i, hashmap[val]]
            hashmap[num] = i
