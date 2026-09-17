class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxP
# Two pointers always has better time/space complexity
# Time complexity: O(N)
# Space complexity: O(1)