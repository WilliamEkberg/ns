class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('inf')
        profit = 0

        for index, value in enumerate(prices):
            val = value-smallest
            
            if val > profit:
                profit = val
            
            if smallest > value:
                smallest = value
        return profit
            



        