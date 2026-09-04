class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        profit=0
        maxProfit=0
        R=L+1
        while (L<len(prices)-1):
            if(prices[L]<=prices[R]):
                profit=prices[R]-prices[L]
                maxProfit=max(maxProfit,profit)
                R+=1
            else:
                R+=1
            if (R==len(prices)):
                L+=1
                R=L+1
        return maxProfit
            



            
        