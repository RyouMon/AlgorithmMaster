from functools import reduce


class Solution:
    """0583. 两个字符串的删除操作 动态规划
    时间复杂度O(mn) 空间复杂度O(mn)
    """
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        
        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = reduce(min, (
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1,
                        dp[i-1][j-1] + 2,
                    ))
        return dp[m-1][n-1]


if __name__ == '__main__':
    assert Solution().minDistance('a', 'b') == 2
