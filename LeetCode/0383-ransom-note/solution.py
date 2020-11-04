class Solution:
    """
    哈希法
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashtable = [0 for _ in range(26)]

        for char in magazine:
            hashtable[ord(char)-97] += 1

        for char in ransomNote:
            index = ord(char) - 97
            hashtable[index] -= 1
            if hashtable[index] < 0:
                return False

        return True
