from typing import List


class Solution:

    @classmethod
    def search(cls, nums: List[int], target: int) -> int:
        # 定义左右指针
        left = 0
        right = len(nums) - 1

        # 开始二分查找
        while left <= right:

            middle = (left + right) // 2

            # target 在区间左边
            if target < nums[middle]:
                right = middle - 1

            # target 在区间右边
            elif target > nums[middle]:
                left = middle + 1

            # target 被找到了
            else:  # nums[middle] = target
                return middle

        return -1


if __name__ == '__main__':
    assert Solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert Solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
