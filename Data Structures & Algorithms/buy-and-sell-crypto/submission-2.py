class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for buy in range(len(prices)):
            for sell in range(buy+1, len(prices)):
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
        return maxP 

        