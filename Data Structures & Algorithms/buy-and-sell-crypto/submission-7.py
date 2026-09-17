class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse=True):
            return 0
        if prices == sorted(prices):
            return max(prices) - min(prices)

        maxSell = 0
        for i in range(1, len(prices)):
            if prices[i] - min(prices[:i]) > maxSell:
                maxSell = prices[i] - min(prices[:i])
        return maxSell

        