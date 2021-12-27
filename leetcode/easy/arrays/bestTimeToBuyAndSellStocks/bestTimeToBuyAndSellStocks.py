class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        current_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > current_price:
                profit += prices[i] - current_price
            current_price = prices[i]
        return profit