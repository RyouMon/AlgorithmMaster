import collections


class Solution01:
    """
    使用内置API
    """

    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


class Solution02:
    """
    自己实现对应的功能
    """

    def trim_space(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去除首尾空格
        while s[left] == ' ':
            left += 1
        while s[right] == ' ':
            right -= 1
        # 去除多余空格
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # 寻找单词的结尾处
            while (end < n) and (l[end] != ' '):
                end += 1
            # 反转单词
            self.reverse(l, start, end - 1)
            # 更新 start 和 end
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # 去除多余空格
        l = self.trim_space(s)
        # 反转整个字符串
        self.reverse(l, 0, len(l) - 1)
        # 反转每个单词
        self.reverse_each_word(l)

        return ''.join(l)


class Solution03:
    """
    使用双端队列
    """

    def reverseWords(self, s: str) -> str:
        # 去除字符串两端的空格
        left, right = 0, len(s) - 1
        while s[left] == ' ':
            left += 1
        while s[right] == ' ':
            right -= 1

        # 将每个单词依次压到队列的头部
        dq, word = collections.deque(), []
        while left <= right:
            if s[left] != ' ':
                word.append(s[left])
            elif s[left] == ' ' and word:
                dq.appendleft(''.join(word))
                word = []
            left += 1
        dq.appendleft(''.join(word))

        return ' '.join(dq)
