from typing import List


class Solution01:
    """暴力破解法
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """

    @classmethod
    def removeElement(cls, nums: List[int], val: int) -> int:
        length = len(nums)
        index = 0

        while index < length:

            if nums[index] == val:

                for j in range(index + 1, length):
                    nums[j - 1] = nums[j]

                length -= 1
                index -= 1  # 因为数组整体向左移动了一个元素，所以索引也要同时移动

            index += 1

        return length


class Solution02:
    """双指针法
    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    @classmethod
    def removeElement(cls, nums: List[int], val: int) -> int:
        fast = slow = 0

        while fast < len(nums):

            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

            # 当 fast 指针遇到要删除的元素时停止赋值
            # slow 指针停止移动, fast 指针继续前进
            fast += 1

        return slow


if __name__ == '__main__':
    assert Solution01.removeElement([3, 2, 2, 3], 3) == 2
    assert Solution01.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5

    assert Solution02.removeElement([3, 2, 2, 3], 3) == 2
    assert Solution02.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
