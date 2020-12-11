from typing import List


class Solution01:
    def arrayPairSum(elf, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(0, len(nums), 2):
            s = s + nums[i]
        return s
