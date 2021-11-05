class Solution1:
    """买卖股票的最佳时机IV 动态规划
    时间复杂度O(kn) 空间复杂度O(kn)
    """

    def maxProfit(self, k: int, prices: list[int]) -> int:
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        for j in range(1, 2 * k, 2):
            dp[0][j] = -prices[0]
            
        for i in range(1, len(dp)):
            for j in range(0, 2 * k, 2):
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
                dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    result = Solution1().maxProfit(2, [2, 4, 1])
    assert result == 2
