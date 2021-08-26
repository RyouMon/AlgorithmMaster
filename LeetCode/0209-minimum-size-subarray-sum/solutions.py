from typing import List


class Solution01:
    """暴力解法
    时间复杂度O(n^2)
    空间复杂度O(1)
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)  # 原数组长度
        result = float('inf')  # 子数组长度

        for start in range(length):
            sum_ = 0  # 子数组元素之和
            for end in range(start, length):
                sum_ += nums[end]

                if sum_ >= target:
                    result = min(result, end - start + 1)
                    break

        return 0 if result == float('inf') else result


class Solution02:
    """滑动窗口
    时间复杂度O(n)
    空间复杂度O(1)
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')  # 子数组长度
        start = 0  # 窗口的起始位置
        sum_ = 0  # 窗口内的元素之和

        for end in range(len(nums)):
            sum_ += nums[end]

            # 当窗口内元素总和大于 target, 窗口向前移动
            while sum_ >= target:
                result = min(result, end - start + 1)
                sum_ -= nums[start]
                start += 1

        return 0 if result == float('inf') else result


if __name__ == '__main__':
    assert Solution01().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert Solution01().minSubArrayLen(4, [1, 4, 4]) == 1
    assert Solution02().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert Solution02().minSubArrayLen(4, [1, 4, 4]) == 1
