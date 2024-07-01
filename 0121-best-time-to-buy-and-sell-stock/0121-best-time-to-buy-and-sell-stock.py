class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l =r
                r+=1
            else:
                diff = prices[r] - prices[l]
                if diff > max_profit:
                    max_profit = diff
                r+=1
        return max_profit

            
            
                


        