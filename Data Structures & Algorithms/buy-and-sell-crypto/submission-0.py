class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0

        maxprofit= 0 

        if len(prices)==0 or len(prices)==1:
            return 0

        for right in range(len(prices)):
            profit = prices[right] - prices[l]
            if profit>maxprofit:
                maxprofit = profit
            
            if prices[right]<prices[l]:
                l = right 
        return maxprofit