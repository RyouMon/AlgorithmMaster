class Solution01:
    """
    字典法
    """

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        record = [0 for _ in range(26)]

        for char in s:
            key = ord(char) - 97
            record[key] += 1

        for char in t:
            key = ord(char) - 97
            record[key] -= 1

            if record[key] == -1:
                return False

        return not any(record)


class Solution02:
    """
    排序法
    """

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
