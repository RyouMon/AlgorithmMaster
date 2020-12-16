class Solution01(object):
    """滑动窗口"""

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        offset = len(needle) - 1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+offset+1] == needle:
                return i
        return -1


class Solution02(object):
    """KMP算法"""

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        j = 0
        n = self.get_next(needle)
        for i in range(len(haystack)):
            while (j > 0) and (needle[j] != haystack[i]):
                j = n[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

    def get_next(self, needle):
        """
        :type needle: str
        :rtype: list
        """
        i = 0
        j = 1
        n = [0 for _ in range(len(needle))]
        while j < len(needle):
            if needle[i] == needle[j]:
                n[j] = i + 1
                j += 1
                i += 1
            elif i == 0:
                n[j] = 0
                j += 1
            else:
                i = n[i-1]
        return n
