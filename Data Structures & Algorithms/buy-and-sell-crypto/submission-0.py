class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]

        maxPrice = 0

        for price in range(1,len(prices)):

            minPrice = min(prices[price],minPrice)

            maxPrice = max(maxPrice,prices[price] - minPrice)
            

        return maxPrice
