from typing import List


class Solution01:
    """暴力破解法"""
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        index = 0

        while (index < length):

            if nums[index] == val:

                for j in range(index+1, length):

                    nums[j-1] = nums[j]

                length -= 1
                index -= 1  # 因为数组整体向左移动了一个元素，所以索引也要同时移动

            index += 1

        return length


class Solution02:
    """双指针法"""
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):

            if nums[fast] != val:

                nums[slow] = nums[fast]
                slow += 1

        return slow
