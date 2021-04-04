class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPurchase = prices[0]
        
        for day in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[day] - minPurchase)
            minPurchase = min(minPurchase, prices[day])
        return maxProfit