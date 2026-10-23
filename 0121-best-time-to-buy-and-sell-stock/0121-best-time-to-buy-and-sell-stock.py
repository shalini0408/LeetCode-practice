class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) ==1 or len(prices) ==0:
            return 0
        maxStock=0
        buyStock = 0
        sellStock = 1
        while buyStock < sellStock and sellStock < len(prices):
            if prices[sellStock]-prices[buyStock] < 0:
                res = prices[sellStock]-prices[buyStock]
                maxStock = max(maxStock,res)
                buyStock = sellStock
                sellStock = sellStock +1
            else:
                res = prices[sellStock]-prices[buyStock]
                maxStock = max(maxStock, res)
                sellStock=sellStock+1
        return maxStock
        