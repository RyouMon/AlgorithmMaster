class Solution01:
    """
    双指针法。
    """

    def replaceSpace(self, s: str) -> str:
        l = list(s)
        count = 0

        # 统计空格数并扩容数组
        for char in l:
            if char is ' ':
                count += 1
        l += ['' for _ in range(count * 2)]

        left = len(s) - 1
        right = len(l) - 1

        # 当左右指针重合时结束循环
        while left != right:

            if l[left] != ' ':
                l[right] = l[left]
                right -= 1
                left -= 1
                continue

            for c in '02%':
                l[right] = c
                right -= 1
            left -= 1

        return ''.join(l)


class Solution02:
    """
    直接使用 str 的 replace 方法。
    """

    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')
