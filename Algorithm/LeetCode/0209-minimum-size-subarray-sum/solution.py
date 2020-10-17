from typing import List


class Solution01:
    """暴力解法"""
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = len(nums)
        result = length + 1  # 最终结果

        for i in range(length):

            sum_ = 0

            for j in range(i, length):

                sum_ += nums[j]

                if sum_ >= s:
                    sub_len = j - i + 1  # 子序列长度
                    result = result if result < sub_len else sub_len
                    break

        # 如果 result 不小于原数组长度说明不存在最小子数组，返回0
        return result if result <= length else 0


class Solution02:
    """滑动窗口"""
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = len(nums)
        result = length + 1
        sum_ = 0
        start = 0  # 窗口的起始位置

        for end in range(length):

            sum_ += nums[end]

            # 动态调节窗口的起始位置
            while (sum_ >= s):

                sub_len = end - start + 1
                result = result if result <= sub_len else sub_len
                sum_ -= nums[start]
                start += 1

        return result if result <= length else 0
