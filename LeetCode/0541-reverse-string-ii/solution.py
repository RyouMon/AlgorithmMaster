class Solution:

    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        for i in range(0, len(s), 2*k):

            # 这里 Python 有点特殊的，就算 i + k 的值超出了列表实际的长度，没有超出的部分也会全部反转。
            s[i:i+k] = reversed(s[i:i+k])

        return ''.join(s)
