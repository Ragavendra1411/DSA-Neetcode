class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # low,high,profit=0,0,0
        # low = prices[0]
        # for i in range(1,len(prices)):
        #     if prices[i]<prices[i-1]:
        #         low=prices[i]
        #     if prices[i]>prices[i+1]:
        #         high=prices[i]
        #         profit+= (high-low)
        # return profit
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=(prices[i]-prices[i-1])
        return profit
        