class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit