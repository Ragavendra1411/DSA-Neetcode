class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, profit = prices[0],0

        for price in range(1,len(prices)):
            if prices[price]<minimum:
                minimum = prices[price]
            else:
                profit = max(profit, prices[price]-minimum)
        return profit
        