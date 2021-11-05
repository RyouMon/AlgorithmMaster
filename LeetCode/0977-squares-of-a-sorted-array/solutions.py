from typing import List


class Solution01:
    """暴力破解法"""

    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = map(lambda x: x * x, nums)
        return sorted(nums)


class Solution02:
    """双指针法"""

    def sortedSquares(self, nums: List[int]) -> List[int]:
        results = [0]

        left, right = 0, len(nums) - 1

        while left < right:
            sq1 = nums[left] * nums[left]
            sq2 = nums[right] * nums[right]

            if sq2 >= sq1:
                results.appendleft(sq2)
                results.appendleft(sq1)
            else:
                results.appendleft(sq1)
                results.appendleft(sq2)

            left += 1
            right -= 1

        if left == right:
            results.appendleft(nums[left] * nums[left])

        return results


if __name__ == '__main__':
    assert Solution01().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution01().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

    assert Solution02().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution02().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
