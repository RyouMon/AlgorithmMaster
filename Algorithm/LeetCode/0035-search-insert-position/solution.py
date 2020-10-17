from typing import List


class Solution01:
    """暴力解法"""

    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        for i in range(length):
            # 处理以下三种情况：
            #   target 插入到数组头部
            #   target 插入到数组间的某个位置
            #   target 等于某个数组元素
            if (nums[i] >= target):
                return i

        # target 插入到数组尾部
        return length


class Solution02:
    """二分查找法，写法一"""

    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  # 定义 target 在 [left, right] 区间内

        while (left <= right):  # 当 left == right , 区间 [left, right] 仍然有效

            mid = int(left + ((right - left) / 2))  # 防止溢出，等同于 (left + right)/2

            if (nums[mid] > target):
                right = mid - 1  # target 在左区间，[left, mid - 1]
            elif (nums[mid] < target):
                left = mid + 1  # target 在右区间，[mid + 1, right]
            else:  # nums[mid] == target
                return mid

        # 目标值在所有元素之前：return right + 1
        # 目标值等于数组中的某一个元素: return mid
        # 目标值插入数组中的位置: return right + 1
        # 目标值在所有元素之后: return right + 1
        return right + 1


class Solution03:
    """二分查找法，写法二"""

    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)  # 定义 target 在 [left, right) 区间内

        while (left < right):  # 当 left == right , 区间 [left, right) 无效

            mid = int(left + ((right - left) >> 1))  # 防止溢出，等同于 (left + right)/2

            if (nums[mid] > target):
                right = mid  # target 在左区间，[left, mid)
            elif (nums[mid] < target):
                left = mid + 1  # target 在右区间，[mid + 1, right)
            else:  # nums[mid] == target
                return mid

        # 目标值在所有元素之前：return right
        # 目标值等于数组中的某一个元素: return mid
        # 目标值插入数组中的位置: return right
        # 目标值在所有元素之后: return right
        return right
