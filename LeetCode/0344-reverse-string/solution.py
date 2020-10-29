from typing import List


class Solution:
    """
    双指针解法
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for left, right in zip(range(0, len(s)//2), range(-1, -len(s)//2-1, -1)):
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
