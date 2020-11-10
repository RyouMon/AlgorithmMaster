class Solution01:
    """
    字符串切片
    """

    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Solution02:
    """
    列表遍历
    """

    def reverseLeftWords(self, s: str, n: int) -> str:
        result = []
        length = len(s)
        for i in range(n, length):
            result.append(s[i])
        for i in range(n):
            result.append(s[i])
        return ''.join(result)
